"""
shap_utils.py — Reusable SHAP explanation utilities for tree-based
and linear scikit-learn models on the California Housing dataset.

Key concepts embedded in this module:
- TreeExplainer vs KernelExplainer selection
- Shapley additivity property
- MDI vs SHAP importance comparison

Author: Data Science Lab
"""

from __future__ import annotations

import warnings
from typing import Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shap
from sklearn.base import BaseEstimator, is_classifier
from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.inspection import permutation_importance
from sklearn.tree import DecisionTreeRegressor

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

# Type alias for the tree models TreeExplainer supports natively
TreeModel = Union[
    DecisionTreeRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor,
]


def _get_explainer(
    model: BaseEstimator,
    X: np.ndarray,
) -> shap.Explainer:
    """
    Select the right SHAP explainer for the model type.

    ── How TreeExplainer differs from KernelExplainer ──
    • TreeExplainer exploits the internal tree structure to compute
      *exact* Shapley values in O(TLD²) time, where T = #trees,
      L = #leaves, D = depth.  It is specific to tree-based models.
    • KernelExplainer is model-agnostic: it approximates Shapley values
      by sampling coalitions of features and fitting a weighted linear
      model (LIME-style), so it works on *any* predict function but
      is much slower and introduces sampling variance.

    We prefer TreeExplainer whenever the model is tree-based.
    """
    tree_types = (
        DecisionTreeRegressor,
        RandomForestRegressor,
        GradientBoostingRegressor,
    )
    if isinstance(model, tree_types):
        return shap.TreeExplainer(model)
    else:
        # Fall back to the model-agnostic explainer with a subsample
        # of the background data to keep runtime manageable.
        background = shap.sample(X, min(100, X.shape[0]))
        return shap.KernelExplainer(model.predict, background)


def _compute_shap_values(
    model: BaseEstimator,
    X: np.ndarray,
    feature_names: Optional[list[str]] = None,
) -> shap.Explanation:
    """
    Compute SHAP values and return a full shap.Explanation object.

    ── Why SHAP values are additive (Shapley property) ──
    For every prediction f(x), the Shapley values φ_j satisfy:
        f(x) = E[f(X)]  +  Σ_j  φ_j(x)
    This *additivity* (or "efficiency") axiom guarantees that the
    contributions of all features sum exactly to the difference
    between the model output and the expected (base) value.
    This is not an approximation — it is a mathematical identity
    inherited from cooperative game theory.
    """
    explainer = _get_explainer(model, X)
    shap_values = explainer(X)

    # Attach human-readable feature names if provided
    if feature_names is not None:
        shap_values.feature_names = feature_names

    return shap_values


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def explain_prediction(
    model: BaseEstimator,
    X: np.ndarray,
    idx: int,
    feature_names: Optional[list[str]] = None,
    max_display: int = 10,
) -> plt.Figure:
    """
    Generate a SHAP waterfall plot for a single observation.

    Parameters
    ----------
    model : fitted scikit-learn estimator
    X : array-like of shape (n_samples, n_features)
        The dataset (train or test) from which to pick the observation.
    idx : int
        Row index of the observation to explain.
    feature_names : list[str], optional
        Human-readable names for each feature.
    max_display : int
        Maximum number of features to show (default 10).

    Returns
    -------
    matplotlib.figure.Figure
        The waterfall plot figure (also displayed via plt.show).

    Raises
    ------
    IndexError
        If idx is out of bounds for X.
    """
    if idx < 0 or idx >= X.shape[0]:
        raise IndexError(
            f"idx={idx} is out of bounds for X with {X.shape[0]} rows."
        )

    shap_values = _compute_shap_values(model, X, feature_names)

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.sca(ax)
    shap.plots.waterfall(shap_values[idx], max_display=max_display, show=False)
    plt.title(f"SHAP Waterfall — Observation {idx}", fontsize=13)
    plt.tight_layout()
    plt.show()
    return fig


def global_importance(
    model: BaseEstimator,
    X: np.ndarray,
    feature_names: Optional[list[str]] = None,
    max_display: int = 10,
) -> plt.Figure:
    """
    Generate a SHAP beeswarm plot showing global feature importance.

    The beeswarm arranges every observation's SHAP value for every
    feature on the x-axis, coloured by the feature value.  This
    reveals not just *which* features matter but *how* they matter
    (direction + magnitude + interaction spread).

    Parameters
    ----------
    model : fitted estimator
    X : array-like (n_samples, n_features)
    feature_names : list[str], optional
    max_display : int

    Returns
    -------
    matplotlib.figure.Figure
    """
    shap_values = _compute_shap_values(model, X, feature_names)

    fig, ax = plt.subplots(figsize=(10, 7))
    plt.sca(ax)
    shap.plots.beeswarm(shap_values, max_display=max_display, show=False)
    plt.title("SHAP Beeswarm — Global Feature Importance", fontsize=13)
    plt.tight_layout()
    plt.show()
    return fig


def compare_importance(
    model: BaseEstimator,
    X: np.ndarray,
    y: np.ndarray,
    feature_names: Optional[list[str]] = None,
    n_repeats: int = 10,
    random_state: int = 42,
) -> pd.DataFrame:
    """
    Side-by-side comparison of MDI, Permutation, and SHAP importance.

    MDI (Mean Decrease in Impurity) is fast but biased toward
    high-cardinality / noisy features because splits on such
    features reduce impurity a lot even when they don't generalise.
    SHAP importance (mean |φ_j|) is grounded in game theory and
    is additive + consistent.  Permutation importance measures the
    drop in test-set performance when a feature is shuffled, giving
    a model-agnostic, unbiased ranking.

    Parameters
    ----------
    model : fitted tree-based estimator (must expose feature_importances_)
    X, y : test data for permutation importance
    feature_names : list[str], optional
    n_repeats : int – repeats for permutation importance
    random_state : int

    Returns
    -------
    pd.DataFrame
        Columns: feature, mdi_rank, perm_rank, shap_rank,
                 mdi_value, perm_value, shap_value

    Also displays a grouped bar chart comparing the three methods.
    """
    if not hasattr(model, "feature_importances_"):
        raise AttributeError(
            "model must expose `feature_importances_` (tree-based). "
            "Got: " + type(model).__name__
        )

    names = (
        list(feature_names)
        if feature_names is not None
        else [f"x{i}" for i in range(X.shape[1])]
    )

    # 1. MDI importance
    mdi = model.feature_importances_

    # 2. Permutation importance (on the supplied X, y — should be test set)
    perm = permutation_importance(
        model, X, y, n_repeats=n_repeats, random_state=random_state
    )
    perm_mean = perm.importances_mean

    # 3. SHAP importance = mean |SHAP value| per feature
    shap_values = _compute_shap_values(model, X, names)
    shap_imp = np.abs(shap_values.values).mean(axis=0)

    # Build comparison DataFrame
    df = pd.DataFrame(
        {
            "feature": names,
            "mdi_value": mdi,
            "perm_value": perm_mean,
            "shap_value": shap_imp,
        }
    )
    # Rank (1 = most important)
    for col in ["mdi_value", "perm_value", "shap_value"]:
        df[col.replace("value", "rank")] = df[col].rank(ascending=False).astype(int)

    df = df[
        [
            "feature",
            "mdi_rank",
            "perm_rank",
            "shap_rank",
            "mdi_value",
            "perm_value",
            "shap_value",
        ]
    ]

    # ── Visualisation: grouped horizontal bar chart ──
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    methods = [
        ("mdi_value", "MDI (Gini)", "#e07b54"),
        ("perm_value", "Permutation", "#54a0e0"),
        ("shap_value", "SHAP mean(|φ|)", "#6cc070"),
    ]
    order = df.sort_values("shap_value", ascending=True)

    for ax, (col, title, colour) in zip(axes, methods):
        ax.barh(order["feature"], order[col], color=colour, edgecolor="white")
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_xlabel("Importance")

    plt.suptitle(
        "Feature Importance: MDI vs Permutation vs SHAP",
        fontsize=14,
        fontweight="bold",
        y=1.02,
    )
    plt.tight_layout()
    plt.show()

    return df
