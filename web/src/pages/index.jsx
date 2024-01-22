import { Layout } from "antd";

const { Content } = Layout;
import JobList from "../components/JobList/index.jsx";

const Index = () => {
  return (
    <Content className="min-h-screen flex justify-center">
      <JobList />
    </Content>
  );
};

export default Index;
