import pandas as pd
import numpy as np
from scipy import stats

class DataCleaner:
    def __init__(self):
        self.df = None

    def load_dataset(self, file_path):
        if file_path.endswith('.csv'):
            self.df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            self.df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
        print("Dataset loaded successfully.")

    def identify_binary_columns(self):
        # Identifying columns with only 0 and 1 values
        self.binary_cols = [
            col for col in self.df.columns
            if self.df[col].dropna().unique().tolist() in ([0, 1], [1, 0], [0], [1])
            and self.df[col].dtype in [np.int64, np.int32, np.int16, np.int8, np.int0]
        ]

    def get_initial_analysis(self):
        total_rows = self.df.shape[0]
        rows_with_missing = self.df[self.df.isnull().any(axis=1)].shape[0]
        duplicate_rows = self.df.duplicated().sum()

        # Identifying numerical columns excluding binary columns
        self.identify_binary_columns()
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in self.binary_cols]

        # Handle outliers for numerical columns
        if numerical_cols:
            z_scores = np.abs(stats.zscore(self.df[numerical_cols].dropna()))
            outliers = (z_scores > 3).sum().sum()
        else:
            outliers = 0

        counts = {
            'Total Rows': total_rows,
            'Rows with Missing Values': rows_with_missing,
            'Duplicate Rows': duplicate_rows,
            'Outliers': outliers
        }

        return counts

    def handle_missing_values(self, action, method=None):
        total_missing = self.df.isnull().sum().sum()
        total_values = self.df.size
        missing_percentage = (total_missing / total_values) * 100

        if action == 'impute':
            for column in self.df.columns:
                if column in self.binary_cols:
                    # Impute binary columns with mode
                    self.df[column].fillna(self.df[column].mode()[0], inplace=True)
                elif self.df[column].dtype in [np.float64, np.float32, np.int64, np.int32]:
                    if method in ['mean', 'median']:
                        if method == 'mean':
                            self.df[column].fillna(self.df[column].mean(), inplace=True)
                        else:
                            self.df[column].fillna(self.df[column].median(), inplace=True)
                    else:
                        raise ValueError("Invalid imputation method selected.")
                else:
                    # For categorical variables, filling with mode
                    self.df[column].fillna(self.df[column].mode()[0], inplace=True)
        elif action == 'remove':
            if missing_percentage <= 20:
                self.df.dropna(inplace=True)
            else:
                for column in self.df.columns:
                    if column in self.binary_cols or self.df[column].dtype == 'object':
                        self.df[column].fillna(self.df[column].mode()[0], inplace=True)
                    else:
                        self.df[column].fillna(self.df[column].mean(), inplace=True)
        else:
            raise ValueError("Invalid action selected.")

    def remove_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def handle_outliers(self, method):
        # Identifying numerical columns excluding binary columns
        self.identify_binary_columns()
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        numerical_cols = [col for col in numerical_cols if col not in self.binary_cols]

        if numerical_cols:
            if method == 'IQR':
                for col in numerical_cols:
                    Q1 = self.df[col].quantile(0.25)
                    Q3 = self.df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    self.df[col] = np.where(
                        (self.df[col] < lower_bound) | (self.df[col] > upper_bound),
                        np.nan,
                        self.df[col]
                    )
                    self.df[col].fillna(self.df[col].median(), inplace=True)
            elif method == 'z-score':
                z_scores = np.abs(stats.zscore(self.df[numerical_cols]))
                filter = (z_scores < 3).all(axis=1)
                self.df = self.df[filter]
            else:
                raise ValueError("Invalid outlier detection method selected.")

    def save_cleaned_data(self, output_file):
        # Ensuring binary columns are cast back to integer type
        self.identify_binary_columns()
        for col in self.binary_cols:
            self.df[col] = self.df[col].astype(int)
        if output_file.endswith('.csv'):
            self.df.to_csv(output_file, index=False)
        elif output_file.endswith(('.xls', '.xlsx')):
            self.df.to_excel(output_file, index=False)
        else:
            self.df.to_csv(output_file + '.csv', index=False)
