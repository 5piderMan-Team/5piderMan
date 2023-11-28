import pymysql
from config import DB_HOST, DB_NAME, DB_USER, DB_PORT, DB_PASSWORD


def Connect_to_MySql():
    # 建立与 MySQL 数据库的连接
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    # 创建游标对象
    cursor = conn.cursor()
    return cursor, conn
