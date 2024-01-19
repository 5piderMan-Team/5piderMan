import React from "react";
import { Layout, theme } from "antd";

const { Content } = Layout;
import FooterWarp from "./components/FooterWarp";
import Navbar from "./components/Navbar";
import JobList from "./components/JobList/index.jsx";

const ContentWarp = () => {
  return (
    <Content className="flex items-center justify-center">
      <JobList className="w-3/5" />
    </Content>
  );
};

const App = () => {
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  return (
    <Layout className="layout">
      <Navbar />
      <ContentWarp />
      <FooterWarp />
    </Layout>
  );
};

export default App;
