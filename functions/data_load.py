import functions.log as fl
def data_load(player_id):
    with open(f"C:/project/player/player_data/{player_id}.txt", 'a+', encoding='utf-8')as dl:
        while(True):
            dl.seek(0)
            DlLine=dl.readlines()
            if not DlLine:
                print("data_value: None")
            else:
                print(f"data_value: {DlLine[-1].strip()}")
            data=input("데이터를 수정하시려면 q/ 나가시려면 w: ")
            if(data=='q'):
                data_value=input("데이터를 입력해주세요: ")
                check=input("정말로 데이터를 수정하시겠습니까? y/n: ")
                if(check=='y'):
                    dl.write(f"{data_value}\n")
                    fl.data(data_value,player_id)
                elif(check=='n'):
                    print('취소되었습니다')
                else:
                    print('다시 시도해주세요')
            elif(data=='w'):
                break