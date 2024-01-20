import React from "react";
import * as api from "../../backend/job";
import { Select, Table } from "antd";
import { Flex, Radio } from "antd";

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

const cityList = [
  "全国",
  "北京",
  "深圳",
  "上海",
  "广州",
  "成都",
  "杭州",
  "武汉",
  "苏州",
  "南京",
  "西安",
  "长沙",
  "东莞",
  "重庆",
  "佛山",
  "无锡",
  "合肥",
  "宁波",
  "郑州",
  "珠海",
  "常州",
  "嘉兴",
  "中山",
  "大连",
  "厦门",
  "天津",
  "惠州",
  "福州",
  "济南",
  "青岛",
  "昆明",
  "南昌",
  "长春",
  "南通",
  "贵阳",
  "沈阳",
  "南宁",
  "温州",
  "湖州",
];

export default function JobList(prop) {
  const [dataSource, setDataSource] = React.useState([]);
  const [city, setCity] = React.useState("全国");

  React.useEffect(() => {
    api.getJobs(city).then((data) => {
      let counter = 1;
      data.map((item) => {
        item.key = counter++;
        return item;
      });
      setDataSource(data);
    });
  }, [city]);

  const handleCityChange = (e) => {
    console.log(e.target.value);
    setCity(e.target.value);
  };

  const handleCitySelect = (e) => {
    console.log(e);
    setCity(e);
  };

  const citySpilt = 11;
  const minCityList = cityList.slice(0, citySpilt);
  const lastCityList = cityList.slice(citySpilt);

  return (
    <>
      <Flex vertical className=" w-3/5 items-center mt-16 mb-16">
        <div className="flex w-full items-center justify-between">
          <div className=" text-sm font-bold mr-4">工作地点</div>
          <div>
            <Radio.Group value={city} defaultValue="全国">
              {minCityList.map((item) => (
                <Radio.Button
                  value={item}
                  key={item}
                  onChange={handleCityChange}
                >
                  {item}
                </Radio.Button>
              ))}
            </Radio.Group>
            <Select
              className=" w-18"
              placeholder="更多"
              placement={city}
              onChange={handleCitySelect}
            >
              {lastCityList.map((item) => (
                <Select.Option value={item} key={item}>
                  {item}
                </Select.Option>
              ))}
            </Select>
          </div>
        </div>

        <Table
          className=" mt-4 w-full"
          dataSource={dataSource}
          columns={columns}
          {...prop}
        />
      </Flex>
    </>
  );
}
