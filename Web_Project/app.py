import sqlite3
from flask import Flask, url_for, render_template, request, jsonify

app = Flask(__name__)

conn = sqlite3.connect('commands.db', check_same_thread=False)
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# s : 커맨드 요청
# Flask route 정의
@app.route('/s')
def web_requests():
    command = request.args.get('c')  # 'ping' 등의 명령을 추출
    ips = request.args.get('ip')  # '192.168.0.14;192.168.0.13' 형식의 IP 주소들을 추출
    ip_list = ips.split(';')  # ';'을 기준으로 IP 주소들을 리스트로 분리

    # 데이터베이스에 명령 저장
    #insert_command_sql = 'UPDATE commands (command, ip_addresses) VALUES (?, ?);'

    #cursor.execute(insert_command_sql, (command, ips))
    conn.commit()

    return jsonify({'message': 'Command received and stored successfully'})


# r : 클라이언트 요청
# d : 드로퍼 요청


if __name__ == '__main__':
    app.run()