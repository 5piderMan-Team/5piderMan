import React from "react";
import * as api from "../../backend/job";
import { Select, Table } from "antd";
import { Flex, Radio, Spin } from "antd";
import { useSearchParams } from "react-router-dom";

const columns = [
  {
    title: "岗位",
    dataIndex: "position",
    key: "position",
    width: "40%",
    ellipsis: true,
  },
  {
    title: "城市",
    dataIndex: "city",
    key: "city",
    width: "10%",
  },
  {
    title: "公司",
    dataIndex: "company_name",
    key: "company_name",
    width: "40%",
    ellipsis: true,
  },
  {
    title: "薪水",
    dataIndex: "salary",
    key: "salary",
    width: "10%",
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

// 主要用于获取屏幕宽度
const useViewport = () => {
  const [width, setWidth] = React.useState(window.innerWidth);

  React.useEffect(() => {
    const handleWindowResize = () => setWidth(window.innerWidth);
    window.addEventListener("resize", handleWindowResize);
    return () => window.removeEventListener("resize", handleWindowResize);
  }, []);

  return { width };
};

export default function JobList(prop) {
  const [dataSource, setDataSource] = React.useState([]);
  const [city, setCity] = React.useState("全国");
  const [spinning, setSpinning] = React.useState(true);
  const [searchParams, setSearchParams] = useSearchParams();

  React.useEffect(() => {
    const c = searchParams.get("city");
    console.log(c);
    let rc = city;
    if (c != "" && c != null) {
      setCity(c);
      rc = c;
    }

    setSpinning(true);
    api.getJobs(rc).then((data) => {
      let counter = 1;
      data.map((item) => {
        item.key = counter++;
        return item;
      });
      setDataSource(data);
      setSpinning(false);
    });
  }, [city]);

  const handleCityChange = (e) => {
    // console.log(e.target.value);
    setSearchParams({ city: e.target.value });
    setCity(e.target.value);
  };

  const handleCitySelect = (e) => {
    // console.log(e);
    setSearchParams({ city: e });
    setCity(e);
  };

  // 根据屏幕宽度，动态调整城市列表的显示
  const { width } = useViewport();
  const citySpilt = width / 100 - 2;
  const minCityList = cityList.slice(0, citySpilt);
  const lastCityList = cityList.slice(citySpilt);

  return (
    <Flex vertical className=" w-3/5 items-center mt-16 mb-16">
      <div className="flex w-full items-center justify-between">
        <div className=" text-sm font-bold mr-4">工作地点</div>
        <div>
          <Radio.Group value={city} defaultValue="全国">
            {minCityList.map((item) => (
              <Radio.Button value={item} key={item} onChange={handleCityChange}>
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

      <Spin wrapperClassName=" w-full" tip="Loading..." spinning={spinning}>
        <Table
          className="mt-4"
          dataSource={dataSource}
          columns={columns}
          {...prop}
        />
      </Spin>
    </Flex>
  );
}
