import os
import re
import shutil
from datetime import date
from urllib import request
import imagehash as imagehash
from PIL import Image
from werkzeug.utils import redirect, secure_filename
import camera
import camera1
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
@app.route("/admin_add_student")
def admin_add_student():
    return render_template('admin_add_student.html')

@app.route("/admin_add_student1", methods=['GET', 'POST'])
def admin_add_student1():
    if request.method == 'POST':
        register_no = request.form['register_no']
        name = request.form['name']
        degree = request.form['degree']
        department = request.form['department']
        dob = request.form['dob']
        password = request.form['password']
        gender=request.form['gender']

        conn = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')

        cursor = conn.cursor()
        cursor.execute("insert into student_details values('"+str(register_no) + "','"+str(name)+"','"+str(degree)+"','"+str(department)+"','"+str(dob)+"','"+str(password)+"','"+str(gender)+"','0','0')")
        conn.commit()
        conn.close()
        #flash(f"You just changed your name to: {session['name']}")
        flash(f"Record Saved!", "success")
        return render_template('admin_add_student1.html', vid=register_no)

@app.route('/video_feed')
def video_feed():
    return Response(gen(camera.VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/add_face', methods=['POST', 'GET'])
def view_voter():
    if request.method == 'POST':
        vid = request.form['register_no']
        fimg = vid + ".jpg"
        shutil.copy('faces/f1.jpg', 'static/photo/' + fimg)
        return render_template('admin_add_student.html')
    #return render_template('admin_add_student.html')
@app.route("/admin_add_staff")
def admin_add_staff():
    return render_template('admin_add_staff.html')
@app.route("/admin_add_staff1", methods=['GET', 'POST'])
def admin_add_staff1():
    if request.method == 'POST':
        staff_name = request.form['staff_name']
        department = request.form['department']
        qualification = request.form['qualification']
        gender = request.form['gender']
        designation = request.form['designation']
        email = request.form['email']
        username=request.form['username']
        password = request.form['password']

        conn = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')

        cursor = conn.cursor()
        cursor.execute("insert into staff_details values('"+str(staff_name) + "','"+str(department)+"','"+str(qualification)+"','"+str(gender)+"','"+str(designation)+"','"+str(email)+"','"+str(username)+"','"+str(password)+"','0','0')")
        conn.commit()
        conn.close()
        return render_template('admin_add_staff.html', flash_message=True,data="Staff Added Successfully")


@app.route("/staff")
def staff():
    return render_template('staff.html')

@app.route("/staff_login",methods = ['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['password']
        cursor = conn.cursor()
        session['staff'] = n
        cursor.execute("SELECT * from staff_details where username='" + str(n) + "' and password='"+str(g)+"'")
        data = cursor.fetchall()
        check=len(data)
        if check==0:
            return render_template('staff.html', flash_message=True,data="Login Failed")
        else:
            session['uname'] = request.form['uname']
            return render_template('staff_home.html',sid=n)
@app.route("/staff_home")
def staff_home():
    return render_template('staff_home.html')
@app.route("/staff_add_question")
def staff_add_question():
    session['qid'] = 1
    return render_template('staff_add_question.html')
@app.route("/staff_add_question1", methods=['GET', 'POST'])
def staff_add_question1():
    if request.method == 'POST':
        qid=session['qid']
        staff=session['uname']
        degree = request.form['degree']
        department = request.form['department']
        year = request.form['year']
        semester = request.form['semester']
        subject_code = request.form['subject_code']
        subject_name = request.form['subject_name']
        paper_code=request.form['paper_code']
        no_of_qustions = request.form['no_of_qustions']
        mark_per_question = request.form['mark_per_question']
        total_marks = request.form['total_marks']

        session['qid'] = qid
        session['staff'] = staff
        session['degree'] = degree
        session['department'] = department
        session['year'] = year
        session['semester'] = semester
        session['subject_code'] = subject_code
        session['subject_name'] = subject_name
        session['paper_code'] = paper_code
        session['no_of_qustions'] = no_of_qustions
        session['mark_per_question'] = mark_per_question
        session['total_marks'] = total_marks
        return render_template('staff_add_question1.html',qid=qid)

@app.route("/staff_add_question2", methods=['GET', 'POST'])
def staff_add_question2():
    if request.method == 'POST':
        qid=session['qid']
        staff=session['uname']
        degree = session['degree']
        department = session['department']
        year = session['year']
        semester = session['semester']
        subject_code = session['subject_code']
        subject_name = session['subject_name']
        paper_code=session['paper_code']
        no_of_qustions = session['no_of_qustions']
        mark_per_question = session['mark_per_question']
        total_marks = session['total_marks']

        question = request.form['question']
        keypoint = request.form['keypoint']
        conn = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')
        cursor = conn.cursor()
        cursor.execute("Select max(id)+1 From question_details")
        maxid = cursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        sql1 = "insert into question_details values('" + str(
            maxid) + "','" + str(staff) + "','" + str(degree) + "','" + str(department) + "','" + str(year) + "','" + \
              str(semester) + "','" + str(subject_code) + "','" + str(subject_name) + "','" + str(paper_code) + "','" \
              + str(no_of_qustions) + "','" + str(mark_per_question) + "','" + str(total_marks) + "','" + str(qid ) + "','" + \
              str(question) + "','" + str(keypoint) + "','-','0','0')"
        conn1 = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')
        cursor1 = conn1.cursor()
        cursor1.execute(sql1)
        conn1.commit()
        tmp=int(qid)
        a=int(no_of_qustions)
        if tmp>=a:
            return render_template('staff_home.html')
        else:
            tmp=tmp+1
            session['qid']=str(tmp)
            return render_template('staff_add_question1.html', qid=qid)
@app.route("/staff_student_Details")
def staff_student_Details():
    cur = conn.cursor()
    cur.execute("SELECT register_no,name,degree,department,dob,gender FROM student_details")
    data = cur.fetchall()
    print(data)
    return render_template('staff_student_Details.html',items=data)

@app.route("/student")
def student():
    return render_template('student.html')

@app.route("/student_login",methods = ['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['password']
        hh = "reg.txt"
        f = open(hh, "w")
        f.write(n)

        hh1 = n+".txt"
        f = open(hh1, "w")
        f.write("Normal")


        cursor = conn.cursor()
        session['student'] = n
        cursor.execute("SELECT * from student_details where register_no='" + str(n) + "' and password='"+str(g)+"'")
        data = cursor.fetchall()
        check=len(data)
        if check==0:
            return render_template('student.html', flash_message=True,data="Login Failed")
        else:
            session['register_no'] = request.form['uname']
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
    return render_template('student_home.html')
@app.route("/student_exam")
def student_exam():
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT degree,department,year,semester,subject_code,subject_name from question_details")
    data = cursor.fetchall()
    degree=[]
    department=[]
    year=[]
    semester=[]
    subject_code=[]
    subject_name=[]
    for a in data:
        degree.append(a[0])
        department.append(a[1])
        year.append(a[2])
        semester.append(a[3])
        subject_code.append(a[4])
        subject_name.append(a[5])
    return render_template('student_exam.html',degree=degree,department=department,year=year,semester=semester,subject_code=subject_code,subject_name=subject_name)

@app.route("/student_exam1",methods = ['GET', 'POST'])
def student_exam1():
    if request.method == 'POST':
        degree = request.form['degree']
        department = request.form['department']
        year = request.form['year']
        semester = request.form['semester']
        subject_name = request.form['subject_name']
        subject_code=request.form['subject_code']

        session['degree'] = degree
        session['department'] = department
        session['year'] = year
        session['semester'] = semester
        session['subject_name'] = subject_name
        session['subject_code'] = subject_code
        session['qid'] = 1
        session['total_mark'] = 0
        student = session['student']
        qq="select * from student_exam_details where subject_code='"+str(subject_code)+"' and student='"+str(student)+"'"
        cursor = conn.cursor()
        cursor.execute(qq)
        data = cursor.fetchall()
        res=[]
        for a in data:
            res.append(a[0])
        dd=(len(res))
        if dd==0:
            return student_exam2()
        else:
            return render_template('student_home.html', flash_message=True,data="Alredy Finished")


@app.route("/student_exam2",methods = ['GET', 'POST'])
def student_exam2():
    if request.method == 'POST':
        degree=session['degree']
        department=session['department']
        year=session['year']
        semester=session['semester']
        subject_name=session['subject_name']
        subject_code=session['subject_code']
        qid=session['qid']


        cursor = conn.cursor()
        cursor.execute("SELECT question from question_details where subject_code='"+str(subject_code)+"' and qid='"+str(qid)+"'")
        data = cursor.fetchone()
        return render_template('student_exam1.html',qid=qid,degree=degree,department=department,year=year,semester=semester,subject_name=subject_name,subject_code=subject_code,data=data)


@app.route("/student_exam3",methods = ['GET', 'POST'])
def student_exam3():
    if request.method == 'POST':
        enter_answer = request.form['answer']
        qid = session['qid']
        student = session['student']
        subject_code = session['subject_code']
        cursor = conn.cursor()
        qq="SELECT keypoint from question_details where subject_code='" + str(subject_code) + "' and qid='" + str(qid) + "'"
        cursor.execute(qq)
        data = cursor.fetchone()
        original_answer=str((data[0]))
        original_answer=str(original_answer).lower()

        mark=0
        original_answer_wordList = re.sub("[^\w]", " ", original_answer).split()
        key_point_length=len(original_answer_wordList)

        enter_answer=enter_answer.lower()
        wordList = re.sub("[^\w]", " ", enter_answer).split()
        wordList_length = len(wordList)

        for x in wordList:
            if x in original_answer:
                mark=mark+1

        result_mark=int((mark/key_point_length)*5)
        total_mark=int(session['total_mark'])
        total_mark=total_mark+result_mark

        session['total_mark']=total_mark
        print(total_mark,result_mark)

        t_qid = int(qid) + 1
        session['qid'] = str(t_qid)


        if(t_qid>10):
            print(student)
            f=open(student+".txt","r")
            predict=f.read()
            cursor.execute("Select max(id)+1 From student_exam_details")
            maxid = cursor.fetchone()[0]
            if maxid is None:
                maxid = 1
            sql1 = "insert into student_exam_details values('" + str(maxid) + "','" + str(subject_code) + "','" + str(student) + "','" + str(total_mark) + "','"+str(predict)+"','0')"
            conn1 = pymysql.connect(user='root', password='', host='localhost', database='python_digital_ai_exam')
            cursor1 = conn1.cursor()
            cursor1.execute(sql1)
            conn1.commit()
            return student_home()
        else:
            return student_exam2()

@app.route('/video_feed1')
def video_feed1():
    return Response(gen1(camera1.VideoCamera1()),mimetype='multipart/x-mixed-replace; boundary=frame')




@app.route("/student_result")
def student_result():
    register_no = session['register_no']
    print(register_no)
    qq = "select id,subject_code,student,total_mark,status from student_exam_details where student='" + str(register_no) + "'"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('student_result.html',items=data)

def gen1(camera1):
    while True:
        #get camera frame
        frame1 = camera1.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')




@app.route("/staff_marked_students")
def staff_marked_students():
    qq = "select id,subject_code,student,total_mark,status from student_exam_details where status='Marked'"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('staff_marked_students.html',items=data)

@app.route("/staff_student_result")
def staff_student_result():
    qq = "select id,subject_code,student,total_mark from student_exam_details where status='Normal'"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('staff_student_result.html',items=data)


@app.route("/admin_exam_result")
def admin_exam_result():
    qq = "select id,subject_code,student,total_mark from student_exam_details where status='Normal'"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('admin_exam_result.html',items=data)


@app.route("/admin_question")
def admin_question():
    qq = "select degree,department,year,semester,subject_code,subject_name,paper_code,qid,question,keypoint	 from question_details"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('admin_question.html',items=data)


@app.route("/admin_marked_student")
def admin_marked_student():
    qq = "select id,subject_code,student,total_mark,status from student_exam_details where status='Marked'"
    cursor = conn.cursor()
    cursor.execute(qq)
    data = cursor.fetchall()
    return render_template('admin_marked_student.html',items=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)