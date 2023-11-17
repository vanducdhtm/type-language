import os
from modules.download import download_mongodb


# Check whether the computer has installed MongoDB or not.
mongodb_path = r"C:\Program Files\MongoDB"
current_folder = os.getcwd()

if not os.path.exists(mongodb_path):
    download_mongodb(current_folder)
