import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Import model modules
from preprocessing import load_data, handle_missing_values, handle_outliers, encode_categories, split_data, scale_features
from decision_tree import tune_hyperparameters as tune_dt
from random_forest import tune_hyperparameters as tune_rf
from knn import find_optimal_k
from xgboost_model import tune_hyperparameters as tune_xgb

def train_all_models(X_train, y_train):
    """Train and tune Decision Tree, Random Forest, KNN, and XGBoost models."""
    print("Training Decision Tree...")
    dt_grid = {
        'max_depth': [3, 5, 8, 10, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    best_dt, dt_params = tune_dt(X_train, y_train, dt_grid)
    print(f"Best Decision Tree params: {dt_params}")
    
    print("\nTraining Random Forest...")
    rf_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 8, None],
        'min_samples_split': [2, 5, 10]
    }
    best_rf, rf_params = tune_rf(X_train, y_train, rf_grid)
    print(f"Best Random Forest params: {rf_params}")
    
    print("\nTraining K-Nearest Neighbors...")
    knn_range = [3, 5, 7, 9, 11, 15]
    best_knn, knn_params = find_optimal_k(X_train, y_train, knn_range)
    print(f"Best KNN params (k): {knn_params}")
    
    print("\nTraining XGBoost...")
    xgb_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2]
    }
    best_xgb, xgb_params = tune_xgb(X_train, y_train, xgb_grid)
    print(f"Best XGBoost params: {xgb_params}")
    
    return {
        'Decision Tree': best_dt,
        'Random Forest': best_rf,
        'KNN': best_knn,
        'XGBoost': best_xgb
    }


def evaluate_models(models, X_test, y_test):
    """Compare models using accuracy, precision, recall, and F1-score."""
    results = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        results[name] = {
            'model': model,
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, zero_division=0),
            'recall': recall_score(y_test, y_pred, zero_division=0),
            'f1_score': f1_score(y_test, y_pred, zero_division=0)
        }
    return results


def select_best_model(results):
    """Return the best-performing model based on evaluation metrics."""
    best_name = None
    best_score = -1
    best_model = None
    
    for name, metrics in results.items():
        score = metrics['f1_score']
        if score > best_score:
            best_score = score
            best_name = name
            best_model = metrics['model']
            
    return best_name, best_model


def save_comparison_report(results, filepath):
    """Write model comparison results to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    lines = []
    lines.append("Model Comparison Report")
    lines.append("=======================")
    lines.append("")
    lines.append(f"{'Model':<20} | {'Accuracy':<10} | {'Precision':<10} | {'Recall':<10} | {'F1-Score':<10}")
    lines.append("-" * 71)
    
    for name, metrics in results.items():
        lines.append(
            f"{name:<20} | {metrics['accuracy']:<10.4f} | {metrics['precision']:<10.4f} | {metrics['recall']:<10.4f} | {metrics['f1_score']:<10.4f}"
        )
    
    report_content = '\n'.join(lines)
    with open(filepath, 'w') as f:
        f.write(report_content)
    
    print("\n--- Model Evaluation Results ---")
    print(report_content)


if __name__ == "__main__":
    # Resolve relative paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
    
    dataset_path = os.path.join(project_root, "3. Project Design Phase", "dataset", "raw", "flood dataset.xlsx")
    models_dir = os.path.join(project_root, "5. Project Development Phase", "models")
    report_path = os.path.join(project_root, "5. Project Development Phase", "model_comparison_report.txt")
    
    os.makedirs(models_dir, exist_ok=True)
    
    print(f"Loading dataset from: {dataset_path}")
    df = load_data(dataset_path)
    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = encode_categories(df)
    
    X = df.drop(columns=['flood'])
    y = df['flood']
    
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    
    print(f"Train size: {X_train_scaled.shape}, Test size: {X_test_scaled.shape}")
    
    # Train all models
    models = train_all_models(X_train_scaled, y_train)
    
    # Evaluate models
    results = evaluate_models(models, X_test_scaled, y_test)
    
    # Save comparison report
    save_comparison_report(results, report_path)
    
    # Select best model
    best_name, best_model = select_best_model(results)
    print(f"\nBest Model Selected: {best_name} (F1-score: {results[best_name]['f1_score']:.4f})")
    
    # Save best model and scaler
    model_save_path = os.path.join(models_dir, "best_model.pkl")
    scaler_save_path = os.path.join(models_dir, "scaler.pkl")
    
    joblib.dump(best_model, model_save_path)
    joblib.dump(scaler, scaler_save_path)
    print(f"Best model saved to: {model_save_path}")
    print(f"Scaler saved to: {scaler_save_path}")

