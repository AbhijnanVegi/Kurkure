import pymysql
import pymysql.cursors

con = pymysql.connect(host='localhost',
                        user='root',
                        password='password',
                        db='db',
                        cursorclass= pymysql.cursors.DictCursor
                    )
cur = con.cursor()