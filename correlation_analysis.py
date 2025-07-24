import pandas as pd

# Step 1: Load the CSV files
inventory_df = pd.read_csv("retail_inventory_data.csv")
transaction_df = pd.read_csv("retail_transaction_data.csv")

# Step 2: Merge the two DataFrames on Product_ID
merged_df = pd.merge(transaction_df, inventory_df, on='Product_ID', how='inner')

# Step 3: Calculate correlation between Inventory_Days and Profit
# Make sure 'Inventory_Days' and 'Profit' columns exist
if 'Inventory_Days' in merged_df.columns and 'Profit' in merged_df.columns:
    correlation = merged_df['Inventory_Days'].corr(merged_df['Profit'])
    print("Correlation between Inventory Days and Profitability:", round(correlation, 4))
else:
    print("One or both columns 'Inventory_Days' and 'Profit' not found in merged data.")
