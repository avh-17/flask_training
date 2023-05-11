import psycopg2
import datetime

conn = psycopg2.connect(database="avh_db",
                        host="127.0.0.1",
                        user="postgres",
                        password="Valtech123",
                        port=5432)

cursor = conn.cursor()

smpdb = """CREATE TABLE smpdb 
(
    id SERIAL PRIMARY KEY,
    profileID VARCHAR(80) NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL, 
    firstname VARCHAR(80),
    lastname VARCHAR(80),
    email VARCHAR(150) NOT NULL,
    createdAt TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updatedAt TIMESTAMP WITH TIME ZONE,
    humanApis JSON,
    status INT DEFAULT 1,
    phonenumber VARCHAR(15) ,
    phonevalidation BOOLEAN DEFAULT False,
    emailvalidation BOOLEAN DEFAULT False,
    role TEXT [] NOT NULL,
    source INT
);
"""

in_row_2 = ("""INSERT INTO smpdb (profileID,
    username,
    password, 
    firstname,
    lastname ,
    email,
    createdAt,
    updatedAt,
    humanApis,
    status,
    phonenumber,
    phonevalidation,
    emailvalidation,
    role,
    source)
    VALUES('rdj17','ramsey','valrdj123','rams','dj','rdj15@gmail.com',%s,%s,'[{"name":"ram","salary":50000,"married":false}]',1,'8936543218',True,False,array['guest', 'user'],482)
    """)

in_row_3 = ("""INSERT INTO smpdb (
profileID,
username,
password, 
firstname,
lastname ,
email,
createdAt,
updatedAt,
humanApis,
status,
phonenumber,
phonevalidation,
emailvalidation,
role,
source)
VALUES (
'bry19',
'bryan',
'valbry123',
'bryan',
'adams',
'brya15@gmail.com',
%s,
%s,
'[{"name":"bry","salary":80000,"married":true}]',
2,
'2357378092',
True,
True,
array['emp ', 'dev'],
352
)
""")

in_row_4 = ("""INSERT INTO smpdb (
profileID,
username,
password, 
firstname,
lastname ,
email,
createdAt,
updatedAt,
humanApis,
status,
phonenumber,
phonevalidation,
emailvalidation,
role,
source)
VALUES (
'ani18',
'anirudh',
'valani123',
'ani',
'',
'ani15@gmail.com',
%s,
%s,
'[{"name":"ani","salary":40000,"married":false}]',
1,
'6462173861',
True,
False,
array['asd', 'emp'],
529
)
""")

in_row_5 = ("""INSERT INTO smpdb (
    profileID,
    username,
    password, 
    firstname,
    lastname ,
    email,
    createdAt,
    updatedAt,
    humanApis,
    status,
    phonenumber,
    phonevalidation,
    emailvalidation,
    role,
    source)
    VALUES (
    'rkl2',
    'rahul',
    'valrahul123',
    'rahul',
    'k l',
    'rahulkl2@gmail.com',
    %s,
    %s,
    '[{"name":"rahul","salary":1300000,"married":true}]',
    3,
    '23547382992',
    False,
    True,
    array['manager', 'emp'],
    212
    )
    """)

in_row_6 = ("""INSERT INTO smpdb (
    profileID,
    username,
    password, 
    firstname,
    lastname ,
    email,
    createdAt,
    updatedAt,
    humanApis,
    status,
    phonenumber,
    phonevalidation,
    emailvalidation,
    role,
    source)
    VALUES (
    'rajjk5',
    'raj',
    'valraj123',
    'raj',
    'j k',
    'rajjk5@gmail.com',
    %s,
    %s,
    '[{"name":"raj","salary":650000,"married":true}]',
    true,
    '2387934723',
    False,
    False,
    array['manager', 'user'],
    641
    )
    """)


# cursor.execute(in_row_1, (datetime.datetime.now(), None))
# cursor.execute(in_row_2, (datetime.datetime.now(), None))
# cursor.execute(in_row_3, (datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days = 17)))
# cursor.execute(in_row_4, (datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days = 11)))
# cursor.execute(in_row_5, (datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days = 8)))
# cursor.execute(in_row_6, (datetime.datetime.now() - datetime.timedelta(days = 12), datetime.datetime.now()))

# cursor.execute("""CREATE INDEX ind_user
# ON smpdb (username);""")
# cursor.execute("""CREATE INDEX ind_stat
# ON smpdb (status);""")
# cursor.execute("""SELECT * FROM smpdb WHERE username LIKE 'ram%'""")
cursor.execute("""SELECT * FROM smpdb WHERE lastname=''""")
# cursor.execute("""SELECT * FROM smpdb WHERE status=true""")
# cursor.execute("""select * from smpdb WHERE updatedAt BETWEEN (createdAt + '10 days') AND (createdAt + '15 days')""")
rows = cursor.fetchall()

for row in rows:
    print(row)
    print('\n')

conn.commit()
cursor.close()
conn.close()
    

