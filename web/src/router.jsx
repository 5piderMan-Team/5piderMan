import { createBrowserRouter } from "react-router-dom";
import ErrorPage from "./err-page.jsx";
import Index from "./pages/index.jsx";
import Analyze from "./pages/analyze.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Index />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/analyze",
    element: <Analyze />,
    errorElement: <ErrorPage />,
  },
]);

export default router;
