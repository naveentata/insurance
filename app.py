from flask import Flask, request, redirect, render_template
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")  #OPTIONAL: Only if need to access Python packages installed on a local (non-global) directory
sys.path.insert(2, "PATH TO FLASK DIRECTORY")      #OPTIONAL: Only if you need to add the directory of your flask app

app = Flask(__name__)

@app.route('/') 
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data''')
    msg = 'SELECT * FROM data'
    return render_template('sqldatabase.html', results=results, msg=msg)


@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        sql_edit_insert(''' INSERT INTO data (first_name,last_name,address,city,state,zip) VALUES (?,?,?,?,?,?) ''', (first_name,last_name,address,city,state,zip) )
    results = sql_query(''' SELECT * FROM data''')
    msg = 'INSERT INTO data (first_name,last_name,address,city,state,zip) VALUES ('+first_name+','+last_name+','+address+','+city+','+state+','+zip+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 


@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM data where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM data''')
    msg = 'DELETE FROM data WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM data where first_name = ? and last_name = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM data''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)

        CREATE TABLE "data" (
	"Policy_id"	INTEGER,
	"DateofPurchase"	TEXT,
	"Customer_id"	INTEGER,
	"Fuel"	TEXT,
	"VEHICLE_SEGMENT"	TEXT,
	"Premium"	INTEGER,
	"bodilyinjuryliability"	INTEGER,
	"personalinjuryprotection"	INTEGER,
	"propertydamageliability"	INTEGER,
	"collision"	INTEGER,
	"comprehensive"	INTEGER,
	"Customer_Gender"	TEXT,
	"Customer_Incomegroup"	TEXT,
	"Customer_Region"	TEXT,
	"Customer_Marital_status"	INTEGER
)
@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        Policy_id = request.form['Policy_id']
        DateofPurchase = request.form['DateofPurchase']
        Customer_id = request.form['Customer_id']
        Fuel = request.form['Fuel']
        VEHICLE_SEGMENT = request.form['VEHICLE_SEGMENT']
        Premium = request.form['Premium']
        bodilyinjuryliability = request.form['bodilyinjuryliability']
        personalinjuryprotection = request.form['personalinjuryprotection']
        propertydamageliability = request.form['propertydamageliability']
        collision = request.form['collision']
        comprehensive = request.form['comprehensive']
        Customer_Gender = request.form['Customer_Gender']
        Customer_Incomegroup = request.form['Customer_Incomegroup']
        Customer_Region = request.form['Customer_Region']
        Customer_Marital_status = request.form['Customer_Marital_status']
        sql_edit_insert(''' UPDATE data set Policy_id=?,DateofPurchase=?,Customer_id=?,Fuel=?,VEHICLE_SEGMENT=?,Premium=?,bodilyinjuryliability=?,personalinjuryprotection=?,propertydamageliability=?,collision=?,comprehensive=?,Customer_Gender=?,Customer_Incomegroup=?,Customer_Region=?,Customer_Marital_status=? WHERE Policy_id=? ''', (Policy_id,DateofPurchase,Customer_id,Fuel,VEHICLE_SEGMENT,Premium,bodilyinjuryliability,personalinjuryprotection,propertydamageliability,collision,comprehensive,Customer_Gender,Customer_Incomegroup,Customer_Region,Customer_Marital_status))
    results = sql_query(''' SELECT * FROM data''')
    msg = 'UPDATE data set first_name = ' + first_name + ', last_name = ' + last_name + ', address = ' + address + ', city = ' + city + ', state = ' + state + ', zip = ' + zip + ' WHERE first_name = ' + old_first_name + ' and last_name = ' + old_last_name
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)