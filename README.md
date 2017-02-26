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
	COPYPASTE_SUCCESS: File was successfully copy/pasted/overwritten
	COPYPASTE_FAIL: File specified does not exist


2) Create_GlacierVault.py
Script takes the following parameter:
- String for new vault name

	A request for a new vault with inputted name is sent to AWS Glacier.
	Credentials stored on user root are used (IAM must be properly configured)

	Reporting:
	- Script will print one line with response from AWS Glacier

3) CopyPastOverwritetoS3.py
Script takes the following parameters:
- Path of a directory to copy from (source)
- Path of a directory to move to on S3 (destination)

 If dest does not already exist, it will be created, and all files are coped over
 preserving folder structure.
 If dest folder already exists, all files from source will overwrite colliding files
 in destination

  Reporting:
	-TBD
