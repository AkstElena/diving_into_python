import os
from pathlib import Path

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
