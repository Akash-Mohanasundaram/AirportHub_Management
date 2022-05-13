# main.py

# from tkinter.tix import Select
# from tokenize import Name
from flask import Flask, render_template, request, redirect, url_for, session
# from flask_session import Session
import mysql.connector
from datetime import timedelta
# from sqlalchemy import union
app = Flask(__name__)
app.secret_key = "top-secret"
app.permanent_session_lifetime = timedelta(days=5)


# session.permanent='True'
# session={'updated_tech_ssn':[],'updated_no_of_hours':[],'updated_date':[],'updated_score':[],'updated_max_score':[],'updated_regno':[],'permenent':'True'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def getvalue_for_username_password():
    name = request.form['uname']
    password = request.form['psw']
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    query1 = "SELECT `USERNAME`,`PASSWORD`,`ROLE` FROM `EMPLOYEE`;"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    usernames = [i[0] for i in rr]
    passwords = [i[1] for i in rr]
    roles = [i[2] for i in rr]
    dataBase.close()
    # print(usernames,passwords,roles)
    if name in usernames:
        if passwords[usernames.index(name)] == password:
            print("IN")
            role = roles[usernames.index(name)]
            # htmlp=role+".html"
            # print(htmlp)
            return redirect(url_for(role, username=name))
            # if(role=='FAA'):
            #     return redirect(url_for(role))
            # if(role=="Admin"):
            #     return redirect(url_for(role))
            # if(role=="Technician"):
            #     return redirect(url_for(role))
            # if(role=="Traffic Controller"):
            #     return redirect(url_for(role))
        else:
            return render_template("index.html", CMT="Invalid Username or Password")
    else:
        return render_template("index.html", CMT="Invalid Username or Password")


@app.route('/FAA/<username>', methods=['POST', 'GET'])
def FAA(username):
    # dict_for_approval=dict.fromkeys(['TECHNICIAN NAME', 'TEST DATE', 'NO. OF HOURS WORKED','SCORE','MAXIMUM SCORE','AIRPLANE REG.NO'])
    # # print(dict_for_approval)
    session.permanent = 'True'
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    query1 = "select * from employee where role='FAA' and username = '" + \
        str(username) + "';"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    query2 = "select ed.name as technicain_name,t.date,  t.no_of_hours, t.score, tms.maximum_possible_score,  t.Reg_no,t.FAA_number from test t, test_max_score tms, employeedetails ed where t.reg_no=tms.reg_no and ed.ssn=t.ssn and t.FAA_Name =  '"
    query2 += rr[0][1]
    query2 += "' order by date desc;"
    cursorObject.execute(query2)
    rr1 = cursorObject.fetchall()
    query3 = "select union_membership_number from employeedetails where ssn = "
    # name= rr[0][0]
    query3 += rr[0][0]
    cursorObject.execute(query3)
    rr2 = cursorObject.fetchall()

    query4 = "select union_name from union_table ut , employeedetails ed where ut.union_membership_number = ed.union_membership_number and ssn = "
    query4 += rr[0][0]
    query4 += ';'
    cursorObject.execute(query4)
    rr3 = cursorObject.fetchall()

    if(request.method == "POST"):
        # session.permanent='True'
        if "phn" in request.form or "addr" in request.form or "pwd" in request.form:
            new_phone = request.form['phn']
            new_address = request.form['addr']
            new_password = request.form['pwd']

            # print(new_phone, new_address, new_password)

            if new_phone:
                query5 = "update employee set phone = '" + \
                    str(new_phone) + "' where username = '" + \
                    str(username) + "';"
                # print(query5)
                cursorObject.execute(query5)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('FAA', username=username))

            elif new_address:
                query6 = "update employee set address = '" + \
                    str(new_address) + "' where username = '" + \
                    str(username) + "';"
                # print(query6)
                cursorObject.execute(query6)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('FAA', username=username))

            elif new_password:
                query7 = "update employee set password = '" + \
                    str(new_password) + "' where username = '" + \
                    str(username) + "';"
                # print(query7)
                cursorObject.execute(query7)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('FAA', username=username))
        elif "updated_tech_ssn" in request.form and "updated_FAA_Number" in request.form and "updated_no_of_hours" in request.form and "updated_date" in request.form and "updated_score" in request.form and "updated_regno" in request.form:
            # print(1)
            # if(session['updated_tech_ssn'] is None and session['updated_no_of_hours'] is None and session['updated_date'] is None and session['updated_score'] is None and session['updated_max_score'] is None and session['updated_regno'] is None):
            if('updated_tech_ssn' not in session and 'updated_FAA_Number' not in session and 'updated_no_of_hours' not in session and 'updated_date' not in session and 'updated_score' not in session and 'updated_regno' not in session):
                # print(2)
                # session={'updated_tech_ssn':[],'updated_no_of_hours':[],'updated_date':[],'updated_score':[],'updated_max_score':[],'updated_regno':[],'permenent':'True'}
                session['updated_tech_ssn'] = []
                session['updated_FAA_Number'] = []
                session['updated_no_of_hours'] = []
                session['updated_date'] = []
                session['updated_score'] = []

                session['updated_regno'] = []

                session['updated_tech_ssn'].append(
                    request.form['updated_tech_ssn'])
                session['updated_FAA_Number'].append(
                    request.form['updated_FAA_Number'])
                session['updated_no_of_hours'].append(
                    request.form['updated_no_of_hours'])
                session['updated_date'].append(request.form['updated_date'])
                session['updated_score'].append(request.form['updated_score'])

                session['updated_regno'].append(request.form['updated_regno'])
                # print(session)

            else:
                session['updated_tech_ssn'].append(
                    request.form['updated_tech_ssn'])
                session['updated_FAA_Number'].append(
                    request.form['updated_FAA_Number'])
                session['updated_no_of_hours'].append(
                    request.form['updated_no_of_hours'])
                session['updated_date'].append(request.form['updated_date'])
                session['updated_score'].append(request.form['updated_score'])

                session['updated_regno'].append(request.form['updated_regno'])
                # print(session)

        else:
            return redirect(url_for('FAA', username=username))

    dataBase.close()
    # for key in list(session.keys()):
    #     session.pop(key)
    temp_address = rr[0][2].split(',')
    # print(4568)
    address_line1 = temp_address[0]+' '+temp_address[1]
    address_line2 = temp_address[2]+' '+temp_address[3]
    # print(session)
    # session.pop('updated_max_score', None)
    # print(session)
    return render_template("FAA.html", Name=rr[0][1], phone=rr[0][3], address_line_1=address_line1, address_line_2=address_line2, department=rr[0][4], union_mem_no=rr2[0][0], union_name=rr3[0][0], FAA_tabular_li=rr1)


@app.route('/Technician/<username>', methods=['POST', 'GET'])
def Technician(username):
    session.permanent = 'True'
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    # name=request.form['uname']
    # password=request.form['psw']
    # name = request.args['name']
    # querry0="Select ssn from employeedetails where username = "
    # querry0+=username
    # querry0+=';'
    # cursorObject.execute(query1)
    # rr0=cursorObject.fetchall()
    query1 = "SELECT * FROM EMPLOYEE where role = 'Technician' and username = '" + \
        str(username) + "';"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    query2 = "select ed.name as technicain_name,t.date,  t.no_of_hours, t.score, tms.maximum_possible_score,  t.Reg_no,t.FAA_number from test t, test_max_score tms, employeedetails ed where t.reg_no=tms.reg_no and ed.ssn=t.ssn "
    # query2+= rr[0][1]
    query2 += " order by date desc;"
    cursorObject.execute(query2)
    rr1 = cursorObject.fetchall()
    # query2 = "select salary from employee_salary where role='technician' ;"
    # cursorObject.execute(query2)
    # rr1 = cursorObject.fetchall()
    query3 = "select union_membership_number from employeedetails where ssn = "
    # name= rr[0][0]
    query3 += rr[0][0]
    cursorObject.execute(query3)
    rr2 = cursorObject.fetchall()
    query4 = "select union_name from union_table ut , employeedetails ed where ut.union_membership_number = ed.union_membership_number and ssn = "
    query4 += rr[0][0]
    query4 += ';'
    cursorObject.execute(query4)
    rr3 = cursorObject.fetchall()
    # print(username)
    query5 = "select td.FAA_number, td.date, td.No_of_hours,td.ssn,td.score,td.maximum_possible_score,ed.name, td.reg_no from testdetails td, employeedetails ed where td.ssn=ed.ssn and ed.ssn = "
    query5 += rr[0][0]
    query5 += ';'
    cursorObject.execute(query5)
    rr4 = cursorObject.fetchall()

    if(request.method == "POST"):
        if "phn" in request.form or "addr" in request.form or "pwd" in request.form:
            new_phone = request.form['phn']
            new_address = request.form['addr']
            new_password = request.form['pwd']

            # print(new_phone, new_address, new_password)

            if new_phone:
                query6 = "update employee set phone = '" + \
                    str(new_phone) + "' where username = '" + \
                    str(username) + "';"
                print(new_phone)
                cursorObject.execute(query6)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Technician', username=username))

            elif new_address:
                query7 = "update employee set address = '" + \
                    str(new_address) + "' where username = '" + \
                    str(username) + "';"
                # print(new_address)
                cursorObject.execute(query7)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Technician', username=username))

            elif new_password:
                query8 = "update employee set password = '" + \
                    str(new_password) + "' where username = '" + \
                    str(username) + "';"
                # print(query8)
                cursorObject.execute(query8)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Technician', username=username))

        else:
            return redirect(url_for('Technician', username=username))

    dataBase.close()
    # ssn = rr[0]
    # name = rr[1]
    # address = rr[2]
    # phone = rr[3]
    # role = rr[4]
    # username = rr[5]
    # password = rr[6]
    # salary = rr[7]
    # union_membership_number = rr[8]
    temp_address = rr[0][2].split(',')
    address_line1 = temp_address[0]+' '+temp_address[1]
    address_line2 = temp_address[2]+' '+temp_address[3]
    # print(address_line1,address_line2)
    # print(rr4)
    print(session)
    return render_template("technician.html", Name=rr[0][1], phone=rr[0][3], address_line_1=address_line1, address_line_2=address_line2, department=rr[0][4], union_mem_no=rr2[0][0], union_name=rr3[0][0], li=rr4, all_test_li=rr1)


@app.route('/Admin/<username>', methods=['POST', 'GET'])
def Admin(username):
    session.permanent = 'True'
    print(len(session['updated_FAA_Number']))
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    query1 = "SELECT * FROM EMPLOYEE where role = 'Admin' and username = '" + \
        username + "';"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    query2 = "select salary from employee_salary where role='Admin' ;"
    cursorObject.execute(query2)
    rr1 = cursorObject.fetchall()
    # print(rr1[0][0])
    query3 = "select union_membership_number from employeedetails where ssn = "
    # name= rr[0][0]
    query3 += rr[0][0]
    cursorObject.execute(query3)
    rr2 = cursorObject.fetchall()

    query4 = "select union_name from union_table ut , employeedetails ed where ut.union_membership_number = ed.union_membership_number and ssn = "
    query4 += rr[0][0]
    query4 += ';'
    cursorObject.execute(query4)
    rr3 = cursorObject.fetchall()
    query5 = "Select ssn, name, role, salary from employeedetails;"
    cursorObject.execute(query5)
    rr4 = cursorObject.fetchall()

    query6 = "select ed.ssn, ed.name, ed.union_membership_number, ut.union_name  from employee_union eu, union_table ut, employeedetails ed where eu.union_membership_number = ut.union_membership_number and ed.ssn = eu.ssn and ut.union_name = 'management' order by ed.name;"
    cursorObject.execute(query6)
    rr5 = cursorObject.fetchall()
    query7 = "select ed.ssn, ed.name, ed.union_membership_number, ut.union_name  from employee_union eu, union_table ut, employeedetails ed where eu.union_membership_number = ut.union_membership_number and ed.ssn = eu.ssn and ut.union_name = 'workers' order by ed.name;"
    cursorObject.execute(query7)
    rr6 = cursorObject.fetchall()

    if(('updated_tech_ssn' not in session and 'updated_FAA_Number' not in session and 'updated_no_of_hours' not in session and 'updated_date' not in session and 'updated_score' not in session and 'updated_regno' not in session) or (not session['updated_FAA_Number'] or not session['updated_tech_ssn'] or not session['updated_date'] or not session['updated_no_of_hours'] or not session['updated_score'] or not session['updated_regno'])):
        # print(2)
        # session={'updated_tech_ssn':[],'updated_no_of_hours':[],'updated_date':[],'updated_score':[],'updated_max_score':[],'updated_regno':[],'permenent':'True'}
        session['updated_tech_ssn'] = []
        session['updated_FAA_Number'] = []
        session['updated_no_of_hours'] = []
        session['updated_date'] = []
        session['updated_score'] = []
        session['updated_regno'] = []

        session['updated_tech_ssn'].append('-')
        session['updated_FAA_Number'].append('-')
        session['updated_no_of_hours'].append('-')
        session['updated_date'].append('-')
        session['updated_score'].append('-')
        session['updated_regno'].append('-')

    elif(len(session['updated_FAA_Number']) > 1 and len(session['updated_tech_ssn']) > 1 and len(session['updated_date']) > 1 and len(session['updated_no_of_hours']) > 1 and len(session['updated_score']) > 1 and len(session['updated_regno']) > 1):
        
        if('-' in session['updated_FAA_Number'] and session['updated_tech_ssn'] and '-' in session['updated_date'] and '-' in session['updated_no_of_hours'] and '-' in session['updated_score'] and '-' in session['updated_regno']):
            
            session['updated_FAA_Number'].remove('-')

            session['updated_tech_ssn'].remove('-')

            session['updated_no_of_hours'].remove('-')

            session['updated_date'].remove('-')

            session['updated_score'].remove('-')

            session['updated_regno'].remove('-')

    if(request.method == "POST"):
        if "phn" in request.form or "addr" in request.form or "pwd" in request.form:
            new_phone = request.form['phn']
            new_address = request.form['addr']
            new_password = request.form['pwd']

            # print(new_phone, new_address, new_password)

            if new_phone:
                query8 = "update employee set phone = '" + \
                    str(new_phone) + "' where username = '" + \
                    str(username) + "';"
                # print(query8)
                cursorObject.execute(query8)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Admin', username=username))

            elif new_address:
                query9 = "update employee set address = '" + \
                    str(new_address) + "' where username = '" + \
                    str(username) + "';"
                # print(query9)
                cursorObject.execute(query9)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Admin', username=username))

            elif new_password:
                query10 = "update employee set password = '" + \
                    str(new_password) + "' where username = '" + \
                    str(username) + "';"
                # print(query10)
                cursorObject.execute(query10)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Admin', username=username))

        elif "ssn" in request.form and "name" in request.form and "role" in request.form and "phone" in request.form and "addr1" in request.form and "addr2" in request.form and "un" in request.form and "pd" in request.form and "uname" in request.form and "unum" in request.form:
            ssn = request.form['ssn']
            name = request.form['name']
            role = request.form['role']
            phone = request.form['phone']
            addr1 = request.form['addr1']
            addr2 = request.form['addr2']
            # salary = request.form['salary']
            un = request.form['un']
            pd = request.form['pd']
            union_name = request.form['uname']
            union_number = request.form['unum']

            if ssn and name and role and phone and addr1 and addr2 and un and pd and union_name and union_number:
                addr = addr1 + addr2
                query11 = "insert into `employee`(`ssn`,`name`,`address`,`phone`,`role`,`username`,`password`) values ('" + str(
                    ssn) + "','" + str(name) + "','" + str(addr) + "','" + str(phone) + "','" + str(role) + "','" + str(un) + "','" + str(pd) + "');"
                # print(query11)
                cursorObject.execute(query11)
                query12 = "insert into `union_table`(`union_name`,`union_membership_number`) values ('" + str(
                    union_name) + "','" + str(union_number) + "');"
                # print(query12)
                cursorObject.execute(query12)
                query13 = "insert into `Employee_Union` (`ssn`,`role`,`Union_Membership_number`) values ('" + str(
                    ssn) + "','" + str(role) + "','" + str(union_number) + "');"
                # print(query13)
                cursorObject.execute(query13)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Admin', username=username))

        elif "dssn" in request.form:
            dssn = request.form['dssn']

            if dssn:
                query14 = "delete from `employee` where ssn = '" + \
                    str(dssn) + "';"
                cursorObject.execute(query14)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Admin', username=username))

        else:
            return redirect(url_for('Admin', username=username))

    dataBase.close()
    # print(session)
    # temp_dict=session
    # ssn = rr[0]
    # name = rr[1]
    # address = rr[2]
    # phone = rr[3]
    # role = rr[4]
    # username = rr[5]
    # password = rr[6]
    # salary = rr[7]
    # union_membership_number = rr[8]
    temp_address = rr[0][2].split(',')
    address_line1 = temp_address[0]+' '+temp_address[1]
    address_line2 = temp_address[2]+' '+temp_address[3]
    # print(rr5)
    # for key in list(session.keys()):
    #     session.pop(key)
    # print(session)
    # print(temp_dict)
    return render_template("admin.html", Name=rr[0][1],
                           phone=rr[0][3], address_line_1=address_line1, address_line_2=address_line2,
                           department=rr[0][4], union_mem_no=rr2[0][0], union_name=rr3[0][0], employee_li=rr4,
                           union_management_li=rr5, union_workers_li=rr6,
                           length_of_temp=len(session['updated_tech_ssn']), temp=session,
                           username=username)


@app.route('/Traffic_Controller<username>', methods=['POST', 'GET'])
def Traffic_Controller(username):
    session.permanent = 'True'
    # ph_no=request.form['new_phno']
    # address=request.form['new_address']
    # password=request.form['new_password']
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    query1 = "SELECT * FROM EMPLOYEE where role = 'Traffic_Controller' and username = '" + \
        str(username) + "';"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    query2 = "select salary from employee_salary where role='traffic_controller' ;"
    cursorObject.execute(query2)
    rr1 = cursorObject.fetchall()

    query3 = "select union_membership_number from employeedetails where ssn = "
    # name= rr[0][0]
    query3 += rr[0][0]
    cursorObject.execute(query3)
    rr2 = cursorObject.fetchall()
    query4 = "select union_name from union_table ut , employeedetails ed where ut.union_membership_number = ed.union_membership_number and ssn = "
    query4 += rr[0][0]
    query4 += ';'
    cursorObject.execute(query4)
    rr3 = cursorObject.fetchall()

    query5 = "select * from traffic_controller where ssn = "
    query5 += rr[0][0] + ';'
    cursorObject.execute(query5)
    rr4 = cursorObject.fetchall()

    if(request.method == "POST"):
        if "phn" in request.form or "addr" in request.form or "pwd" in request.form:
            new_phone = request.form['phn']
            new_address = request.form['addr']
            new_password = request.form['pwd']

            # print(new_phone, new_address, new_password)

            if new_phone:
                query6 = "update employee set phone = '" + \
                    str(new_phone) + "' where username = '" + \
                    str(username) + "';"
                # print(query6)
                cursorObject.execute(query6)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Traffic_Controller', username=username))

            elif new_address:
                query7 = "update employee set address = '" + \
                    str(new_address) + "' where username = '" + \
                    str(username) + "';"
                # print(query7)
                cursorObject.execute(query7)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Traffic_Controller', username=username))

            elif new_password:
                query8 = "update employee set password = '" + \
                    str(new_password) + "' where username = '" + \
                    str(username) + "';"
                # print(query8)
                cursorObject.execute(query8)
                dataBase.commit()
                dataBase.close()
                return redirect(url_for('Traffic_Controller', username=username))

        else:
            return redirect(url_for('Traffic_Controller', username=username))

    dataBase.close()
    # ph_no=request.form['new_phno']
    # address=request.form['new_address']
    # password=request.form['new_password']
    # print(query3+rr[0][0])
    # ssn = rr[0]
    # name = rr[1]
    # address = rr[2]
    # phone = rr[3]
    # role = rr[4]
    # username = rr[5]
    # password = rr[6]
    # salary = rr[7]
    # union_membership_number = rr[8]
    # for i in rr[0]:
    #     print(i)
    # print(ph_no)
    temp_address = rr[0][2].split(',')
    address_line1 = temp_address[0]+' '+temp_address[1]
    address_line2 = temp_address[2]+' '+temp_address[3]
    # print(address_line1,address_line2)
    # print(username)
    # print(rr4[0][0])
    print(session)
    return render_template("traffic_controller.html", Name=rr[0][1], phone=rr[0][3], address_line_1=address_line1, address_line_2=address_line2, department=rr[0][4], union_mem_no=rr2[0][0], union_name=rr3[0][0], li=rr4)


@app.route("/admin_testdetails/<username>", methods=['POST', 'GET'])
def admin_testdetails(username):
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    session.permanent = 'True'
    query1 = "select ed.name as technician_name,td.FAA_number,td.date, td.no_of_hours, td.score, tms.maximum_possible_score, td.reg_no   from test td, employeedetails ed, test_max_score tms  where ed.ssn=td.ssn and tms.reg_no=td.reg_no order by td.date;"
    cursorObject.execute(query1)
    rr1 = cursorObject.fetchall()
    return render_template("admin_testdetails.html", FAA_display=rr1, username=username)


@app.route("/admin_approve_faa/<username>/<faa>/<ssn>/<date>/<hours>/<score>/<regno>", methods=['POST', 'GET'])
def admin_approve_faa(username, faa, ssn, date, hours, score, regno):
    session.permanent = 'True'
    # name = request.form['uname']
    # password = request.form['psw']
    print(faa, ssn, date, hours, score, regno)
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="AKash@123",
        database="dbproject_normalized",
        auth_plugin='caching_sha2_password')
    cursorObject = dataBase.cursor()
    query1 = "SELECT `USERNAME`,`PASSWORD`,`ROLE` FROM `EMPLOYEE` where role = 'Admin';"
    cursorObject.execute(query1)
    rr = cursorObject.fetchall()
    query2 = "select faa_name from test where faa_number = '" + faa + "';"
    cursorObject.execute(query2)
    rr2 = cursorObject.fetchall()
    faaname = rr2[0][0]

    # usernames = [i[0] for i in rr]
    # passwords = [i[1] for i in rr]
    # roles = [i[2] for i in rr]

    if(request.method == "POST"):
        name = request.form['uname']
        password = request.form['psw']
    # print(rr[0][0],rr[0][1])
        if(username == rr[0][0] and password == rr[0][1]):
            # query="insert into test values (%s,%s,%s,%s,%s,%s,%s)",(session['updated_FAA_Number'][0], session['updated_date'][0], session['updated_no_of_hours'][0] , session['updated_score'][0], session['updated_tech_ssn'][0], session['updated_reg_no'][0], 'Ram')
            # print(session)
            query3 = "insert into test values ('"
            query3 += faa
            query3 += "','" + date + "','" + hours + "','" + score + \
                "','" + ssn + "','" + regno + "','" + faaname + "');"
            cursorObject.execute(query3)
            dataBase.commit()
            dataBase.close()

            if faa in session['updated_FAA_Number']:
                session['updated_FAA_Number'].remove(faa)

            if ssn in session['updated_tech_ssn']:
                session['updated_tech_ssn'].remove(ssn)

            if hours in session['updated_no_of_hours']:
                session['updated_no_of_hours'].remove(hours)

            if date in session['updated_date']:
                session['updated_date'].remove(date)

            if score in session['updated_score']:
                session['updated_score'].remove(score)

            if regno in session['updated_regno']:
                session['updated_regno'].remove(regno)

            # session.pop("updated_FAA_Number", None)
            return redirect(url_for("Admin", username=username))
        else:
            return render_template("admin_approve_faa.html", CMT="incorrect username or password")
    dataBase.close()
    # session.pop("updated_FAA_Number", None)
    # print(session)

    # print(query)

    # print(username,password)
    # if name in usernames:
    #     if passwords[usernames.index(name)] == password:
    #         print("IN")
    #         role = roles[usernames.index(name)]
    #         # htmlp=role+".html"
    #         # print(htmlp)
    #         return redirect(url_for(role, username=name))
    #         # if(role=='FAA'):
    #         #     return redirect(url_for(role))
    #         # if(role=="Admin"):
    #         #     return redirect(url_for(role))
    #         # if(role=="Technician"):
    #         #     return redirect(url_for(role))
    #         # if(role=="Traffic Controller"):
    #         #     return redirect(url_for(role))
    #     else:
    #         return render_template("index.html", CMT="Invalid Username or Password")

    return render_template("admin_approve_faa.html")

@app.route("/admin_decline_faa/<username>/<faa>/<ssn>/<date>/<hours>/<score>/<regno>", methods=['POST', 'GET'])
def admin_decline_faa(username, faa, ssn, date, hours, score, regno):
    session.permanent = 'True'
    # name = request.form['uname']
    # password = request.form['psw']
    print(faa, ssn, date, hours, score, regno)

    if faa in session['updated_FAA_Number']:
        session['updated_FAA_Number'].remove(faa)

    if ssn in session['updated_tech_ssn']:
        session['updated_tech_ssn'].remove(ssn)

    if hours in session['updated_no_of_hours']:
        session['updated_no_of_hours'].remove(hours)

    if date in session['updated_date']:
        session['updated_date'].remove(date)

    if score in session['updated_score']:
        session['updated_score'].remove(score)

    if regno in session['updated_regno']:
        session['updated_regno'].remove(regno)

    return render_template("admin_decline_faa.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)