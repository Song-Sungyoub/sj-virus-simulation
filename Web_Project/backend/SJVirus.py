from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def html():
    con = sqlite3.connect('zombie.db')
    c = con.cursor()

    for row in c.execute('SELECT * FROM info_list'):
        data = row

    con.close()

    return render_template("SJVirus.html", data = data)

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        data = request.args.to_dict()
        return render_template('SJVirus.html', data = data)
    
    else:
        data = request.form
        return render_template('SJVirus.html', data = data)
    
if __name__ == '__main__':
    app.run