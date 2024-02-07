import os
from pathlib import Path

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
