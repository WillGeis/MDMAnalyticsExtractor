import os
import pandas as pd
import extract_msg

# Define the root folder containing dated subfolders with .msg files
root_folder_path = r'C:\\Users\\u235211\\OneDrive - Trane Technologies\\Desktop\\Stuff\\CustOnbMDMS\\####EMAIL BACKUPS\\6-2025'

# Initialize an empty list to store the extracted data
data = []

# Loop through all subfolders in the root folder
for subfolder_name in os.listdir(root_folder_path):
    subfolder_path = os.path.join(root_folder_path, subfolder_name)
    
    # Check if the subfolder name is a date in the format '6-2-2025' to '6-26-2025'
    if os.path.isdir(subfolder_path) and subfolder_name.startswith('6-') and subfolder_name.endswith('-2025'):
        # Loop through all files in the subfolder
        for filename in os.listdir(subfolder_path):
            if filename.endswith('.msg'):
                # Create the full file path
                file_path = os.path.join(subfolder_path, filename)
                
                # Load the .msg file
                msg = extract_msg.Message(file_path)
                
                # Extract the required information
                date = msg.date
                subject = msg.subject
                sender = msg.sender
                
                # Append the extracted data to the list, including the subfolder date
                data.append([date, subject, sender, subfolder_name])

# Create a DataFrame from the extracted data
df = pd.DataFrame(data, columns=['Date', 'Subject', 'Sender', 'Folder Date'])

# Save the DataFrame to a .csv file
output_csv_path = r'C:\\Users\\u235211\\OneDrive - Trane Technologies\\Desktop\\outputmodern.csv'
df.to_csv(output_csv_path, index=False)

print(f"Data has been successfully extracted and saved to {output_csv_path}")