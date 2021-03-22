import os
from datetime import datetime


def get_upload_path(instance, filename):
    folder = f'uploaded_{instance.login}'
    name = f'picture_{datetime.now().microsecond}.{filename.split(".")[-1]}'
    return os.path.join(folder, name)
