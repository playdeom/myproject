import datetime
import os
up=os.getcwd()
print(up)
def log_up(check, player_id, player_password):
    with open(f"{up}/project/player/log.txt", 'r+', encoding='utf-8')as log:
        log.seek(0,2)
        date=datetime.datetime.now()
        if(check==2):
            log.write(f"[{date}]{player_id} is sign up using {player_password}\n")
            print("회원가입이 되었습니다.")
        else:
            log.write(f"[{date}]{player_id} try to sign up using {player_password}\n")
            print("회원가입을 다시 시도해주세요")
def log_in(check, line, player_id, player_password):
    with open(f"{up}/project/player/log.txt", 'a+', encoding='utf-8')as log:
        log.seek(0,2)
        if(check==2):
            if(line==1):
                date=datetime.datetime.now()
                log.write(f"[{date}]{player_id} is sign in using {player_password}\n")
            else:
                date=datetime.datetime.now()
                log.write(f"[{date}]{player_id} try to sign in using {player_password}\n")
        else:
            date=datetime.datetime.now()
            log.write(f"[{date}]{player_id} try to sign in using {player_password}\n")
def data(data, player_id):
    with open(f"{up}/project/player/log.txt", 'a+', encoding='utf-8')as log:
        date=datetime.datetime.now()
        log.seek(0,2)
        log.write(f"[{date}]{player_id} change the data_value to {data}\n")