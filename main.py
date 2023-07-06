import datetime
import functions.sign_up as su
import functions.sign_in as si
date=datetime.datetime.now()
player_id=0
player_password=0
check=True
while(check):
    ask=input("로그인을 하려면 y/ 회원가입을 하려면 x/ 종료하려면 z: ")
    if(ask=='y'):
        player_id=input("아이디를 입력하세요: ")
        player_password=input("비밀번호를 입력하세요: ")
        si.sign_in(player_id, player_password)
    elif(ask=='x'):
        player_id=input("아이디를 입력하세요: ")
        player_password=input("비밀번호를 입력하세요: ")
        su.sign_up(player_id, player_password)
    elif(ask=='z'):
        break
    else:
        print("다시 시도하세요")
    