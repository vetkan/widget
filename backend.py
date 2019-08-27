import sqlite3


#Cursor allows Python code to execute PostgreSQL command in a database session.
#The column names cannot have '', since SQLIte cannot read it and we cannot use quotes


def connect():
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tool ('id' INTEGER PRIMARY KEY,'Row_Current_Ind' text, 'Row_Deleted_Ind' text, 'CPT_Codes' text,'Valid_From' text,'Valid_To' text,'Key_Value' INTEGER )")
    conn.commit()
    conn.close()

#The id value is Integer Primary kay. Here, we don't need to pass on the values. Python will automatiocally create the values. Hence we set it as NULL in INSERT.
#Make sure that the execute contains only column names without quotes, else we will start printing them in the table.
        
def insert(Row_Current_Ind,Row_Deleted_Ind,CPT_Codes,Valid_From,Valid_To,Key_Value):
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO tool VALUES(NULL,?,?,?,?,?,?)",(Row_Current_Ind,Row_Deleted_Ind,CPT_Codes,Valid_From,Valid_To,Key_Value))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tool")
    rows=cur.fetchall()
    conn.close()
    return rows

#search and update not working

def search(Row_Current_Ind = "",Row_Deleted_Ind = "",CPT_Codes ="",Valid_From = "",Valid_To = "",Key_Value = ""):
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM tool  WHERE Row_Current_Ind=? OR Row_Deleted_Ind=? OR CPT_Codes=? OR Valid_From=? OR Valid_To=? OR Key_Value=?",(Row_Current_Ind,Row_Deleted_Ind,CPT_Codes,Valid_From,Valid_To,Key_Value))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM tool WHERE id=? ",(id,))
    conn.commit()
    conn.close()
    
def update(id,Row_Current_Ind,Row_Deleted_Ind,CPT_Codes,Valid_From,Valid_To,Key_Value):
    conn=sqlite3.connect("Star_Tool.db")
    cur=conn.cursor()
    cur.execute("UPDATE tool SET Row_Current_Ind=?,Row_Deleted_Ind=?,CPT_Codes=?,Valid_From=?,Valid_To=?,Key_Value=? WHERE id=? ",(Row_Current_Ind,Row_Deleted_Ind,CPT_Codes,Valid_From,Valid_To,Key_Valueid))
    conn.commit()
    conn.close()

connect()
#print(update(5, '12/01/2019', '12/01/2020', 'H1', '12/01/2018', '12/01/2021', 3))
#print(view())