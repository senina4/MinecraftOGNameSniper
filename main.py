try:
    from mojang import API as mcapi
    from mojang import Client as cl
    import mojang
    import requests
    import sys
    import time
    from colorama import Fore, Back, just_fix_windows_console
    just_fix_windows_console()
    from datetime import datetime
    
    def msg(tittle, submsg):
        return f"{Fore.CYAN}{Back.RESET}{datetime.now().hour}-{datetime.now().minute}-{datetime.now().second} {Fore.BLUE}{tittle}{Fore.RESET}: {Fore.GREEN}{submsg}{Fore.RESET}"
        
    bearer_token = input(msg("登入", "請輸入 bearer token(你可以在'https://senina4.github.io/OGName/'找到如何獲取bearer token): "))
    client = cl(bearer_token=bearer_token)
    newname = input(msg("系統", "輸入你想要的新名稱: ")
    api = mcapi()
    uuid = api.get_uuid(client.get_profile().name)
    times = 0
    while True:
        if api.get_uuid(uuid) == newname:
            print(msg("系統", "成功"))
            time.sleep(5)
            exit()
        time.sleep(5)
        times += 1
        print(msg("系統", times))
        client.change_username(newname)
     
except KeyboardInterrupt:
    print(msg("\n系統", "已結束程式"))
except Exception as ex:
    print(msg("系統", f"發生錯誤, 錯誤代碼: {ex}"))
