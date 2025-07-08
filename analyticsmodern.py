import pandas as pd
from datetime import datetime

# Function to preprocess the subject lines
def preprocess_subject(subject):
    if isinstance(subject, str):
        if subject.startswith("FW: "):
            return subject[4:]
        elif subject.startswith("RE: "):
            return subject[4:]
    return subject

# Read the CSV file
df = pd.read_csv('outputmodern.csv')

# Preprocess the subject lines
df['Subject'] = df['Subject'].apply(preprocess_subject)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', utc=True)

# Drop rows with NaT in Date column
df = df.dropna(subset=['Date'])

# Group by Subject and calculate the required metrics
grouped = df.groupby('Subject').agg(
    first_email=('Date', 'min'),
    last_email=('Date', 'max')
).reset_index()

# Calculate the time difference
grouped['time_difference'] = grouped['last_email'] - grouped['first_email']

# Save the first CSV
grouped.to_csv('outputtimediffmodern.csv', index=False)

# Extract month and year from the Date column
df['Month'] = df['Date'].dt.to_period('M')

# Group by Month and count distinct subjects
monthly_subjects = df.groupby('Month')['Subject'].nunique().reset_index()

# Rename columns for clarity
monthly_subjects.columns = ['Month', 'Distinct_Subjects']

# Save the second CSV
monthly_subjects.to_csv('outputvolumemodern.csv', index=False)

print("CSV files have been generated successfully.")