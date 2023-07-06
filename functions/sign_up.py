import functions.log as fl
def sign_up(player_id, player_password):
    check_log=0
    id=open("C:/project/player/player_id.txt", 'r+', encoding='utf-8')
    password=open("C:/project/player/player_password.txt", 'r+', encoding='utf-8')
    cnt=0
    check=0
    id.seek(0)
    Ilines=id.readlines()
    while(cnt!=len(Ilines)):
        if(player_id+'\n'==Ilines[cnt]):
            print("이미 사용된 이름입니다.")
            check+=1
            break
        else:
            cnt+=1
    if(check==1):
        pass
    else:
        check_log+=1
        print("아이디가 확인되었습니다.")  
    cnt=0
    check=0
    password.seek(0)
    Plines=password.readlines()
    while(cnt!=len(Plines)):
        if(player_password+'\n'==Plines[cnt]):
            print("이미 사용된 비밀번호 입니다.")
            check+=1
            break
        else:
            cnt+=1
    if(check==1):
        pass
    else:
        check_log+=1
        print("비밀번호가 확인되었습니다")
    if(check_log==2):
        id.write(f"{player_id}\n")
        password.write(f"{player_password}\n")
    id.close()
    password.close()
    fl.log_up(check_log, player_id, player_password)