import random

import dynaconf
import pymysql


def show(data):
    # print("=========")
    # print(data)
    # print("=========")
    pass


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

cursor = connection.cursor()

cursor.execute("select * from job_lg")
rows = cursor.fetchall()
cursor.close()

results = []
for row in rows:
    show(row)
    row = row[1:]
    row = list(row)
    row[-2] = row[-2][1:-1]
    show(row)
    row = tuple(row)
    results.append(row)

print("处理完成，开始打乱：", len(results))

# 置乱result

random.shuffle(results)

print("shuffle done")

cursor = connection.cursor()
rc = cursor.executemany(
    "insert into jobs (position, city, area, salary, tag, education, experience, company_name, industry, financing_stage, company_size, welfare, category) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    results,
)

print("插入完成：", rc)
cursor.close()
connection.commit()
connection.close()
