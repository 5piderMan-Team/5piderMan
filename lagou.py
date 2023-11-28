import requests
from lxml import html
import pymysql
import time

jobs = []


class LagouJob:
    def __init__(self, position, place_city, place_area, salary, tag, require_education, require_experience,
                 company, company_status_industry, company_status_Financing_stage,
                 company_status_company_size, welfare):
        self.position = position
        self.tag = tag
        self.place_city = place_city
        self.place_area = place_area
        self.salary = salary
        self.require_education = require_education
        self.require_experience = require_experience
        self.company = company
        self.company_status_industry = company_status_industry
        self.company_status_Financing_stage = company_status_Financing_stage
        self.company_status_company_size = company_status_company_size
        self.welfare = welfare


def Send_Request(url, headers):
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
    companies_status = tree.xpath('//div[@class="industry__1HBkr"]')  # 数据服务｜咨询 / 未融资 / 50-150人
    # 领域
    tags_ = tree.xpath('//div[@class="ir___QwEG"]')  # C++科技金融  不同个数的span
    # 福利
    welfares_ = tree.xpath('//div[@class="il__3lk85"]')  # “年轻团队；发展前景；技术大牛带教”
    # 跳转链接
    # Todo
    # links_ = tree.xpath('')
    print("*")
    num_elements = len(positions_)
    print("num_elements:", num_elements)
    print("当前所在页面链接：", url)

    for i in range(num_elements):
        position_ = positions_[i].text_content()
        position = position_.split("[")[0]
        place = position_.split("[")[1].split("]")[0]
        place_city = place.split("·")[0]
        place_area = place.split("·")[1]
        salary = salarys_[i].text_content()

        require = requires_[i].strip()  # 去除多余的空格和换行符
        require_education = require.split(" / ")[1]
        require_experience = require.split(" / ")[0]

        company = companies_[i].text_content()
        try:
            company_status = companies_status[i].text_content()
            company_status_industry = company_status.split(" / ")[0]
            company_status_Financing_stage = company_status.split(" / ")[1]
            company_status_company_size = company_status.split(" / ")[2]
        except IndexError:
            company_status = "N/A"
            company_status_industry = "N/A"
            company_status_Financing_stage = "N/A"
            company_status_company_size = "N/A"
        tag = tags_[i].text_content()
        welfare = welfares_[i].text_content()
        print("职位:", position)
        print("城市:", place_city)
        print("区域:", place_area)
        print("薪资:", salary)
        print("标签", tag)
        print("学历要求:", require_education)
        print("经验要求:", require_experience)
        print("企业名称:", company)
        print("行业领域:", company_status_industry)
        print("融资阶段:", company_status_Financing_stage)
        print("公司规模:", company_status_company_size)
        print("福利待遇:", welfare)
        print("--------------------")
        job = LagouJob(position, place_city, place_area, salary,tag, require_education, require_experience,
                       company, company_status_industry, company_status_Financing_stage,
                       company_status_company_size, welfare)
        jobs.append(job)


def Connect_to_MySql():
    # 建立与 MySQL 数据库的连接
    DB_HOST = "??"  # 将 'IP1' 替换为实际的 IP1 地址
    DB_PORT = ??  # 如果端口号不是默认的 3306，请将其替换为实际的端口号
    DB_USER = ??
    DB_PASSWORD = ??
    DB_NAME = ??
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


def Save_to_MySql(cursor, conn, jobs):
    for job in jobs:
        # 编写插入数据的 SQL 语句
        sql = "INSERT INTO job (职位,城市,区域,薪资,标签,学历要求,经验要求,企业名称,行业领域,融资阶段, 公司规模,福利待遇) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 定义要插入的数据
        data = (job.position, job.place_city, job.place_area, job.salary,
                job.tag, job.require_education, job.require_experience,
                job.company, job.company_status_industry, job.company_status_Financing_stage,
                job.company_status_company_size, job.welfare)
        try:
            # 执行插入操作
            cursor.execute(sql, data)
            # 提交事务
            conn.commit()

        except Exception as e:
            # 发生错误时回滚事务
            conn.rollback()
            print("数据插入失败:", repr(e))

    print("当前页面数据插入成功！")


if __name__ == "__main__":
    base_url = "https://www.lagou.com/wn/zhaopin?fromSearch=true&kd="
    part = "&pn="
    # https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=  python   &pn=   1
    #  base_url + kd + part + page
    # 代理
    #  请求头
    headers = {
        'Connection': '??',
        'User-Agent': '??',

        'Cookie': '??',

        'Host': '??',
        'Referer': '??'

    }
    page = 1

    cursor, conn = Connect_to_MySql()

    kd = str(input("请输入你要查找的关键词："))
    while page <= 30:
        print("---" * 30)
        print("page:", page)
        print("---" * 30)
        url = base_url + kd + part + str(page)
        #
        page += 1
        content = Send_Request(url, headers)
        parse(content)
        Save_to_MySql(cursor, conn, jobs)
        jobs.clear()
    print("所有数据已成功导入！！！")
    cursor.close()
    conn.close()
