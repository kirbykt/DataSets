import logging
import re

# Set up logging
logging.basicConfig(filename='file.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Clean column names
def clean_column_names(col_list):
    cleaned = [re.sub('[^A-Za-z0-9_]+', '', col.strip().replace(' ', '_')) for col in col_list]
    return cleaned

# Validate headers
def col_header_val(expected_list, actual_list):
    if expected_list == actual_list:
        logging.info("Column names match expected values.")
        return True
    else:
        logging.warning(f"Mismatch in column names.\nExpected: {expected_list}\nActual: {actual_list}")
        return False
