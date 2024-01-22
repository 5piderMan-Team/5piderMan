import { Input } from "antd";

const { Search } = Input;
import PropTypes from "prop-types";

export default function SearchBar({ onSearch, ...prop }) {
  return <Search placeholder="输入以搜索岗位" onSearch={onSearch} {...prop} />;
}

SearchBar.propTypes = {
  onSearch: PropTypes.func,
};
