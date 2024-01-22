import { Layout } from "antd";

const { Content } = Layout;
import { Input } from "antd";
const { Search } = Input;
import { Table } from "antd";
import { useState } from "react";
import * as Api from "../backend/job";
import router from "../router";

const SearchPage = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const onSearch = (value) => {
    setLoading(true);
    router.navigate(`/search?keyword=${value}`);
    Api.searchJobs(value).then((data) => {
      let counter = 1;
      data.map((item) => {
        item.key = counter++;
        return item;
      });
      setResult(data);
      setLoading(false);
    });
  };

  return (
    <Content className=" min-h-screen">
      <div className="flex flex-col items-center justify-center m-16">
        <div className="text-3xl font-bold mb-4">搜索</div>
        <Search
          className=" w-96"
          placeholder="input search text"
          enterButton="Search"
          size="large"
          loading={loading}
          onSearch={onSearch}
        />
        {result && (
          <Table
            className="w-1/2 mt-8"
            dataSource={result}
            columns={[
              {
                title: "岗位",
                dataIndex: "position",
                key: "position",
                width: "30%",
                ellipsis: true,
              },
              {
                title: "城市",
                dataIndex: "city",
                key: "city",
                width: "20%",
              },
              {
                title: "公司",
                dataIndex: "company_name",
                key: "company_name",
                width: "30%",
                ellipsis: true,
              },
              {
                title: "薪水",
                dataIndex: "salary",
                key: "salary",
                width: "20%",
              },
            ]}
          />
        )}
      </div>
    </Content>
  );
};

export default SearchPage;
