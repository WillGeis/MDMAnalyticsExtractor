import os
import pandas as pd
import extract_msg

# Define the folder containing .msg files
folder_path = r'' # This is where you put your folder path to extract information, for windows machines r'C:\\ . . .'

# Initialize an empty list to store the extracted data
data = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.msg'):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Load the .msg file
        msg = extract_msg.Message(file_path)
        
        # Extract the required information
        date = msg.date
        subject = msg.subject
        sender = msg.sender
        
        # Append the extracted data to the list
        data.append([date, subject, sender])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Date', 'Subject', 'Sender'])

# Save the DataFrame to a .csv file
output_csv_path = r'C:\\Users\\u235211\\OneDrive - Trane Technologies\\Desktop\\output.csv'
df.to_csv(output_csv_path, index=False)

print(f"Data has been successfully extracted and saved to {output_csv_path}")
