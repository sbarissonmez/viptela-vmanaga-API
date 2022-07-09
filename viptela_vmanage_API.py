import requests
import sys

requests.packages.urllib3.disable_warnings()

ur = input("Enter the path to Vmanage :")
name = input("Please enter your user name:")
passw = input("Please enter your password:")

def my_login():
  login_url = '%s/j_security_check' % ur
  login_credentials = {'j_username': name, 'j_password': passw}
  session = requests.session()
  response = session.post(url = login_url, data = login_credentials, verify=False)
  if b'<html>' in response.content:
    print(f"Login Failed, {response.status_code}")
    exit(0)
  else:
    print(f"Login Success, {response.status_code}")

my_login()
