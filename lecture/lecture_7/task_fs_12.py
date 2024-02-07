import os
from pathlib import Path

os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'old_name.py'))
old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)  # перенос с сохранением имени
