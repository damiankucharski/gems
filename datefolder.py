import os
from datetime import datetime

def create_directory_with_timestamp(path, prefix):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dir_name = f"{prefix}_{timestamp}"
    full_path = os.path.join(path, dir_name)
    os.makedirs(full_path, exist_ok=True)

    return full_path
