import pandas as pd

def extract_top_rows(input_csv_path, output_csv_path, num_rows=10000):
    try:
        # Read the CSV file
        df = pd.read_csv(input_csv_path)
        
        # Select the top rows
        df_top = df.head(num_rows)
        
        # Save to a new CSV file
        df_top.to_csv(output_csv_path, index=False)
        
        print(f"Successfully saved top {num_rows} rows to {output_csv_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_csv = "email.csv"  # Replace with your actual file path
output_csv = "op2.csv"  # Replace with your desired output path
extract_top_rows(input_csv, output_csv)
