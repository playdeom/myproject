import functions.log as fl
import os
up=os.getcwd()
def data_load(player_id):
    DlLine=None
    with open(f"{up}/project/player/player_data/{player_id}.txt", 'r+', encoding='utf-8')as dl:
        dl.seek(0)
        DlLine=dl.readlines()
    with open(f"{up}/project/player/player_data/{player_id}.txt", 'w+', encoding='utf-8')as dl:
        while(True):
            if not DlLine:
                print("data_value: None")
            else:
                print(f"data_value: ")
                for i in DlLine:
                    print(i[0:len(i)-1], end=' ')
                print()
            data=input("데이터를 수정하시려면 q/ 추가하시려면 n/ 나가시려면 w: ")
            if(data=='q'):
                if(len(DlLine)==0):
                    print("수정할 수 있는 정보가 없습니다 n을 눌러 데이터를 추가하세요.")
                    continue
                data_value=input("데이터를 입력해주세요: ")
                while 1:
                    data_index=int(input("몇 번째 데이터를 수정하시겠습니까? 1~:"))
                    if data_index-1>=len(DlLine):
                        print("잘못된 범위입니다")
                    else:
                        break
                check=input("정말로 데이터를 수정하시겠습니까? y/n: ")
                if(check=='y'):
                    DlLine[data_index-1]=data_value+'\n'
                    fl.data(data_value,player_id)
                elif(check=='n'):
                    print('취소되었습니다')
                else:
                    print('다시 시도해주세요')
            elif(data=='w'):
                for i in DlLine:
                    dl.write(i)
                break
            elif(data=='n'):
                data_value=input("데이터를 입력해주세요: ")
                check=input("정말로 데이터를 추가하시겠습니까? y/n: ")
                if check=='y':
                    DlLine.append(data_value+'\n')
                    fl.data(data_value,player_id)
                elif check=='n':
                    print('취소되었습니다')
                else:
                    print('다시 시도해주세요')


