import os
import sqlite3
import pandas as pd

# data_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
headers = ['Policy_id','Date of Purchase','Customer_id','Fuel','VEHICLE_SEGMENT','Premium','bodily injury liability','personal injury protection','property damage liability','collision','comprehensive','Customer_Gender','Customer_Income group','Customer_Region','Customer_Marital_status']
data_table = pd.read_csv('data.csv', header=None, names=headers, converters={'zip': str})


# Create a database
conn = sqlite3.connect('abc.db',check_same_thread=False)

# Add the data to our database


conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows