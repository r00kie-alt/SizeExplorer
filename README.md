#SizeExplorer

Size Explorer is a Python script that analyzes the sizes of subfolders within a parent folder. 
It provides insights into the disk space occupied by each subfolder, helping you identify which subfolders are taking up the most space.

## Features

- Calculates the size of each subfolder within a parent folder
- Supports size units: bytes, kilobytes, megabytes, gigabytes, terabytes
- Sorts the subfolders by size in ascending or descending order
- Recursive calculation to determine the total size of subfolders within folders
- User-friendly command-line interface

## Usage
1.Run the script
2.Follow the prompts
	2.1 Enter the path of the parent folder
	2.2 Select the unit you wish the size to be displayed as
	2.3 Select the sort order
3.Read the output!

## Example Usage

Enter the parent directory path: /path/to/parent/folder
Choose the size unit:
1. Bytes
2. Kilobytes
3. Megabytes
4. Gigabytes
5. Terabytes
Enter your choice: 3
Enter the sort order (asc for ascending, desc for descending): desc

## Example Output

Subfolder1: 52.30 MB
Subfolder2: 38.75 MB
Subfolder3: 21.45 MB
...
