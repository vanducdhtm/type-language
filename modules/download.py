import os
import requests
import subprocess


def download_mongodb(current_folder):
    mongodb_url = r"https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.3-signed.msi"
    
    msi_path = os.path.join(
        current_folder, 
        mongodb_url.split("/")[-1]
    )

    # Download the MongoDB installation software
    response = requests.get(mongodb_url, stream=True)

    with open(msi_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    # Open this software
    subprocess.run([msi_path], shell=True)

    # After that, delete the MongoDB installation software
    os.remove(msi_path)
