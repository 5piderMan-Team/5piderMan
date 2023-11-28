from config import jobs, base_url, part_url, headers
from connect import Connect_to_MySql
from data_parse import Send_Request, parse
from save import Save_to_MySql

if __name__ == "__main__":
    page = 1

    cursor, conn = Connect_to_MySql()

    kd = str(input("请输入你要查找的关键词："))
    while page <= 30:
        url = base_url + kd + part_url + str(page)
        print("---" * 30)
        print("page:", page)
        print("当前所在页面链接：", url)
        print("---" * 30)
        page += 1
        content = Send_Request(url, headers)
        parse(content)
        Save_to_MySql(cursor, conn, jobs)
        jobs.clear()
    print("所有数据已成功导入！！！")
    cursor.close()
    conn.close()
