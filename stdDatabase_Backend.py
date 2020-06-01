# -*- coding: utf-8 -*-
"""
Created on Sat May 30 22:15:36 2020

@author: Pranav Deshpande
"""

import sqlite3
#backend

def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text,DOB text,\
                Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()
    
def addStdRec(StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",(StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    con.commit()
    con.close    
    
def viewData():
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close    
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close    

def searchData(StdID="", Firstname="", Surname="", DOB="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DOB=? OR Age=? OR Gender=? OR Address=? OR \
                Mobile=?", (StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    rows =cur.fetchall()
    con.close    
    return rows
    
def dataUpdate(id, StdID="", Firstname="", Surname="", DOB="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Surname=?, DOB=?, Age=?, Gender=?, Address=?, Mobile=? WHERE id=?", \
                (StdID, Firstname, Surname, DOB, Age, Gender, Address, Mobile))
    con.commit()
    con.close    

    
studentData()