import React from "react";
import {Menu, Layout} from "antd";

const {Header} = Layout;
import SearchBar from "../SearchBar";

const items = [
    {
        key: "home",
        title: "首页",
        label: (
            <a href="/">首页</a>
        ),
    },
];

export default function Navbar() {
    return (
        <Header
            className="flex justify-between items-center bg-gray-800"
        >
            <div className="text-white text-xl">5piderMan</div>
            <div className="flex justify-between items-center">
                <Menu
                    className="bg-transparent"
                    theme="dark"
                    mode="horizontal"
                    items={items}
                />
                <SearchBar className="w-12"/>
            </div>
        </Header>
    )
}