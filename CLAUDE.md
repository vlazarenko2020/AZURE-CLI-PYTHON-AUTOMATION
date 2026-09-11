# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo does

Small utility scripts for generating sample CSV data and uploading it to Azure Blob Storage:

- `create_10_csv_files.py` — generates synthetic employee CSV files (id, name, DOB, title, salary) into `input_csv_files/`.
- `load_files_to_blob.sh` — uploads the contents of `input_csv_files/` to an Azure Blob Storage container via `az storage blob upload-batch`, using a storage account key.
- `load_files_to_blob.py` — currently empty; intended Python equivalent of the upload step.
- `main.py` — placeholder entry point (`uv run` default), not wired to the rest of the project yet.

## Commands

- Generate sample data: `python create_10_csv_files.py` (writes to `input_csv_files/`, overwriting existing `data_part_*.csv` files).
- Upload to Azure: `./load_files_to_blob.sh` (requires the Azure CLI `az` to be installed and authenticated/configured; edit the `STORAGE_ACCOUNT`, `CONTAINER_NAME`, `BLOB_PREFIX`, and `ACCOUNT_KEY` variables at the top of the script before running).
- Run the placeholder app: `python main.py` (or `uv run main.py`).

Project uses `uv`/`pyproject.toml` (Python >= 3.14, no dependencies declared yet). There is no build, lint, or test tooling configured.

## Security note

`load_files_to_blob.sh` embeds a raw Azure storage **account key** as a shell variable. Never commit real account keys — prefer environment variables, a SAS token, or Azure AD auth (`az storage blob upload-batch --auth-mode login`) instead of embedding keys in the script.
