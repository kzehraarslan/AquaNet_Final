"""Metric utilities for binary water/land segmentation."""

import numpy as np


def _to_bool(mask):
    """Convert numeric mask to boolean water mask."""
    return np.asarray(mask).astype(bool)


def iou_score(y_true, y_pred, eps=1e-7):
    """Intersection over Union for binary masks."""
    y_true = _to_bool(y_true)
    y_pred = _to_bool(y_pred)
    intersection = np.logical_and(y_true, y_pred).sum()
    union = np.logical_or(y_true, y_pred).sum()
    return float((intersection + eps) / (union + eps))


def f1_score_binary(y_true, y_pred, eps=1e-7):
    """F1-score for binary water/land masks."""
    y_true = _to_bool(y_true)
    y_pred = _to_bool(y_pred)
    tp = np.logical_and(y_true, y_pred).sum()
    fp = np.logical_and(~y_true, y_pred).sum()
    fn = np.logical_and(y_true, ~y_pred).sum()
    precision = (tp + eps) / (tp + fp + eps)
    recall = (tp + eps) / (tp + fn + eps)
    return float(2 * precision * recall / (precision + recall + eps))


def normalized_confusion_matrix(y_true, y_pred):
    """Return row-normalized confusion matrix [[TN, FP], [FN, TP]]."""
    y_true = _to_bool(y_true).ravel()
    y_pred = _to_bool(y_pred).ravel()
    tn = np.logical_and(~y_true, ~y_pred).sum()
    fp = np.logical_and(~y_true, y_pred).sum()
    fn = np.logical_and(y_true, ~y_pred).sum()
    tp = np.logical_and(y_true, y_pred).sum()
    cm = np.array([[tn, fp], [fn, tp]], dtype=float)
    row_sum = cm.sum(axis=1, keepdims=True)
    row_sum[row_sum == 0] = 1.0
    return cm / row_sum
