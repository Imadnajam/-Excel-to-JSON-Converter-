import pandas as pd
import os

def excel_to_json(excel_file_path, json_file_path):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file_path)

        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')

        # Write JSON data to a file
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)

        print(f'Success! JSON file saved at {json_file_path}')

    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == "__main__":
    # Get the path to the Excel file
    excel_file_path = input('Enter the path to the Excel file: ')

    # Validate that the file exists
    if not os.path.isfile(excel_file_path):
        print('Error: Excel file not found.')
    else:
        # Get the path for the output JSON file
        json_file_path = input('Enter the path for the output JSON file: ')

        # Call the conversion function
        excel_to_json(excel_file_path, json_file_path)
