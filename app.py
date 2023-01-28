from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
load_dotenv()
MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='abbas'
app.config['MYSQL_PASSWORD']=MYSQL_PASSWORD
app.config['MYSQL_DB']='flaskapp'

mysql=MySQL(app)


# def first():
#     return render_template('index.html')

@app.route('/show',methods=['POST'])
def second():
    if request.method == 'POST':
        name=str(request.form['fullname'])
        cursor=mysql.connection.cursor()
        print(name)
    
        cursor.execute('''select * from report where name=%s''',[name])
        data=cursor.fetchall()
        print(data)
        mysql.connection.commit()
        cursor.close()
        return render_template('show.html',employees=data)

    

@app.route('/edit')
def read():
    
    cursor=mysql.connection.cursor()
    
    
    cursor.execute('''select * from report ''')
    data=cursor.fetchall()
    print(data)
    mysql.connection.commit()
    cursor.close()
    return render_template('show.html',employees=data)

@app.route('/delete/<string:name>')
def delete(name):
    fullname=str(name)
    print(fullname)
    cursor=mysql.connection.cursor()
    cursor.execute('''delete from report where name=%s''',[fullname])
    mysql.connection.commit()
    cursor.close()
    return redirect('/edit')
    
@app.route('/')
@app.route('/done',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        cursor=mysql.connection.cursor()
        name=str(request.form['fullname'])
        email=str(request.form['email'])
        contact=str(request.form['contact'])
        message=str(request.form['message'])
        cursor.execute('''insert into report values(%s,%s,%s,%s)''',(name,email,contact,message))
        mysql.connection.commit()
        cursor.close()
        return render_template('index.html')
    else:
        return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True)
