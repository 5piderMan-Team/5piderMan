def Save_to_MySql(cursor, conn, jobs):
    for job in jobs:
        # 编写插入数据的 SQL 语句
        sql = "INSERT INTO job (职位,城市,区域,薪资,标签,学历要求,经验要求,企业名称,行业领域,融资阶段, 公司规模,福利待遇) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 定义要插入的数据
        data = (job.position, job.place_city, job.place_area, job.salary, job.tag,
                job.require_education, job.require_experience,
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
