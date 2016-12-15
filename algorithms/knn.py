from collections import Counter

import numpy as np
from scipy.spatial.distance import euclidean

from algorithm.base import BaseEstimator


class KNNBase(BaseEstimator):

    def __init__(self, k=5, distance_func=euclidean):
        """Base for K-Nearest neighbors classifier and regressor.
        """

        self.k = None if k == 0 else k
        self.distance_func = distance_func

    def aggregate(self, neighbors_targets):
        raise NotImplementedError()

    def _predict(self, X=None):
        predictions = [self._predict_x(x) for x in X]
        return np.array(predictions)

    def _predict_x(self, x):
        """Predict the label of a single instance x."""

        # Compute distances between x and all examples in the training set.
        distances = (self.distance_func(x, example) for example in self.X)

        # Sort all examples by their distance to x and keep their target value,
        neighbors = sorted(((dist, target)
                            for (dist, target) in zip(distances, self.y)),
                           key=lambda x: x[0])

        # Get targets of the k-nn and aggregate them.
        neighbors_targets = [target for (_, target) in neighbors[:self.k]]

        return self.aggregate(neighbors_targets)


class KNNClassifier(KNNBase):
    """Nearest neighbors classifier."""

    def aggregate(self, neighbors_targets):
        """Return the most common target label."""

        most_common_label = Counter(neighbors_targets).most_common(1)[0][0]
        return most_common_label


class KNNRegressor(KNNBase):
    """Nearest neighbors regressor."""

    def aggregate(self, neighbors_targets):
        """Return the mean of all targets."""

        return np.mean(neighbors_targets)
