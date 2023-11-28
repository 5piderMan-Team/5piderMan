import requests
from lxml import html
from config import LagouJob, jobs


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
        print("标签:", tag)
        print("学历要求:", require_education)
        print("经验要求:", require_experience)
        print("企业名称:", company)
        print("行业领域:", company_status_industry)
        print("融资阶段:", company_status_Financing_stage)
        print("公司规模:", company_status_company_size)
        print("福利待遇:", welfare)
        print("--------------------")
        job = LagouJob(position, place_city, place_area, salary, tag, require_education, require_experience,
                       company, company_status_industry, company_status_Financing_stage,
                       company_status_company_size, welfare)
        jobs.append(job)
