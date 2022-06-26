import os

BASE = os.path.dirname(os.path.abspath(__file__))
HISTORICAL_DATA_DIRECTORY = os.path.join(BASE, "lib/historical_data")
UI_DIRECTORY = os.path.join(BASE, "lib/modules")

EXECUTION_DIRECTORIES = ['lib/historical_data']
for directory in EXECUTION_DIRECTORIES:
    if not os.path.exists(directory):
        os.makedirs(directory)
        
        