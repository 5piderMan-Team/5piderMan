import React from "react";
import * as api from "../../backend/job";
import { Table } from "antd";

const columns = [
  {
    title: "岗位",
    dataIndex: "position",
    key: "position",
  },
  {
    title: "城市",
    dataIndex: "city",
    key: "city",
  },
  {
    title: "公司",
    dataIndex: "company_name",
    key: "company_name",
  },
  {
    title: "薪水",
    dataIndex: "salary",
    key: "salary",
  },
];

export default function JobList(prop) {
  const [dataSource, setDataSource] = React.useState([]);

  React.useEffect(() => {
    api.getJobs().then((data) => {
      let counter = 1;
      data.map((item) => {
        item.key = counter++;
        return item;
      });
      setDataSource(data);
    });
  }, []);

  return (
    <>
      <Table dataSource={dataSource} columns={columns} {...prop} />
    </>
  );
}
