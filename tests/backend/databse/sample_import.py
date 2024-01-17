import pymysql
import dynaconf

settings = dynaconf.Dynaconf(
    settings_files=".secrets.toml",  # 配置文件
)

# Connect to the database
connection = pymysql.connect(
    host=settings.db_host,
    user=settings.db_user,
    password=settings.db_password,
    database=settings.db_name,
)

with open("sample.sql") as f:
    dump = f.read()
    sqls = dump.split(";")
    cursor = connection.cursor()
    for sql in sqls:
        cursor.execute(sql)
        connection.commit()

cursor.close()
connection.close()
