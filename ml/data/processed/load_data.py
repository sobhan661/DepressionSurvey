import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


df = pd.read_csv(f"{BASE_DIR}\\raw\\Teen_Mental_Health_Dataset.csv")