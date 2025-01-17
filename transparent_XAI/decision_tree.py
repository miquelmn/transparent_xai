""" Module for the attribution of a decision tree model.

Decision tree models are interpretable models that can be easily explained. This module contains the
algorithm to attribute the importance of each feature in the prediction in a local way.

Author: Miquel Miró Nicolau (UIB), 2025
"""

__version__ = '1.0'
__author__ = 'Miquel Miró Nicolau (UIB)'

import numpy as np

def attribute(estimator, image):
    """ Attribute the importance of each feature in the prediction of a decision tree.

    Args:
        estimator: (sklearn.model). Decision tree model.
        image: (np.array) Image to explain.

    Returns:
        np.array with the attribution of each feature.
    """
    children_left = estimator.tree_.children_left
    children_right = estimator.tree_.children_right
    feature = estimator.tree_.feature
    threshold = estimator.tree_.threshold
    impurity = estimator.tree_.impurity

    importance = {}

    node_id = 0
    while children_left[node_id] != children_right[node_id]:

        if feature[node_id] not in importance:
            importance[feature[node_id]] = 0

        if image[feature[node_id]] <= threshold[node_id]:
            children_id = children_left[node_id]
        else:
            children_id = children_right[node_id]

        importance[feature[node_id]] += (impurity[node_id] - impurity[children_id])
        node_id = children_id

    attribution = np.zeros_like(image).astype(np.float64)

    adder = 0
    for feature, value in importance.items():
        adder += value
        attribution[feature] = value

    attribution /= adder

    return attribution

