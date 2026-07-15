"""
K-Nearest Neighbors Module — Rising-Waters-Flood-Prediction

Trains and evaluates a KNN classifier for flood prediction.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def train_knn(X_train, y_train, n_neighbors=5):
    """Train a K-Nearest Neighbors classifier."""
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    return clf


def find_optimal_k(X_train, y_train, k_range):
    """Evaluate different K values to find the optimal neighbor count."""
    clf = KNeighborsClassifier()
    grid_search = GridSearchCV(
        estimator=clf,
        param_grid={'n_neighbors': k_range},
        cv=5,
        scoring='f1'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_

