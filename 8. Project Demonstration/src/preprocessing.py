import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def load_data(filepath):
    if filepath.endswith('.xlsx') or filepath.endswith('.xls'):
        return pd.read_excel(filepath)
    else:
        return pd.read_csv(filepath)


def handle_missing_values(df, strategy="mean"):
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].isnull().any():
            if df_clean[col].dtype in [np.float64, np.int64]:
                if strategy == "mean":
                    val = df_clean[col].mean()
                elif strategy == "median":
                    val = df_clean[col].median()
                else:
                    val = 0
                df_clean[col] = df_clean[col].fillna(val)
            else:
                val = df_clean[col].mode()[0] if not df_clean[col].mode().empty else "Missing"
                df_clean[col] = df_clean[col].fillna(val)
    return df_clean


def handle_outliers(df, columns=None):
    df_clean = df.copy()
    if columns is None:
        columns = [col for col in df_clean.select_dtypes(include=[np.number]).columns if col != 'flood']
    
    for col in columns:
        q1 = df_clean[col].quantile(0.25)
        q3 = df_clean[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        df_clean[col] = df_clean[col].clip(lower=lower_bound, upper=upper_bound)
        
    return df_clean


def encode_categories(df, columns=None):
    df_clean = df.copy()
    if columns is None:
        columns = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()
    
    if len(columns) > 0:
        df_clean = pd.get_dummies(df_clean, columns=columns, drop_first=True)
        
    return df_clean


def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)


def scale_features(X_train, X_test, scaler_type="standard"):
    if scaler_type == "minmax":
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
        
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns, index=X_train.index)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns, index=X_test.index)
    
    return X_train_scaled, X_test_scaled, scaler


