import * as echarts from "echarts/core";
import { TreemapChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([TreemapChart, CanvasRenderer]);

const optionSample = {
  series: [
    {
      type: "treemap",
      breadcrumb: false,
      data: [
        {
          name: "nodeA",
          value: 10,
        },
        {
          name: "nodeB",
          value: 20,
        },
        {
          name: "nodeA",
          value: 10,
        },
        {
          name: "nodeB",
          value: 20,
        },
      ],
    },
  ],
};

export default function TreeMapChart({ items, data, onChartReady, ...props }) {
  if (data.length === 0) {
    return <div className="h-64"></div>;
  }

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

TreeMapChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
