from pathlib import Path

# Path to the root of the project (one level above main.py)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Now build correct paths
CONFIG_FILE_PATH = ROOT_DIR / 'config' / 'config.yaml'
PARAMS_FILE_PATH = ROOT_DIR / 'params.yaml'
SCHEMA_FILE_PATH = ROOT_DIR / 'schema.yaml'
