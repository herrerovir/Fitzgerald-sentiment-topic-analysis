# notebooks/setup_path.py
import sys
from pathlib import Path

# Add src directory (where config.py lives) to sys.path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))