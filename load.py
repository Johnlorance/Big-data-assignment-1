import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Check if a file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python load.py <file_path>")
    sys.exit(1)

# Get the file path from the command-line argument
file_path = sys.argv[1]

# Load the dataset into a DataFrame
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)

# Now, let's pass the DataFrame to the next file (dpre.py)
exec(open("app/dpre.py").read())
