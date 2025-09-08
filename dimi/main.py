import pandas as pd
import os

filename = "data.jsonl.gz"
path = os.path.abspath(f"{filename}")

df = pd.read_json(path, lines=True)
print(df)
