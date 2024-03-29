import * as echarts from "echarts/core";
import {
  TitleComponent,
  GridComponent,
  DataZoomComponent,
} from "echarts/components";
import { BarChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import EChartsReactCore from "echarts-for-react/lib/core";
import PropsTypes from "prop-types";

echarts.use([
  TitleComponent,
  GridComponent,
  DataZoomComponent,
  BarChart,
  CanvasRenderer,
]);

// prettier-ignore
let dataAxis = ['点', '击', '柱', '子', '或', '者', '两', '指', '在', '触', '屏', '上', '滑', '动', '能', '够', '自', '动', '缩', '放'];
// prettier-ignore
let data = [220, 182, 191, 234, 290, 330, 310, 123, 442, 321, 90, 149, 210, 122, 133, 334, 198, 123, 125, 220];

const optionSample = {
  // title: {
  //   text: "特性示例：渐变色 阴影 点击缩放",
  //   subtext: "Feature Sample: Gradient Color, Shadow, Click Zoom",
  // },
  xAxis: {
    data: dataAxis,
    axisLabel: {
      // inside: true,
      color: "#000",
      fontSize: 8,
    },
    axisTick: {
      show: false,
    },
    axisLine: {
      show: false,
    },
    z: 10,
  },
  yAxis: {
    axisLine: {
      show: false,
    },
    axisTick: {
      show: false,
    },
    axisLabel: {
      color: "#999",
    },
  },
  dataZoom: [
    {
      type: "inside",
    },
  ],
  series: [
    {
      type: "bar",
      showBackground: true,
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: "#83bff6" },
          { offset: 0.5, color: "#188df0" },
          { offset: 1, color: "#188df0" },
        ]),
      },
      emphasis: {
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: "#2378f7" },
            { offset: 0.7, color: "#2378f7" },
            { offset: 1, color: "#83bff6" },
          ]),
        },
      },
      data: data,
    },
  ],
};

export default function BarChartComponent({
  dataAxis,
  data,
  onChartReady,
  ...props
}) {
  if (data.length === 0) {
    return <div className="h-64"></div>;
  }

  // console.log(dataAxis, data);
  let option = optionSample;
  option.xAxis.data = dataAxis;
  option.series[0].data = data;
  const zoomSize = 6;

  let echartRef = null;
  return (
    <EChartsReactCore
      echarts={echarts}
      ref={(e) => {
        echartRef = e;
      }}
      option={option}
      // notMerge={true}
      // lazyUpdate={true}
      onChartReady={onChartReady}
      onEvents={{
        click: (params) => {
          // console.log(dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)]);
          const echarts = echartRef.getEchartsInstance();
          echarts.dispatchAction({
            type: "dataZoom",
            startValue: dataAxis[Math.max(params.dataIndex - zoomSize / 2, 0)],
            endValue:
              dataAxis[
                Math.min(params.dataIndex + zoomSize / 2, data.length - 1)
              ],
          });
        },
      }}
      {...props}
    />
  );
}

BarChartComponent.propTypes = {
  dataAxis: PropsTypes.array,
  data: PropsTypes.array,
  onChartReady: PropsTypes.func,
};
