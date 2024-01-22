
import pandas as pd

def convert_excel_to_json(excel_file_path):
    """
    Converts an Excel file to a JSON file and returns the JSON data.
    
    Parameters:
        - excel_file_path (str): Path to the Excel file.

    Returns:
        - json_data (str): JSON representation of the Excel data.
    """
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(excel_file_path)

        # Convert DataFrame to JSON
        json_data = df.to_json(orient='records')

        return json_data

    except Exception as e:
        raise ValueError(f'Error converting Excel to JSON: {str(e)}')

def save_json_to_file(json_data, json_file_path):
    """
    Saves JSON data to a file.
    
    Parameters:
        - json_data (str): JSON data to be saved.
        - json_file_path (str): Path for the output JSON file.
    """
    try:
        # Write JSON data to a file
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)

    except Exception as e:
        raise ValueError(f'Error saving JSON to file: {str(e)}')
