import { createBrowserRouter } from "react-router-dom";
import ErrorPage from "./err-page.jsx";
import Index from "./pages/index.jsx";
import Analyze from "./pages/analyze.jsx";
import SearchPage from "./pages/search.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Index />,
  },
  {
    path: "/analyze",
    element: <Analyze />,
  },
  {
    path: "/search",
    element: <SearchPage />,
  },
  {
    path: "*",
    element: <ErrorPage />,
  },
]);

export default router;
