#!/usr/bin/env bash
set -euo pipefail

# Configuration
STORAGE_ACCOUNT="vteststorageaccount2026"
CONTAINER_NAME="test-20260910"
LOCAL_DIR="input_csv_files"
BLOB_PREFIX="20260911-1st_load" # Optional prefix in container, leave empty ("") for root

# Read from the AZURE_STORAGE_ACCOUNT_KEY env var; never hardcode a real key here.
: "${AZURE_STORAGE_ACCOUNT_KEY:?AZURE_STORAGE_ACCOUNT_KEY must be set}"
ACCOUNT_KEY="${AZURE_STORAGE_ACCOUNT_KEY}"

# Determine target destination (with or without prefix)
if [ -n "${BLOB_PREFIX}" ]; then
    TARGET_DEST="${CONTAINER_NAME}/${BLOB_PREFIX}"
else
    TARGET_DEST="${CONTAINER_NAME}"
fi

echo "Uploading files from '${LOCAL_DIR}' to container '${TARGET_DEST}'..."

# Upload directory recursively using storage account key
az storage blob upload-batch \
    --account-name "${STORAGE_ACCOUNT}" \
    --account-key "${ACCOUNT_KEY}" \
    --destination "${TARGET_DEST}" \
    --source "${LOCAL_DIR}" \
    --overwrite

echo "Upload complete!"
