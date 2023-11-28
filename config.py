# 数据库
DB_HOST = ??  # 将 'IP1' 替换为实际的 IP1 地址
DB_PORT = ??  # 如果端口号不是默认的 3306，请将其替换为实际的端口号
DB_USER = ??
DB_PASSWORD = ??
DB_NAME = ??

# 请求资源
base_url = "https://www.lagou.com/wn/zhaopin?fromSearch=true&kd="
part_url = "&pn="
headers = {
    'Connection': '??',
    'User-Agent':
        '??',
    'Cookie':
        '??',
    'Host': '??',
    'Referer':
        '??'
}

# 存储
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
