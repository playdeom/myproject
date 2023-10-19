import functions.data_load as dl
import functions.log as fl
import os
up=os.getcwd()
def sign_in(player_id, player_password):
    check_correct=0
    check_line=0
    pcnt=0
    icnt=0
    with open(f"{up}/project/player/player_id.txt", 'r', encoding='utf-8')as id:
        id.seek(0)
        id_line=id.readlines()
        while(icnt!=len(id_line)):
            if(player_id+'\n'==id_line[icnt]):
                check_correct+=1
                break
            else:
                icnt+=1
    with open(f"{up}/project/player/player_password.txt", 'r', encoding='utf-8')as password:
        password.seek(0)
        password_line=password.readlines()
        while(pcnt!=len(password_line)):
            if(player_password+'\n'==password_line[pcnt]):
                check_correct+=1
                break
            else:
                pcnt+=1
    if(check_correct==2):
        if(icnt==pcnt):
            check_line=1
            print("확인되었습니다")
            print("로그인되었습니다")
            dl.data_load(player_id)
        else:
            print("잘못된 아이디 또는 비밀번호를 잘못 입력했습니다")
    else:
        print("잘못된 아이디 또는 비밀번호를 잘못 입력했습니다")
    fl.log_in(check_correct, check_line, player_id, player_password)
        
