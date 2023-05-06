<strong>IMPORTANT:</strong> Note that this script is for educational purposes only and should not be used for any illegal or unauthorized activities.

# Socket Port Scanner

A Python script that allows you to scan for open ports on one or multiple IP addresses using the socket library.

## Usage

---

To use this script, simply run the `scan.py` file with Python 3.x. You will be prompted to enter the targets you wish to scan and the number of ports you want to scan. If you wish to scan multiple targets, separate them with commas.

The script will then scan the specified number of ports for each target and print out any open ports it finds.

## Example of test run

---

```
$ python scan.py
[*] Enter targets to scan: 192.168.1.1, 192.168.1.5
[*] Enter number of ports to scan: 1000
[*] Scanning multiple targets

Starting scan for 192.168.1.1
[+]Port Opened 22
[+]Port Opened 80
[+]Port Opened 443

Starting scan for 192.168.1.5
[+]Port Opened 22
[+]Port Opened 80
```
