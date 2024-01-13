import requests
from lxml import html
import random
import pymysql
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options


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
    # driver = webdriver.Chrome()
    # driver.get(url)
    # # 点击跳转链接
    # link_element = driver.find_element_by_css_selector(".position_link")
    # link_element.click()
    # # 切换到新打开的窗口
    # driver.switch_to.window(driver.window_handles[1])
    # # 获取跳转窗口的URL
    # new_window_url = driver.current_url
    # print(new_window_url)
    # driver.quit()

    # 创建 ChromeOptions 对象
    edge_options = Options()
    # 启用无头模式
    edge_options.add_argument("--headless")
    # 创建 Chrome\edge WebDriver，并将 ChromeOptions\edgeoptions 传递给它
    driver = webdriver.Edge(options=edge_options)
    # 在后续的代码中继续使用 driver 进行其他操作
    driver.get(url)
    # 获取页面总高度
    total_height = driver.execute_script("return document.body.scrollHeight")
    print("当前所在页面链接：", url)
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

        link =
        print("Position:", position)
        print("Place:", place)
        print("Salary:", salary)
        print("Require_education:", require_education)
        print("Require_experience:", require_experience)
        print("Company:", company)
        # print("Company Status:", company_status)
        print("Work_Area:", area)
        print("Welfare:", welfare)
        print("Link to Details page:", link)
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
    base_url = "https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=python&pn="
    # https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=python&city=%E5%85%A8%E5%9B%BD
    # https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=python&pn=2
    # https://www.lagou.com/wn/jobs?pn=1&fromSearch=true&kd=python
    # 代理

    #  请求头
    headers = {
        'Connection': 'keep - alive',
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Cookie':
            'index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAAECABIEACCAC38D6783CABF5DF6FF7FAE780C74AD58; WEBTJ-ID=20231126171526-18c0ae9882fe94-0c498a8dcb75cc-15373079-1327104-18c0ae98830100f; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218c0ae989a3af9-00b2d2f349f16b-15373079-1327104-18c0ae989a4e03%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22102.0.5005.63%22%7D%2C%22%24device_id%22%3A%2218c0ae989a3af9-00b2d2f349f16b-15373079-1327104-18c0ae989a4e03%22%7D',
        'Host': 'www.lagou.com',
        'Referer':
            'https://www.lagou.com/wn/'
    }
    page = 1
    DB_HOST = '??'  # 将 'IP1' 替换为实际的 IP1 地址
    DB_PORT = '??'  # 如果端口号不是默认的 3306，请将其替换为实际的端口号
    DB_USER = '??'
    DB_PASSWORD = '??'
    DB_NAME = '??'

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
        url = base_url + str(page)
        page += 1
        content = Send_Request(url, headers)
        parse(content)
    print("所有数据已成功导入！！！")
    cursor.close()
    conn.close()
