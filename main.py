import requests
import json
import time
import sys
from colorama import just_fix_windows_console, Fore, Back, Style

class API():
    def get_profile_information(self, bearer_token):
        response = requests.get(url="https://api.minecraftservices.com/minecraft/profile", 
                                headers={
                                            "Authorization": "Bearer %s" %bearer_token
                                })
        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code== 401:
            raise Exception("Unauthorized (Bearer token expired or is not correct).")
        elif response.status_code == 500:
            print("Timed out (API lagged out and could not respond).")
        else:
            raise Exception("something went wrong: %s" % response.status_code)
        
    def change_username(self, bearer_token, new_username):
        response = requests.put("https://api.minecraftservices.com/minecraft/profile/name/%s" %new_username, 
                                headers={
                                    "Authorization": "Bearer %s" %bearer_token,
                                    "Content-Type": "application/json"
                                })
            
        if response.status_code == 200:
            print("Username changed successfully!")
            time.sleep(1)
            if API().get_profile_information(bearer_token=bearer_token)["name"] == new_username:
                sys.exit("Username changed successfully!" + time.strftime("%X"))
        elif response.status_code == 400:
            raise Exception("Name is invalid, longer than 16 characters or contains characters other than (a-zA-Z0-9_)." + time.strftime("%X"))
        elif response.status_code == 403:
            print("Name is unavailable (Either taken or has not become available)." + time.strftime("%X"))
            time.sleep(10)
        elif response.status_code == 401:
            raise Exception("Unauthorized (Bearer token expired or is not correct)." + time.strftime("%X"))
        elif response.status_code == 429:
            print("Too many requests." + time.strftime("%X"))
            time.sleep(3)
        elif response.status_code == 500:
            print("Timed out (API lagged out and could not respond)." + time.strftime("%X"))

def main():
    just_fix_windows_console()
    bearer_token = input("Please enter your bearer token: ")
    profile = API().get_profile_information(bearer_token=bearer_token)
    print("Username: %s" % profile["name"])
    print("UUID: %s" % profile["id"])
    print(Fore.RED + """Warning: Limitations You can only change your username once every 30 days. A username must be between 3 and 16 characters and cannot contain invalid characters.""")
    new_username = input(Fore.RESET + "Enter the new name you want: ")
    while True:
        API().change_username(bearer_token=bearer_token, new_username=new_username)

if __name__ == "__main__":
    main()