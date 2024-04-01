from internet_bs3_requests import *
import pymssql


query_insert = ''' INSERT INTO podaci 
                (sifra, naziv, gl_grad, populacija, povrsina)
                VALUES (%s, %s, %s, %s, %s)

               '''


query_create = '''  CREATE TABLE podaci (
                    sifra INT PRIMARY KEY,
                    naziv VARCHAR(100), 
                    gl_grad VARCHAR(100),
                    populacija INT,
                    povrsina FLOAT)
                '''


broj = len(lista_n)
#print(broj)    


# "Provider=SQLOLEDB;Data Source=serverName;"
# Initial Catalog=databaseName;
# User ID=MyUserID;Password=MyPassword;"


SERVER = '172.21.206.245'
DATABASE = 'Drzave'
USERNAME = 'python'
PASSWORD = 'Test123'
PROVIDER = 'MSOLEDBSQL'

#print('tu sam')

conn = pymssql.connect(
    server='172.21.206.245',
    user='python',
    password='Test123',
    database='Drzave',
    as_dict=True
)


#connectionString = f'DRIVER={PROVIDER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
#conn = pyodbc.connect(connectionString) 


try:

    cursor = conn.cursor()
    cursor.execute(query_create)
    # print('kreirao tablicu')
    conn.commit()

    

    for x in range(broj):
        y = (x+1, lista_n[x], lista_c[x], lista_p[x], lista_a[x])
        cursor.execute(query_insert, y)

    print('ubacio sam')

    
    conn.commit()


    cursor.close()



except: 
    print('Greška pri spajanju na bazu')

finally:
    conn.close()




