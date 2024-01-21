import * as echarts from "echarts/core";
import { TooltipComponent, LegendComponent } from "echarts/components";
import { PieChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";

echarts.use([
  TooltipComponent,
  LegendComponent,
  PieChart,
  CanvasRenderer,
  LabelLayout,
]);

const optionSample = {
  tooltip: {
    trigger: "item",
  },
  // 图例位置
  legend: {
    top: "5%",
    left: "center",
  },
  series: [
    {
      name: "Access From",
      type: "pie",
      radius: ["40%", "70%"],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: "#fff",
        borderWidth: 2,
      },
      label: {
        show: false,
        position: "center",
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: "bold",
        },
      },
      labelLine: {
        show: false,
      },
      data: [
        { value: 1048, name: "Search Engine" },
        { value: 735, name: "Direct" },
        { value: 580, name: "Email" },
        { value: 484, name: "Union Ads" },
        { value: 300, name: "Video Ads" },
      ],
    },
  ],
};

export default function DoughnutChart({ items, data, onChartReady, ...props }) {
  if (items.length === 0) {
    return <div className="h-64"></div>;
  }

  let option = optionSample;

  const chartdata = [];
  for (let i = 0; i < items.length; i++) {
    chartdata.push({ value: data[i], name: items[i] });
  }
  option.series[0].data = chartdata;
  console.log(chartdata);
  return (
    <EChartsReactCore
      echarts={echarts}
      option={option}
      onChartReady={onChartReady}
      {...props}
    />
  );
}
