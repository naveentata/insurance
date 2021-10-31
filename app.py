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

@app.route('/graph') 
def sql_graph():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT DateofPurchase  FROM data''')
    msg = 'SELECT DateofPurchase FROM data'
    sample = []
    for ele in results:
        sample.append(ele['DateofPurchase'])

    for i in range(0,len(sample)):
        sample[i]=sample[i].split("/")
        for j in range(0,len(sample[i])):
            sample[i][j]=int(sample[i][j])
    # print(sample)
    main={}
    needed=[2018]

    for ele in needed:
        main[ele]={}
        for i in range(1,13):
            main[ele][i]=0

    for ele in sample:
        if(ele[2] in needed):
            main[ele[2]][ele[0]]+=1
    print(main)
    # keys=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    val=[]
    for i in range(1,13):
        val.append(main[2018][i])
    

    return render_template('graph.html', val=val, msg=msg)

@app.route('/search',methods = ['POST', 'GET']) 
def search_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM data''')
    msg = 'SELECT * FROM data'
    if request.method== 'POST':
        search = request.form['search']
        results = sql_query(''' SELECT * FROM data where Policy_id ='%?%'  ''',(search,))
    return render_template('searchdatabase.html', results=results, msg=msg)




@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        Policy_id = request.args.get('Policy_id')

        sql_delete(''' DELETE FROM data where Policy_id = ?''', (Policy_id,) )
    results = sql_query(''' SELECT * FROM data''')
    msg = 'DELETE FROM data WHERE first_name = ' 
    return render_template('sqldatabase.html', results=results, msg=msg)

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        ePolicy_id = request.args.get('ePolicy_id')
        eresults = sql_query2(''' SELECT * FROM data where Policy_id = ?''',(ePolicy_id,))
    results = sql_query(''' SELECT * FROM data''')
    return render_template('sqldatabase.html', eresults=eresults, results=results)

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        Policy_id = request.form['Policy_id']
        # DateofPurchase = request.form['DateofPurchase']
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
        sql_edit_insert(''' UPDATE data set Policy_id=?,Customer_id=?,Fuel=?,VEHICLE_SEGMENT=?,Premium=?,bodilyinjuryliability=?,personalinjuryprotection=?,propertydamageliability=?,collision=?,comprehensive=?,Customer_Gender=?,Customer_Incomegroup=?,Customer_Region=?,Customer_Marital_status=? WHERE Policy_id=? ''', (Policy_id,Customer_id,Fuel,VEHICLE_SEGMENT,Premium,bodilyinjuryliability,personalinjuryprotection,propertydamageliability,collision,comprehensive,Customer_Gender,Customer_Incomegroup,Customer_Region,Customer_Marital_status,Policy_id,))
    results = sql_query(''' SELECT * FROM data''')
    msg = 'UPDATE data set'
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
