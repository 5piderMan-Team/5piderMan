import ReactECharts from 'echarts-for-react';
import {Col, Row} from "antd";
import React from "react";

const option = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
        }
    ]
};

function Chart() {
    return (
        <ReactECharts
            option={option}
            notMerge={true}
            lazyUpdate={true}
        />
    )
}

export default function Charts() {
    return (
        <div>
            <Row>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
            </Row>
            <Row>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
            </Row>
            <Row>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
                <Col span={8}>
                    <Chart/>
                </Col>
            </Row>
        </div>
    )
}
