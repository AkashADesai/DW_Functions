import os
import shutil
import argparse
import distutils.core

"""
CopyPasteOrOverwrite Files
--

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

-Eventually toss into an R dataset

"""

# argparser = argparse.ArgumentParser()
# argparser.add_argument("srcPath")
# argparser.add_argument("destPath")
# argparser.add_argument("pathsToMove", nargs="*")
# args = argparser.parse_args()

# srcPath = args.srcPath
# destPath = args.destPath
# pathsToMove = args.pathsToMove

# srcPath = r'/Users/akashdesai/Akash_DW/mastercode/Pythonscripts/test_source'
# destPath = r'/Users/akashdesai/Akash_DW/mastercode/Pythonscripts/test_destination'
# pathsToMove = ["test1.txt", "test1.txt"]
# pathsToMove = ["test1.txt", "test2.txt", "garbage.txt"]
# pathsToMove = ["test1.txt"]
# pathsToMove = ["garbage"]
# pathsToMove = []

pathsMovedSucc = []
paths_not_found = []

if len(pathsToMove) == 0:
	print(" *\* CopyPaste or Overwrite Directory */* ")
	print()
	srcLeaf = os.path.basename(srcPath)
	dest_path = os.path.join(destPath,srcLeaf)
	if os.path.exists(srcPath) is True:
		print("COPYPASTE_SUCCESS: {}".format(dest_path))
		pathsMovedSucc.append(srcPath)
		distutils.dir_util.copy_tree(srcPath,dest_path)
	else:
		print("COPYPASTE_FAIL: {}".format(srcPath))
		quit()

else:
	print(" *\* CopyPaste or Overwrite Files */* ")
	print()

	for path in pathsToMove:

		file_path = os.path.join(srcPath, path)
		dest_path = os.path.join(destPath, path)

		if os.path.exists(os.path.join(srcPath,path)) is True:
			print("COPYPASTE_SUCCESS: {}".format(dest_path))
			print()
			pathsMovedSucc.append(path)
			shutil.copy(file_path,dest_path)

		else:
			print("COPYPASTE_FAIL: {}".format(path))
			print()
			paths_not_found.append(path)
