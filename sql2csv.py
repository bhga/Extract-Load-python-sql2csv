import MySQLdb
import pandas as pd

outputpath=input("Enter the output path file:")

db=MySQLdb.connect(host='',user='',password='',database='')
mycursor=db.cursor()

query = 'select * from tablename'

mycursor.execute(query)
dfRecord=pd.DataFrame(mycursor.fetchall()) #note: by default fetchall() loads data into tuple here we are storing it into DataFrame
db.commit()
print("Successfully Read the table data")
dfRecord.rename(columns={0:'col1',1:'col2',2:'col3',3:'col4',4:'col5',5:'col6',6:'col7'},inplace=True) #Renaming the columns by applying inplace
dfRecord.to_csv(outputpath,index=False) #if we don't specify delimiter by default it takes as tab
print("Import of the MySQL data into CSV is successfull!!!")
