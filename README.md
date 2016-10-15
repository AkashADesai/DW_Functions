# DW_Functions
DataWarehousing Fuctions

1) CopyPasteOverwrite.py
Script takes the following parameters:
- Path of a directory to copy from (source)
- Path of a directory to move to (destination).

	If dest does not already exist, it will be created, and all files are copied over preserving folder structure.
	If dest folder already exists, all files from source will overwrite colliding files in destination

- Optionally, takes a list of file names if provided, and only copy/pastes/overwrites those file paths.

Reporting:
-Status keywords are the following:
	COPYPASTE_SUCCESS: File was successfully unzipped
	COPYPASTE_FAIL: File specified does not exist in the archive
