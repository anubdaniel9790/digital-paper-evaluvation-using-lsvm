import os
import shutil
from datetime import date
from urllib import request
import imagehash as imagehash
from PIL import Image
from werkzeug.utils import redirect, secure_filename
import camera
import pymysql
from flask import Flask, render_template, flash, request, session, Response, url_for, send_from_directory, current_app,send_file


conn = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin_login")
def admin1():
    return render_template('admin.html')

#####################################################################################################################3
#################################################################################################################3
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':
            return render_template('admin_home.html',error=error)
        else:
            return render_template('admin.html', error=error)
@app.route("/admin_home")
def adminhome():
    return render_template('admin_home.html')

@app.route("/add_student",methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        roolno = request.form['roolno']
        studentname = request.form['studentname']
        class1 = request.form['class1']
        section = request.form['section']
        fathername = request.form['fathername']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        conn = pymysql.connect(user='root', password='', host='localhost', database='python_biometric_login')
        session['roolno'] = section
        cursor = conn.cursor()
        cursor.execute("insert into user_details values('"+roolno + "','"+studentname+"','"+class1+"','"+section+"','"+fathername+"','"+contact+"','"+email+"','"+address+"','0','0')")
        conn.commit()
        conn.close()
        #flash("Logged in successfully.")
        #return 'file uploaded successfully'
        return render_template('admin_student1.html',vid=section)
@app.route('/video_feed')
def video_feed():
    return Response(gen(camera.VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/add_face',methods=['POST','GET'])
def view_voter():
    if request.method=='POST':
        vid=request.form['vid']
        fimg=vid+".jpg"
        conn = pymysql.connect(user='root', password='', host='localhost', database='python_biometric_login')
        cursor = conn.cursor()
        cursor.execute('update user_details set report=%s WHERE name = %s', (fimg, vid))
        conn.commit()
        conn.close()
        shutil.copy('faces/f1.jpg', 'static/photo/'+fimg)
        return render_template('student.html')
@app.route("/admin_upload")
def admin_upload():
    return render_template('admin_upload.html')

@app.route('/upload_data',methods=['POST','GET'])
def upload_data():
    mycursor = conn.cursor()
    if request.method=='POST':
        name = request.form['class1']
        caption = request.form['subject']
        if 'file' not in request.files:
            flash('No file Part')
            return redirect(request.url)
        file= request.files['file']
        print(file)
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename(f.filename)))
        cursor = conn.cursor()
        today = date.today()
        rdate = today.strftime("%d-%m-%Y")
        cursor.execute("SELECT max(id)+1 FROM   question")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO question  VALUES (%s, %s, %s, %s, %s)"
        val = (maxid, name, caption, f.filename,  rdate)
        print(val)
        cursor.execute(sql,val)
        conn.commit()
    return render_template('admin_home.html')

@app.route("/student")
def student():
    return render_template('student.html')
@app.route("/student_login",methods = ['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['cont']
        cursor = conn.cursor()
        session['roolno'] = n
        cursor.execute("SELECT * from user_details where account_no='" + n + "'")
        data = cursor.fetchall()
        if data is None:
            return 'Username or Password is wrong'
        else:
            session['uname'] = request.form['uname']
            return render_template('student_face_verification.html',sid=n)
@app.route('/verify_face',methods=['POST','GET'])
def verify_face():
    msg=""
    sid=request.form['uname']
    print(sid)
    if request.method=='POST':
        try:
            shutil.copy('faces/f1.jpg', 'faces/s1.jpg')
            hash0 = imagehash.average_hash(Image.open("faces/s1.jpg"))
            hash1 = imagehash.average_hash(Image.open("static/photo/"+sid+".jpg"))
            cc1=hash0 - hash1
            print(cc1)
            if cc1<=10:
                today = date.today()
                return redirect(url_for('student_home', msg=msg))
            else:
                return redirect(url_for('student', msg=msg))
        except:
            return redirect(url_for('student', msg=msg))
    return render_template('verify_face.html',msg=msg)

@app.route("/student_home")
def student_home():
    un=session['uname']
    return render_template('student_home.html',vid=un)

@app.route("/student_question")
def student_question():
    return render_template('student_question.html')

@app.route("/search_question1",methods=['POST','GET'])
def search_question1():
    if request.method=='POST':
        name = request.form['textfield']
        name1 = request.form['textfield2']
        cur = conn.cursor()
        #cur.execute("SELECT * FROM question where class1='"+name+"' and subject='"+name1+"'")
        cur.execute("SELECT * FROM question where class1='"+name+"' and subject='"+name1+"'")
        data = cur.fetchall()
        print(data)
        return render_template('search_question_1.html', data=data)
    else:
        return student_question()

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(filename)
    uploads = os.path.join(current_app.root_path, "static/uploads/")
    print(uploads)
    f=filename
    return send_from_directory(directory=uploads, filename=filename,as_attachment=True)

@app.route("/student_attendance", methods=['GET', 'POST'])
def student_attendance():
    n= session['roolno']
    print(n)
    cur = conn.cursor()
    cur.execute ("SELECT id,sid,rdate,month FROM attendance where sid='"+n+"'")
    return render_template('student_attendance.html',items=cur.fetchall())
@app.route("/admin_attendance")
def admin_attendance():
    cur = conn.cursor()
    cur.execute ("SELECT id,sid,rdate,month FROM attendance")
    return render_template('admin_attendance.html',items=cur.fetchall())

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
