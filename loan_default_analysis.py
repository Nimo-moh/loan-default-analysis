import os
import pandas as pd
from scipy.stats import zscore

# Step 1: Load the Dataset
try:
    file_path = "Loan_default.csv"  # Ensure the CSV is in the same directory as this script
    df = pd.read_csv(file_path)
    print(f"Successfully loaded data from {file_path}")
except FileNotFoundError:
    print("Error: File not found. Please ensure 'Loan_default.csv' is in the script directory.")
    exit()

# Step 2: Process Numerical Columns
numeric_cols = ['Age', 'Income', 'LoanAmount', 'CreditScore',
                'MonthsEmployed', 'NumCreditLines', 'InterestRate',
                'LoanTerm', 'DTIRatio']

# Calculate Z-scores and filter rows
try:
    z_scores = df[numeric_cols].apply(zscore)
    data = df[(z_scores < 3).all(axis=1)]
    print("Successfully applied Z-score normalization and filtered outliers.")
except KeyError as e:
    print(f"Error: Missing column in dataset: {e}")
    exit()

# Step 3: Process Categorical Columns
categorical_cols = ['Education', 'EmploymentType', 'MaritalStatus',
                    'HasMortgage', 'HasDependents', 'LoanPurpose', 'HasCoSigner']

for col in categorical_cols:
    if col in data.columns:
        data[col] = data[col].str.strip().str.title()
    else:
        print(f"Warning: Column '{col}' not found in dataset. Skipping.")

# Step 4: Save the Cleaned Data
output_file = "Cleaned_Loan_default.csv"
try:
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
except Exception as e:
    print(f"Error: Could not save cleaned data. {e}")

# End of script
