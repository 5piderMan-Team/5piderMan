import { createBrowserRouter } from "react-router-dom";
import ErrorPage from "./err-page.jsx";
import Index from "./pages/index.jsx";
import Analyze from "./pages/analyze.jsx";
import SearchPage from "./pages/search.jsx";

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
  {
    path: "/search",
    element: <SearchPage />,
    errorElement: <ErrorPage />,
  },
]);

export default router;
