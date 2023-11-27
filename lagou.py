import requests
from lxml import html
import random
import pymysql

def Send_Request(url, headers):
    # proxies = [
    #     {'http': '122.137.59.88:21871'},
    #     {'http': '120.41.143.120:16225'},
    #     {'http': '115.219.4.5:22784'},
    #     {'http': '121.232.97.190:19069'},
    #     {'http': '180.120.100.145:22018'},
    # ]
    #
    # proxy = random.choice(proxies)
    # proxies=proxy
    # print(proxy)
    response = requests.get(url=url, headers=headers, )
    response.encoding = 'utf-8'
    content = response.text
    return content


def parse(content):
    tree = html.fromstring(content)
    # 职位
    positions_ = tree.xpath('//div[@class="p-top__1F7CL"]')  # python数据开发工程师[上海·浦东新区]  中括号split
    # 薪资
    salarys_ = tree.xpath('//span[@class="money__3Lkgq"]')
    # 要求
    requires_ = tree.xpath('//div[@class="p-bom__JlNur"]/text()')
    # 企业
    companies_ = tree.xpath('//div[@class="company-name__2-SjF"]/a')
    # 企业大体状态   ---- Error : index out of range
    # companies_status = tree.xpath('//div[@class="industry__1HBkr"]')  # 数据服务｜咨询 / 未融资 / 50-150人
    # 领域
    areas_ = tree.xpath('//div[@class="ir___QwEG"]')  # C++科技金融  不同个数的span
    # 福利
    welfares_ = tree.xpath('//div[@class="il__3lk85"]')  # “年轻团队；发展前景；技术大牛带教”
    # 跳转链接
    # Todo
    # links_ = tree.xpath('')
    print("*")
    num_elements = len(positions_)
    for i in range(num_elements):
        position_ = positions_[i].text_content()
        position = position_.split("[")[0]
        place = position_.split("[")[1].split("]")[0]

        salary = salarys_[i].text_content()

        require = requires_[i].strip()  # 去除多余的空格和换行符
        require_education = require.split(" / ")[1]
        require_experience = require.split(" / ")[0]

        company = companies_[i].text_content()
        # company_status = companies_status[i].text_content()
        area = areas_[i].text_content()
        welfare = welfares_[i].text_content()

        print("Position:", position)
        print("Place:", place)
        print("Salary:", salary)
        print("Require_education:", require_education)
        print("Require_experience:", require_experience)
        print("Company:", company)
        # print("Company Status:", company_status)
        print("Work_Area:", area)
        print("Welfare:", welfare)
        print("--------------------")
        # 编写插入数据的 SQL 语句
        sql = "INSERT INTO lagou_py (职位,地点,薪资,学历要求,工作经验,企业名称,工作领域, 福利待遇) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        # 定义要插入的数据
        data = (position, place, salary, require_education,
                require_experience, company, area, welfare)

        try:
            # 执行插入操作
            cursor.execute(sql, data)

            # 提交事务
            conn.commit()

            print("数据插入成功！")

        except Exception as e:
            # 发生错误时回滚事务
            conn.rollback()
            print("数据插入失败:", repr(e))


if __name__ == "__main__":
    base_url = "https://www.lagou.com/wn/jobs?pn="
    end_url = "&fromSearch=true&kd=python"
    # https://www.lagou.com/wn/jobs?pn=1&fromSearch=true&kd=python
    # 代理

    #  请求头
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Cookie':
            'user_trace_token=20231120150143-552745f5-bc71-45f7-ad46-42ef37d893f3; _ga=GA1.2.1989561172.1700463706; _gid=GA1.2.1114739848.1700463706; LGUID=20231120150145-4944ce37-d4cc-4691-bfe8-8ef860940837; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; RECOMMEND_TIP=true; smidV2=20231120153850e4c5db4d2e1711e6546172c28121051c006e662ca7269af10; thirdDeviceIdInfo=%5B%7B%22channel%22%3A1%2C%22thirdDeviceId%22%3A%22WHJMrwNw1k/HviVRrpOSZpGlCFFBcMXPE94OvzT5YvGCDkOPESeWPJCK5af1q2vAi6ARdJpb4Ww1sgWkBQ2lHGKUIio68fjT9dCW1tldyDzmQI99+chXEihrPgjJ5dyOf9lCUKKcsmkTaFO8webhNijYmmmXo8LlTkQE5YcNLqNriNYPfoOP/bjt5qvm7vZPSFRRuSg/X1FURTkAd7H/eWn5w+ofbFZzHHFZ6Botq8RBm70zJmaGxgAUDic6AW2yIixSMW2OQhYo%3D1487582755342%22%7D%2C%7B%22channel%22%3A2%2C%22thirdDeviceId%22%3A%22140%23GmrDKHF5zzP0JQo23xoT4pN8s9xJEAe6rGkirFt6+7q5EgABvy8gCazTs5jMSZPX0VT2j3hqzznNnvmZri+zzXzdIamqlQzx2DD3VthqzFcm2O8+lpYazDrbV2QYomjzONdOHaU+PQbxPE2/4ioOJ0gwhVeCOMwgvj7oDwBn5lNo4f0ihho9PTY0W7ogxqgXSVRzHyNMQvLKZCj2+CahP5N2FSuqVvWoCod3QMzlmSEbMQOVwVrYIBEZzdwsOJY9IioGaC4vkWQQvNbWZ5nnl26Vv9X0+f4V7ykyNM4C5hWn5L2bNo4nRYlKa9bdZQYseiKde0qxx1W2dkEb9xWFGJHm+PHJEYvGGsLQ8x+joAtiJ5KhQS4GxqsovlKU/z4TDMKPw3en1YwsHOOVFLsV+qyN39Smbq5KFdoHmI4LHb+js2bI7f6wZJllb/QS5CXfe0Sz5gy4KycN218vGSY76NjacPOqEgzf6OgR2Zgp958Ex8RHJn/rI4ICzwPxEzKLB681QJzQ9CEFCPFFLVyCzlIqmmTD62HnxFgiv9484gw+pnpZ91CkoV9dnf8VSwhzOsvapBpc2R9liFqoasF1CRb/ydxLEUAkHwDNWm732+o8+ftHOujsGknOVmNSu8kcn2j7BG/QCU+Ilg7gdtMH3tOHSseMy729pj61Cw5LVu/F//AMemrgqlpio3uZqgnBQPaKVRNShICGmKc3LescZEYpYWXNx2lVs/NMfkbgO86zPcdILodzK5UQMKyzHnMmty49raPfisvOZCtN31a57oFyD/jnFCd7WSfw0uBTR6EeS4nk6aefP0SgYzX9n6O0ThP5Bk3wq0GkhPW4rTAN/y/BZfhGaJLcShobwjarzKHS7F1c5icZsas+/PIx7OqE7qY6bFSEs1oT29mIeKhbNcgXHkwV/6PYq4PyDkZs5onvDPf23flooDq9s8yAxrsSitAPh0sGusLuO6a2Zj5755z0XZE04ttGbJKTRXTL7S9xYsFOTF2Yw7L957GbW/AmC1srhot2TV0ccFmgdwVVX4BAMu3CnyzKAG8tuzHSh8H93sXp4/NKFD5SOZh9lmi993NkO8vPiKF%3D%2Cundefined%22%7D%5D; user-finger=dfd5c59f62f0c079f6a3dc3aecd8e9f4; gate_login_token=v1####7df99fde56d345fd51ae249982d46aafdaf91b9253b049be46b2d806dce1f071; JSESSIONID=ABAAABAABEIABCI3B5C4A95714AD1619278D4C837AC65AF; WEBTJ-ID=20231122161013-18bf614646310b0-0928d061420f32-26031051-1327104-18bf6146464108e; _gat=1; _putrc=46B70532ADE34A1B123F89F2B170EADC; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1700463706,1700485615,1700558150,1700640614; login=true; unick=%E7%99%BD%E5%BC%80%E6%B0%B4; __SAFETY_CLOSE_TIME__25298088=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1700640616; LGSID=20231122161015-8c262eef-ffbd-483e-b7d4-9f5f2ac3c84d; PRE_UTM=pc_top_jljx_1; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fwn%2FresumeRefinement%3Futm%5Fsource%3Dpc%5Ftop%5Fjljx%5F1; _ga_DDLTLJDLHH=GS1.2.1700640615.4.1.1700640616.59.0.0; TG-TRACK-CODE=index_search; __lg_stoken__=24e3dbb17367126a2748360270bb62f44ae2d9aedb6afca46d471674a81a659fecb500649a045324842e56c2ac444166941161dd51dd3ef0bd52cce65053b9dfac83b6b6c4d0; LGRID=20231122161023-d30c2d9e-3459-4ac7-8e72-43e0c8f6d3f9; X_HTTP_TOKEN=02a93c3e3c1228f82611460071c562b9e81304af74; X_MIDDLE_TOKEN=6de4cc58adbbb183f2c829f1355adc06; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2225298088%22%2C%22%24device_id%22%3A%2218beb88fdb81f7-06f4f66cff8dca-26031051-1327104-18beb88fdb9c82%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_campaign%22%3A%22distribution%22%2C%22%24latest_utm_source%22%3A%22pc_top_jljx_1%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22119.0.0.0%22%7D%2C%22first_id%22%3A%2218beb88fdb81f7-06f4f66cff8dca-26031051-1327104-18beb88fdb9c82%22%7D',
        'Host': 'www.lagou.com',
        'Referer':
            'https: // www.lagou.com / utrack / trackMid.html?'
    }
    page = 1
    DB_HOST = '？？'  # 将 'IP1' 替换为实际的 IP1 地址
    DB_PORT = 3306  # 如果端口号不是默认的 3306，请将其替换为实际的端口号
    DB_USER = '？？'
    DB_PASSWORD = '？？'
    DB_NAME = 'lagou'

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

    while page <= 30:
        print("---" * 30)
        print("page:", page)
        print("---" * 30)
        url = base_url + str(page) + end_url
        page += 1
        content = Send_Request(url, headers)
        parse(content)
    print("所有数据已成功导入！！！")
    cursor.close()
    conn.close()
