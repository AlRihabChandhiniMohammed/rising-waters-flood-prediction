"""
XGBoost Module — Rising-Waters-Flood-Prediction

Trains and evaluates an XGBoost classifier for flood prediction.
"""

from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

def train_xgboost(X_train, y_train, params=None):
    """Train an XGBoost classifier with optional hyperparameters."""
    if params is None:
        params = {}
    if 'random_state' not in params:
        params['random_state'] = 42
    if 'eval_metric' not in params:
        params['eval_metric'] = 'logloss'
    if 'scale_pos_weight' not in params:
        num_neg = (y_train == 0).sum()
        num_pos = (y_train == 1).sum()
        params['scale_pos_weight'] = num_neg / num_pos if num_pos > 0 else 1.0
        
    clf = XGBClassifier(**params)
    clf.fit(X_train, y_train)
    return clf


def tune_hyperparameters(X_train, y_train, param_grid):
    """Perform grid search to optimize XGBoost parameters."""
    num_neg = (y_train == 0).sum()
    num_pos = (y_train == 1).sum()
    scale = num_neg / num_pos if num_pos > 0 else 1.0
    
    clf = XGBClassifier(random_state=42, eval_metric='logloss', scale_pos_weight=scale)
    grid_search = GridSearchCV(
        estimator=clf,
        param_grid=param_grid,
        cv=5,
        scoring='f1'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_

