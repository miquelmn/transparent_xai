""" Module containing the implementation of the attribute function for the Linear Regression model.

Linear regression models are interpretable models that can be easily explained. This module contains
the algorithm to attribute the importance of each feature in the prediction in a local way.

Author: Miquel Miró Nicolau (UIB), 2025
"""

__version__ = '1.0.0'
__author__ = 'Miquel Miró Nicolau (UIB)'

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

def attribute(estimator, image):
    """ Attribute the importance of each feature in the prediction of a linear regression model.

    Args:
        estimator: (sklearn.model). Linear regression model.
        image: (np.array) Image to explain.

    Returns:
        np.array with the attribution of each feature.
    """

    weights = estimator.coef_

    expl = weights * image
    expl = scaler.fit_transform(expl.reshape(-1, 1))

    return expl