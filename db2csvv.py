import mysql.connector


def fetch_table_data(student_records):
    
    cnx = mysql.connector.connect(
        host='localhost',
        database='test2',
        user='root',
        password='Anu@1234'
    )

    cursor = cnx.cursor()
    cursor.execute('select * from ' + student_records)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    
    cnx.close()

    return header, rows

def export(student_records):
    header, rows = fetch_table_data(student_records)

    
    f = open(student_records + '.csv', 'w')

    
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)



export('student_records')

