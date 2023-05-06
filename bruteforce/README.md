<strong>IMPORTANT:</strong> Note that this script is for educational purposes only and should not be used for any illegal or unauthorized activities.

# Brute force login credentials

A Python script for password cracking using a brute force attack. The script takes input parameters such as the target URL, the username for the account to crack, the name of the password file, and other relevant details.

The script performs the attack by iterating through a list of passwords in the password file, and attempting to log in to the target account with each password. If the login is successful, the script prints the username and password and exits. If none of the passwords match, the script prints a message indicating that no match was found.

## Example of test run

---

```
HH   HH   OOOO   BBBB   BBBB   YY   YY
HH   HH  OO  OO  BB  B  BB  B   YY YY
HHHHHHH  OO  OO  BBBB   BBBB     YYY
HH   HH  OO  OO  BB  B  BB  B    YYY
HH   HH   OOOO   BBBB   BBBB     YYY

HH   HH   AAAA   CCCCC  KK  KK  SSSSS
HH   HH  AA  AA  CC     KK KK   SS
HHHHHHH AAAAAAA  CC     KKK     SSSSS
HH   HH AA   AA  CC     KK KK      SS
HH   HH AA   AA  CCCCC  KK  KK  SSSSS

[+] Enter URL: https://www.example.com
[+] Enter Username For Account To Bruteforce: admin
[+] Enter Password File To Use: passwords.txt
[+] Enter String That Occurs When Login Fails: Login failed
[+] Enter The Request Type (GET/POST): POST
[+] Enter name of username field: username
[+] Enter name of password field: password
[+] Enter name of submit button: Login
[+] Enter Cookie Value If Within Session (Optional):

[+] Found Username: admin
[+] Found Password: letmein
```
