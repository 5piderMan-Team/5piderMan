import { Menu, Layout } from "antd";

const { Header } = Layout;
import SearchBar from "../SearchBar";

const items = [
  {
    key: "home",
    title: "首页",
    label: <a href="/">首页</a>,
  },
  {
    key: "analyze",
    title: "数据分析",
    label: <a href="/analyze">数据分析</a>,
  },
];

export default function Navbar() {
  return (
    <Header className=" flex justify-between items-center bg-gray-800">
      <div className="flex w-1/2 items-center">
        <div className="text-white text-xl">5piderMan</div>
        <Menu
          className="bg-transparent w-96"
          theme="dark"
          mode="horizontal"
          items={items}
        />
      </div>
      <div className="flex w-1/2 items-center justify-end">
        <SearchBar className="w-fit" />
      </div>
    </Header>
  );
}
