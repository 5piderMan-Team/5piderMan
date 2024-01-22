import * as echarts from "echarts/core";
import { PieChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([PieChart, CanvasRenderer, LabelLayout]);

const optionSample = {
  series: [
    {
      type: "pie",
      radius: "25%",
      center: ["50%", "50%"],
      data: [],
      label: {
        position: "outer",
        alignTo: "edge",
        // edgeDistance: "25%",
      },
      left: 0,
      right: 0,
      top: 0,
      bottom: 0,
    },
  ],
};

export default function BasicPieChart({ items, data, onChartReady, ...props }) {
  if (data.length === 0) {
    return <div className="h-64"></div>;
  }

  console.log(items);
  let option = optionSample;
  const chartdata = [];
  for (let i = 0; i < items.length; i++) {
    chartdata.push({ value: data[i], name: items[i] });
  }
  option.series[0].data = chartdata;

  return (
    <EChartsReactCore
      echarts={echarts}
      option={option}
      onChartReady={onChartReady}
      {...props}
    />
  );
}

BasicPieChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
