from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

def train_decision_tree(X_train, y_train, params=None):
    if params is None:
        params = {}
    
    if 'random_state' not in params:
        params['random_state'] = 42
        
    clf = DecisionTreeClassifier(**params)
    clf.fit(X_train, y_train)
    return clf


def tune_hyperparameters(X_train, y_train, param_grid):
    clf = DecisionTreeClassifier(random_state=42)
    grid_search = GridSearchCV(
        estimator=clf, 
        param_grid=param_grid, 
        cv=5, 
        scoring='f1'
    )
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_, grid_search.best_params_


