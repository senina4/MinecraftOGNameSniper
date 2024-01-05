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


    try:
        print(msg("系統", "檢查網路中"))
        response = requests.get("https://api.mojang.com", timeout=5)
    except requests.ConnectionError:
        print(msg("系統", "尚未連接網路"))
        time.sleep(5)
        exit()
    bearer_token = input(msg("登入", "請輸入 bearer token(你可以在'https://senina4.github.io/OGName/'找到如何獲取bearer token): "))
    try:
        client = cl(bearer_token=bearer_token)
    except mojang.errors.Unauthorized:
        print(msg("系統", "無權存取所要求的資源。發生這種情況的原因可能是承載令牌無效或過期。"))
        time.sleep(5)
        exit()
    except mojang.errors.LoginFailure:
        print(msg("系統", "登入過程因某種原因失敗。這可能是由於電子郵件或密碼不正確而導致的。"))
        time.sleep(5)
        exit()
    except mojang.errors.MissingMinecraftLicense:
        print(msg("系統", "Microsoft 帳戶有效，但缺少 Minecraft 授權。"))
        time.sleep(5)
        exit()
    except mojang.errors.MissingMinecraftProfile:
        print(msg("系統", "該帳戶擁有 Minecraft 許可證，但尚未建立個人資料。"))
        time.sleep(5)
        exit()
    newname = input(msg("系統", "輸入你想要的新名稱: "))
    if client.is_username_available(newname) == True:
        print(msg("系統", "新名子無法使用，無法切換名稱"))
        time.sleep(5)
        exit()
    api = mcapi()
    if client.get_name_change_info().find("True") != 4:
        print(msg("系統", "帳號無法使用，無法切換名稱"))
        time.sleep(5)
        exit()
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
