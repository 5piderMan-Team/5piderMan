from sqlalchemy.orm import Session

from . import dao


def get_jobs(city_limit: str | None, session: Session):
    if city_limit == "全国" or city_limit is None:
        return dao.get(session)
    return dao.existed_select(session, "city", city_limit)


def get_count_by_list(session: Session, pattern: list[str]) -> dict[str, int]:
    result = []
    for p in pattern:
        result.append((p, dao.filter_count(session, "position", p)))

    result = sorted(result, key=lambda x: x[1], reverse=True)
    return dict(result)


def get_city_analysis(session: Session) -> dict[str, int]:
    data = dao.group_count(session, "city")
    data = sorted(data.items(), lambda x: x[1], reverse=True)
    return dict(data[:20])


def get_education_analysis(session: Session) -> dict[str, int]:
    data = dao.group_count(session, "education")
    data = sorted(data.items(), lambda x: x[1], reverse=True)
    return data


def get_position_analysis(session: Session) -> dict[str, int]:
    position = [
        "算法工程师",
        "前端",
        "前端开发",
        "C++",
        "Java",
        "测试工程师",
        "嵌入式",
        "硬件",
        "Python",
        "架构师",
        "项目经理",
        "web",
        "自动化",
        ".NET",
        "PHP",
        "测试开发",
        "Go",
        "Android",
        "iOS",
        "实施工程师",
        "项目助理",
        "系统工程师",
        "网络工程师",
        "DBA",
        "售后工程师",
        "网络安全",
        "后端开发",
        "售前工程师",
        "系统集成",
        "单片机",
        "U3D",
        "驱动开发",
        "区块链",
        "射频工程师",
        "全栈工程师",
        "机器学习",
        "自动化测试",
        "搜索算法",
        "C#",
        "运维开发工程师",
        "自然语言处理",
        "数据挖掘",
        "ETL",
        "Node.js",
        "机器视觉",
        "Oracle",
        "数据仓库",
        "硬件测试",
        "运维经理",
        "技术经理",
        "IDC",
        "系统管理员",
        "深度学习",
        "硬件开发",
        "性能测试",
        "CDN",
        "图像处理",
        "电路设计",
        "MySQL",
        "技术总监",
        "游戏测试",
        "图像识别",
        "BI工程师",
        "COCOS2D-X",
        "白盒测试",
        "测试经理",
        "ASP",
        "运维总监",
        "Ruby",
        "系统安全",
    ]
    return get_count_by_list(session, position)


def get_language_analysis(session: Session) -> dict[str, int]:
    language = [
        "C++",
        "Java",
        "Python",
        "PHP",
        "Go",
        "JS",
        "C#",
        "Ruby",
        "Scala",
    ]
    return get_count_by_list(session, language)


def get_salary_analysis(session: Session):
    salary_data = dao.group_count(session, "salary")
    histogram = dict()
    for k, v in salary_data.items():
        index = int(k.replace("k", "").split("-")[0])
        if index not in histogram.keys():
            histogram[index] = v
        else:
            histogram[index] += v
    return {str(k) + "k": v for k, v in histogram.items()}


def get_company_analysis(session: Session):
    data = dao.group_count(session, "company_name")
    data = sorted(data.items(), key=lambda it: it[1], reverse=True)
    return dict(data[:10])


def get_category_analysis(session: Session):
    data = dao.group_count(session, "category")
    data = sorted(data.items(), key=lambda it: it[1], reverse=True)
    return dict(data[:10])


def get_experience_analysis(session: Session):
    data = dao.group_count(session, "experience")
    resp = dict()
    for k, v in data.items():
        index = k.replace("经验", "")
        resp[index] = v
    return {k: v for k, v in resp.items()}


def job_search(keyword: str, session: Session):
    return dao.search(session, keyword)
