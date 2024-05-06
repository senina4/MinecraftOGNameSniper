import requests
import json
import time
import sys
from colorama import Fore, just_fix_windows_console

# Call just_fix_windows_console to fix console on Windows
just_fix_windows_console()

class MinecraftAPI():
    def get_profile_information(self, bearer_token):
        """
        Get profile information of the user.
        
        Args:
            bearer_token (str): The bearer token for authentication.
            
        Returns:
            dict: Profile information.
        """
        response = requests.get(url="https://api.minecraftservices.com/minecraft/profile", 
                                headers={
                                    "Authorization": f"Bearer {bearer_token}"
                                })
        if response.status_code == 200:
            return json.loads(response.text)
        elif response.status_code == 401:
            raise Exception(f"{Fore.RED}Unauthorized: Bearer token expired or is not correct.")
        elif response.status_code == 500:
            print(f"{Fore.RED}Timed out: API lagged out and could not respond.")
        else:
            raise Exception(f"{Fore.RED}Something went wrong: {response.status_code}")
        
    def change_username(self, bearer_token, new_username):
        """
        Change the username of the user.
        
        Args:
            bearer_token (str): The bearer token for authentication.
            new_username (str): The new username to be set.
        """
        response = requests.put(f"https://api.minecraftservices.com/minecraft/profile/name/{new_username}", 
                                headers={
                                    "Authorization": f"Bearer {bearer_token}",
                                    "Content-Type": "application/json"
                                })
            
        if response.status_code == 200:
            print(f"{Fore.GREEN}Username changed successfully!")
            time.sleep(1)
            # Check if username change was successful
            if MinecraftAPI().get_profile_information(bearer_token=bearer_token)["name"] == new_username:
                sys.exit(f"{Fore.GREEN}Username changed successfully! {time.strftime('%X')}")
        elif response.status_code == 400:
            raise Exception(f"{Fore.RED}Name is invalid, longer than 16 characters, or contains invalid characters.")
        elif response.status_code == 403:
            print(f"{Fore.RED}Name is unavailable: Either taken or has not become available.")
            time.sleep(10)
        elif response.status_code == 401:
            raise Exception(f"{Fore.RED}Unauthorized: Bearer token expired or is not correct.")
        elif response.status_code == 429:
            print(f"{Fore.RED}Too many requests.")
            time.sleep(3)
        elif response.status_code == 500:
            print(f"{Fore.RED}Timed out: API lagged out and could not respond.")

def main():
    # Get bearer token from user
    bearer_token = input("Please enter your bearer token: ")
    # Fetch profile information
    profile = MinecraftAPI().get_profile_information(bearer_token=bearer_token)
    # Display profile information
    print(f"{Fore.YELLOW}Username: {profile['name']}")
    print(f"UUID: {profile['id']}")
    print(f"{Fore.RED}Warning: Limitations You can only change your username once every 30 days. A username must be between 3 and 16 characters and cannot contain invalid characters.")
    # Get new username from user
    new_username = input(f"{Fore.RESET}Enter the new name you want: ")
    while True:
        # Attempt to change username
        MinecraftAPI().change_username(bearer_token=bearer_token, new_username=new_username)

if __name__ == "__main__":
    main()
