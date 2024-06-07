from pathlib import Path
import os

PARENT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PARENT_DIR / 'data'
RAW_DATA_DIR = PARENT_DIR / 'data' / 'raw'
TRANSFORMED_DATA_DIR = PARENT_DIR / 'data' / 'transformed'

if not Path(DATA_DIR):
    os.makedir(DATA_DIR)

if not Path(RAW_DATA_DIR):
    os.makedir(RAW_DATA_DIR)

if not Path(TRANSFORMED_DATA_DIR):
    os.makedir(TRANSFORMED_DATA_DIR)
