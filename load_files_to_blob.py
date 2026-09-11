import os
from pathlib import Path
from azure.storage.blob import BlobServiceClient

# Configuration
STORAGE_ACCOUNT = "vteststorageaccount2026"
CONTAINER_NAME = "test-20260910"
LOCAL_DIR = "input_csv_files"
BLOB_PREFIX = "20260911-1st_load"  # Set to "" to upload to container root

# Read from the AZURE_STORAGE_ACCOUNT_KEY env var; never hardcode a real key here.
ACCOUNT_KEY = os.environ["AZURE_STORAGE_ACCOUNT_KEY"]


def upload_directory():
    account_url = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net"

    blob_service_client = BlobServiceClient(
        account_url=account_url, credential=ACCOUNT_KEY
    )
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    local_path = Path(LOCAL_DIR).resolve()

    if not local_path.is_dir():
        raise ValueError(f"Directory not found: {local_path}")

    print(f"Starting upload from '{local_path}' to '{CONTAINER_NAME}'...")

    for root, _, files in os.walk(local_path):
        for file_name in files:
            full_file_path = Path(root) / file_name

            # Compute relative path to preserve subfolder structures
            relative_path = full_file_path.relative_to(local_path)

            if BLOB_PREFIX:
                blob_name = f"{BLOB_PREFIX}/{relative_path}".replace("\\", "/")
            else:
                blob_name = str(relative_path).replace("\\", "/")

            print(f"Uploading: {relative_path} -> {blob_name}")

            blob_client = container_client.get_blob_client(blob_name)
            with open(full_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

    print("All files uploaded successfully!")


if __name__ == "__main__":
    upload_directory()
