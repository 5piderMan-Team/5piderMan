import React from 'react';
import {Layout, theme} from 'antd';

const {Content} = Layout;
import FooterWarp from "./components/FooterWarp";
import Navbar from "./components/Navbar";
import Charts from "./chart.jsx";

const ContentWarp = () => {
    return (
        <Content className="min-h-screen">
            <Charts/>
        </Content>
    )
};

const App = () => {
    const {
        token: {colorBgContainer},
    } = theme.useToken();
    return (
        <Layout className="layout">
            <Navbar/>
            <ContentWarp/>
            <FooterWarp/>
        </Layout>
    );
};

export default App;