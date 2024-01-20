import { useRouteError } from "react-router-dom";
import { Button, Result } from "antd";

const Page404 = () => {
  const handleClick = () => {
    window.location.href = "/";
  };

  return (
    <Result
      className="min-h-screen"
      status="404"
      title="404"
      subTitle="Sorry, the page you visited does not exist."
      extra={
        <Button type="primary" onClick={handleClick}>
          回到首页
        </Button>
      }
    />
  );
};

export default function ErrorPage() {
  const error = useRouteError();
  console.error(error);

  return <Page404 />;
}
