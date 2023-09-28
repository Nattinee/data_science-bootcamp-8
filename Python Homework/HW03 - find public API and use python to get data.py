import requests
import pandas as pd

# Make a request to the API
response = requests.get("https://hp-api.onrender.com/api/characters/students")

# Parse the response into JSON
data = response.json()

# Create a Pandas DataFrame from the parsed data
df = pd.DataFrame(data)

# Print the DataFrame
print(df[['name', 'house', 'gender', 'dateOfBirth','ancestry']].head(10))
