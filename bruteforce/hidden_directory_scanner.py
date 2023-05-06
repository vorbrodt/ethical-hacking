import requests

target_url = input("[+] Enter Target URL: ")
file_name = input("[+] Enter Name Of The File Containing Directories: ")

def requests(url):
  try:
    return requests.get("http://" + url)
  except requests.exceptions.ConnectionError:
    pass

f = open(file_name, "r")
for line in f:
  directory = line.strip();
  full_url = target_url + "/" + directory
  response = requests(full_url)
  if response:
    print("[*] Discovered Directory At Path: " + full_urls)