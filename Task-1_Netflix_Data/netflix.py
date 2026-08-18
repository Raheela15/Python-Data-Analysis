import pandas as pd

#  Import the dataset using Python and Pandas

data = pd.read_csv('netflix_titles.csv')             # Load the raw netflix CSV file into a Pandas DataFrame

# Display basic information about total rows and columns
print("Step 1: Dataset Summary ")
print("Total Rows:", data.shape[0])
print("Total Columns:", data.shape[1])


# Identify and handle missing values

print("\n Step 2: Checking Missing Values ")
print(data.isnull().sum())

# Replace missing values in categorical columns with default text
data['director'] = data['director'].fillna('Unknown')
data['cast'] = data['cast'].fillna('Unknown')
data['country'] = data['country'].fillna('Unknown')
data['date_added'] = data['date_added'].fillna('Unknown')
data['rating'] = data['rating'].fillna('Not Rated')
data['duration'] = data['duration'].fillna('Unknown')


# Remove duplicate records and formatting inconsistencies
# Drop duplicate rows if any exist in the dataset
data = data.drop_duplicates()

# Clean extra spaces from text columns
data['title'] = data['title'].str.strip()
data['director'] = data['director'].str.strip()
data['cast'] = data['cast'].str.strip()


# Step 4: Standardize columns such as Country, Rating, and Type
# Remove leading/trailing spaces to standardize text formatting
data['country'] = data['country'].str.strip()
data['rating'] = data['rating'].str.strip()
data['type'] = data['type'].str.strip()


# last: Export the cleaned dataset for analysis
# Save the final processed data to a new CSV file
output_filename = 'netflix_cleaned_data.csv'
data.to_csv(output_filename, index=False)

print("\n last: Process Complete ")
print("Cleaned dataset successfully saved as:", output_filename)