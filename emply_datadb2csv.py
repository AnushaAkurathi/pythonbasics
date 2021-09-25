import mysql.connector


def fetch_table_data(employe_data):
    
    cnx = mysql.connector.connect(
        host='localhost',
        database='test2',
        user='root',
        password='Anu@1234'
    )

    cursor = cnx.cursor()
    cursor.execute('select * from ' + employe_data)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    
    cnx.close()

    return header, rows

def export(employe_data):
    header, rows = fetch_table_data(employe_data)

    
    f = open(employe_data + '.csv', 'w')

    
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)



export('employe_data')
