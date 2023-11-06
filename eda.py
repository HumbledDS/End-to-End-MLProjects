
#Convert Json to CSV
import json
import csv

# Read JSON data from a file (example.json)
with open('file3.json', 'r') as json_file:
    data = json.load(json_file)

# Specify the CSV file name to write the output
csv_file = 'fle3.csv'

# Extract the header from JSON keys
header = data[0].keys() if isinstance(data, list) and len(data) > 0 else data.keys()

# Write JSON data to CSV
with open(csv_file, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=header)
    
    # Write CSV header
    csv_writer.writeheader()

    # Write JSON data to CSV rows
    if isinstance(data, list):
        csv_writer.writerows(data)
    else:
        csv_writer.writerow(data)
        
print(f'JSON data has been successfully converted to CSV and saved as {csv_file}.')
