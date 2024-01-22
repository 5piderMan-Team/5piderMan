import * as echarts from "echarts/core";
import { TitleComponent, ToolboxComponent } from "echarts/components";
import { PieChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([
  TitleComponent,
  ToolboxComponent,
  PieChart,
  CanvasRenderer,
  LabelLayout,
]);

let optionSample = {
  //   title: {
  //     text: "Nightingale Chart",
  //     subtext: "Fake Data",
  //     left: "center",
  //   },
  // toolbox: {
  //   show: true,
  //   feature: {
  //     mark: { show: true },
  //     // dataView: { show: true, readOnly: false },
  //     // restore: { show: true },
  //     // saveAsImage: { show: true },
  //   },
  // },
  label: {
    show: true,
    formatter(param) {
      // correct the percentage
      return param.name + " (" + param.percent * 2 + "%)";
    },
  },
  series: [
    {
      name: "Area Mode",
      type: "pie",
      radius: [20, 140],
      roseType: "area",
      itemStyle: {
        borderRadius: 5,
      },
      data: [
        { value: 30, name: "rose 1" },
        { value: 28, name: "rose 2" },
        { value: 26, name: "rose 3" },
        { value: 24, name: "rose 4" },
        { value: 22, name: "rose 5" },
        { value: 20, name: "rose 6" },
        { value: 18, name: "rose 7" },
        { value: 16, name: "rose 8" },
      ],
    },
  ],
};

export default function NightingaleChart({
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
  //   console.log(chartdata);
  return (
    <EChartsReactCore
      echarts={echarts}
      option={option}
      onChartReady={onChartReady}
      {...props}
    />
  );
}

NightingaleChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
