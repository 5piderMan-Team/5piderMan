import * as echarts from "echarts/core";
import { LegendComponent } from "echarts/components";
import { PieChart } from "echarts/charts";
import { LabelLayout } from "echarts/features";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropTypes from "prop-types";

echarts.use([LegendComponent, PieChart, CanvasRenderer, LabelLayout]);

const optionSample = {
  legend: {
    top: "5%",
    left: "center",
    // doesn't perfectly work with our tricks, disable it
    selectedMode: false,
  },
  series: [
    {
      name: "Access From",
      type: "pie",
      radius: ["40%", "70%"],
      center: ["50%", "70%"],
      // adjust the start angle
      startAngle: 180,
      label: {
        show: true,
        formatter(param) {
          // correct the percentage
          return param.name + " (" + param.percent * 2 + "%)";
        },
      },
      data: [
        { value: 1048, name: "Search Engine" },
        { value: 735, name: "Direct" },
        { value: 580, name: "Email" },
        { value: 484, name: "Union Ads" },
        { value: 300, name: "Video Ads" },
        {
          // make an record to fill the bottom 50%
          value: 1048 + 735 + 580 + 484 + 300,
          itemStyle: {
            // stop the chart from rendering this piece
            color: "none",
            decal: {
              symbol: "none",
            },
          },
          label: {
            show: false,
          },
        },
      ],
    },
  ],
};

export default function HalfPieChart({ items, data, onChartReady, ...props }) {
  if (data.length === 0) {
    return <div className="h-64"></div>;
  }

  let option = optionSample;
  const chartdata = [];
  let sum = 0;
  for (let i = 0; i < items.length; i++) {
    chartdata.push({ value: data[i], name: items[i] });
    sum += data[i];
  }
  chartdata.push({
    // make an record to fill the bottom 50%
    value: sum,
    itemStyle: {
      // stop the chart from rendering this piece
      color: "none",
      decal: {
        symbol: "none",
      },
    },
    label: {
      show: false,
    },
  });
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

HalfPieChart.propTypes = {
  items: PropTypes.array.isRequired,
  data: PropTypes.array.isRequired,
  onChartReady: PropTypes.func.isRequired,
};
