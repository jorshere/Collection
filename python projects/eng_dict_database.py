import mysql.connector

con=mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)
cursor= con.cursor()                # used to navigate through DB;
word= input("enter word: ")
query= cursor.execute(f"SELECT * FROM Dictionary WHERE expression ='{word}'")
#query= cursor.execute("SELECT * FROM Dictionary WHERE expression LIKE 'r%'")    #to get meaning of words starts with "R"
#query= cursor.execute("SELECT * FROM Dictionary WHERE expression LIKE 'rain%'") # to get values starts with "rain"
#query= cursor.execute("SELECT * FROM Dictionary WHERE length(expression) = 4")  # to get expression whose length in equal to 4;
#query= cursor.execute("SELECT * FROM Dictionary WHERE length(exprssion)>1 AND length(expression)<5)     # to set "AND" operator    
result=cursor.fetchall()            # method to fetch all item;
#print(result[1])               * to get all the meaning or 2nd meaning;

if result:
    for item in result:
        print(item)          # to get only the meanings OR
       #print(item) 
else:
    print("no meaning found")