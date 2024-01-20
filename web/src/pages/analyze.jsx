import { Layout } from "antd";

const { Content } = Layout;
import Charts from "../components/Charts/index.jsx";

function Analyze() {
  return (
    <Content className="min-h-screen">
      <Charts />
    </Content>
  );
}

export default Analyze;
