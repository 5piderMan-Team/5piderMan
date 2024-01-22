import * as echarts from "echarts/core";
import {
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { FunnelChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  LegendComponent,
  FunnelChart,
  CanvasRenderer,
]);

const optionSample = {
  // toolbox: {
  //   feature: {
  //     dataView: { readOnly: false },
  //     restore: {},
  //     saveAsImage: {},
  //   },
  // },
  legend: {
    data: ["Show", "Click", "Visit", "Inquiry", "Order"],
  },
  series: [
    {
      name: "Funnel",
      type: "funnel",
      left: "10%",
      top: 60,
      bottom: 60,
      width: "80%",
      min: 0,
      minSize: "5%",
      maxSize: "100%",
      sort: "ascending",
      gap: 2,
      label: {
        show: true,
        position: "inside",
      },
      labelLine: {
        length: 10,
        lineStyle: {
          width: 1,
          type: "solid",
        },
      },
      itemStyle: {
        borderColor: "#fff",
        borderWidth: 1,
      },
      emphasis: {
        label: {
          fontSize: 20,
        },
      },
      data: [
        { value: 600, name: "Visit" },
        { value: 400, name: "Inquiry" },
        { value: 20, name: "Order" },
        { value: 80, name: "Click" },
        { value: 100, name: "Show" },
      ],
    },
  ],
};

export default function PyramidChart({ items, data, onChartReady, ...props }) {
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

FunnelChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
