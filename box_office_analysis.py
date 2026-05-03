"""
Box Office Revenue Prediction - EDA and Linear Regression

This module performs exploratory data analysis and builds a linear regression model
to predict box office revenue for movies using the TMDB dataset.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Tuple, Dict, Optional, List
import warnings
import json
import re

warnings.filterwarnings('ignore')


def load_data(train_path: str, test_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load training and test datasets from CSV files."""
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    return train_data, test_data


def get_data_info(df: pd.DataFrame, name: str = "Dataset") -> None:
    """Print basic information about the dataset."""
    print(f"\n=== {name} Information ===")
    print(f"Shape: {df.shape}")
    print(f"\nColumn Info:")
    print(df.info())
    print(f"\nMissing Values:")
    print(pd.DataFrame(df.isnull().sum(), columns=['Missing_Count']).T)
    print(f"\nMissing Percentage:")
    missing_pct = (df.isnull().sum() / len(df)) * 100
    print(pd.DataFrame(missing_pct, columns=['Missing_Pct']).T)


def visualize_missing_data(df: pd.DataFrame, title: str = "Missing Data Visualization") -> None:
    """Create a bar chart visualization of missing data."""
    plt.figure(figsize=(15, 8))
    missing_data = df.isnull().sum()
    missing_pct = (missing_data / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing_Count': missing_data,
        'Missing_Percentage': missing_pct
    })
    missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Percentage', ascending=False)
    
    if len(missing_df) > 0:
        plt.bar(range(len(missing_df)), missing_df['Missing_Percentage'])
        plt.xticks(range(len(missing_df)), missing_df.index, rotation=90)
        plt.ylabel('Percentage of Missing Values (%)')
        plt.title(title)
        plt.tight_layout()
        plt.show()
    else:
        print("No missing values to visualize.")


def parse_json_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Parse JSON-formatted string columns into usable data."""
    def safe_parse(x):
        if pd.isna(x):
            return []
        try:
            return json.loads(x)
        except (json.JSONDecodeError, TypeError):
            return []
    
    df[f'{column}_parsed'] = df[column].apply(safe_parse)
    return df


def extract_features_from_json(df: pd.DataFrame, column: str, key: str = 'name') -> List[str]:
    """Extract specific features from parsed JSON columns."""
    result = []
    for item in df[f'{column}_parsed']:
        if isinstance(item, list):
            names = [x.get(key, '') for x in item if isinstance(x, dict)]
            result.append(', '.join(names))
        else:
            result.append('')
    return result


def handle_missing_values(df: pd.DataFrame, strategy: Dict[str, str] = None) -> pd.DataFrame:
    """Handle missing values based on specified strategies."""
    df_copy = df.copy()
    
    if strategy is None:
        strategy = {
            'runtime': 'median',
            'budget': 'median',
            'revenue': 'median',
            'belongs_to_collection': 'fill_value',
            'homepage': 'fill_value',
            'tagline': 'fill_value'
        }
    
    for column, method in strategy.items():
        if column not in df_copy.columns:
            continue
            
        if method == 'median':
            df_copy[column] = df_copy[column].fillna(df_copy[column].median())
        elif method == 'mean':
            df_copy[column] = df_copy[column].fillna(df_copy[column].mean())
        elif method == 'fill_value':
            df_copy[column] = df_copy[column].fillna('None')
        elif method == 'drop':
            df_copy = df_copy.dropna(subset=[column])
    
    return df_copy


def create_correlation_heatmap(df: pd.DataFrame, numeric_cols: List[str], title: str = "Correlation Heatmap") -> None:
    """Create a correlation heatmap for numeric columns."""
    plt.figure(figsize=(12, 10))
    corr_matrix = df[numeric_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
    plt.title(title)
    plt.tight_layout()
    plt.show()


def main():
    """Main function to run the EDA pipeline."""
    # Note: Update paths to match your environment
    # For Kaggle: '../input/tmdb-box-office-prediction/train.csv'
    # For local: adjust accordingly
    train_path = '../input/tmdb-box-office-prediction/train.csv'
    test_path = '../input/tmdb-box-office-prediction/test.csv'
    
    try:
        # Load data
        train_data, test_data = load_data(train_path, test_path)
        
        # Display basic info
        get_data_info(train_data, "Training Data")
        get_data_info(test_data, "Test Data")
        
        # Visualize missing data
        visualize_missing_data(train_data, "Training Data - Missing Values")
        visualize_missing_data(test_data, "Test Data - Missing Values")
        
        # Basic statistics
        print("\n=== Training Data Statistics ===")
        print(train_data.describe())
        
        print("\n=== Test Data Statistics ===")
        print(test_data.describe())
        
        # Parse JSON columns (for future feature engineering)
        json_columns = ['belongs_to_collection', 'genres', 'production_companies', 
                       'production_countries', 'spoken_languages', 'Keywords', 'cast', 'crew']
        
        for col in json_columns:
            if col in train_data.columns:
                train_data = parse_json_column(train_data, col)
        
        # Handle missing values
        train_cleaned = handle_missing_values(train_data)
        
        # Create correlation analysis for numeric features
        numeric_features = ['budget', 'popularity', 'runtime', 'revenue']
        available_numeric = [col for col in numeric_features if col in train_cleaned.columns]
        
        if len(available_numeric) >= 2:
            create_correlation_heatmap(train_cleaned, available_numeric, 
                                      "Correlation Matrix - Numeric Features")
        
        print("\n=== EDA Complete ===")
        print("Next steps: Feature engineering, model building, and evaluation")
        
    except FileNotFoundError as e:
        print(f"Error: Could not find data files. Please update the paths.")
        print(f"Details: {e}")


if __name__ == "__main__":
    main()
