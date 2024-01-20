import { Layout } from "antd";

const { Content } = Layout;
import JobList from "../components/JobList/index.jsx";

const Index = () => {
  return (
    <Content className="flex items-center justify-center">
      <JobList />
    </Content>
  );
};

export default Index;
