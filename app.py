from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='abbas'
app.config['MYSQL_PASSWORD']='AB11**as'
app.config['MYSQL_DB']='flaskapp'

mysql=MySQL(app)

@app.route('/')
def first():
    return render_template('index.html')


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
    


if __name__ == '__main__':
    app.run(debug=True)
