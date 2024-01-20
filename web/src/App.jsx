import { Layout } from "antd";

import FooterWarp from "./components/FooterWarp";
import Navbar from "./components/Navbar";
import router from "./router";
import { RouterProvider } from "react-router-dom";

const App = () => {
  // const {
  //   token: { colorBgContainer },
  // } = theme.useToken();
  return (
    <Layout className="layout">
      <Navbar />
      <RouterProvider router={router} />
      <FooterWarp />
    </Layout>
  );
};

export default App;
