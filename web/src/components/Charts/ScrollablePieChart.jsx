import * as echarts from "echarts/core";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { PieChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  PieChart,
  CanvasRenderer,
  LabelLayout,
]);

let optionSample = {
  //   title: {
  //     text: "同名数量统计",
  //     subtext: "纯属虚构",
  //     left: "center",
  //   },
  legend: {
    type: "scroll",
    orient: "vertical",
    right: 10,
    top: 10,
    bottom: 20,
    data: [
      "rose1",
      "rose2",
      "rose3",
      "rose4",
      "rose5",
      "rose6",
      "rose7",
      "rose8",
    ],
  },
  series: [
    {
      name: "姓名",
      type: "pie",
      radius: "55%",
      center: ["40%", "50%"],
      data: [
        { value: 335, name: "rose1" },
        { value: 310, name: "rose2" },
        { value: 274, name: "rose3" },
        { value: 235, name: "rose4" },
        { value: 400, name: "rose5" },
        { value: 335, name: "rose6" },
        { value: 310, name: "rose7" },
        { value: 274, name: "rose8" },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: "rgba(0, 0, 0, 0.5)",
        },
      },
    },
  ],
};

export default function ScrollablePieChart({
  items,
  data,
  onChartReady,
  ...props
}) {
  if (data.length === 0) {
    return <div className="h-64"></div>;
  }
  let option = optionSample;

  const chartdata = [];
  for (let i = 0; i < items.length; i++) {
    chartdata.push({ value: data[i], name: items[i] });
  }
  option.series[0].data = chartdata;
  option.legend.data = items;
  return (
    <EChartsReactCore
      echarts={echarts}
      option={option}
      onChartReady={onChartReady}
      {...props}
    />
  );
}

ScrollablePieChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
