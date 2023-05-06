<strong>IMPORTANT:</strong> Note that this script is for educational purposes only and should not be used for any illegal or unauthorized activities.

# Hidden directory

This repository contains a Python script that performs a brute-force search for directories on a specified website.

## Usage

---

To use this script, simply run the directory_brute_forcer.py file with Python 3.x. You will be prompted to enter the target URL and the name of the file containing the directories you want to search for.

The script will then search for directories on the target URL by appending each directory in the specified file to the target URL. If a directory is found, the script will print out the full URL of the discovered directory.

## Example of test run

---

```
$ python directory_brute_forcer.py
[+] Enter Target URL: https://example.com
[+] Enter Name Of The File Containing Directories: directories.txt

[*] Discovered Directory At Path: https://example.com/admin
[*] Discovered Directory At Path: https://example.com/css
[*] Discovered Directory At Path: https://example.com/js
```
