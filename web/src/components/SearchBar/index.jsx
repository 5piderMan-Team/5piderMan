import React from 'react';
import {Input} from 'antd';

const {Search} = Input;

const onSearch = (value, _e, info) => console.log(info?.source, value);

export default function SearchBar() {
    return (
        <Search
            placeholder="输入以搜索岗位"
            onSearch={onSearch}
        />
    );
}