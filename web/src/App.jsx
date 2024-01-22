import { Layout } from "antd";

import FooterWarp from "./components/FooterWarp";
import Navbar from "./components/Navbar";
import router from "./router";
import { RouterProvider } from "react-router-dom";
import AIAssistant from "./components/AIAssistant";

const App = () => {
  return (
    <Layout className="layout">
      <Navbar />
      <RouterProvider router={router} />
      <AIAssistant />
      <FooterWarp />
    </Layout>
  );
};

export default App;
