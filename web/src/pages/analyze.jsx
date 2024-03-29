import { Layout } from "antd";
import { Col, Row } from "antd";
import { useEffect, useState } from "react";
const { Content } = Layout;
import { Spin } from "antd";
import BarChartComponent from "../components/Charts/BarChart.jsx";
import * as Api from "../backend/job.js";
import DoughnutChart from "../components/Charts/DoughnutChart.jsx";
import NightingaleChart from "../components/Charts/NightingaleChart.jsx";
import ScrollablePieChart from "../components/Charts/ScrollablePieChart.jsx";
import PyramidChart from "../components/Charts/PyramidChart.jsx";
import BasicPieChart from "../components/Charts/BasicPieChart.jsx";
import HalfPieChart from "../components/Charts/HalfPieChart.jsx";
import TreeMapChart from "../components/Charts/TreeMapChart.jsx";
import PropTypes from "prop-types";

function CityAnalyze() {
  const [cities, setCities] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getCitiesAnalyze().then((res) => {
      const cities = [];
      const data = [];
      for (const city in res) {
        cities.push(city);
        data.push(res[city]);
      }
      const limit = 10;
      if (cities.length > limit) {
        cities.splice(limit);
        data.splice(limit);
      }

      setCities(cities);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <BarChartComponent dataAxis={cities} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function EducationAnalyze() {
  const [education, setEducation] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getEducationAnalyze().then((res) => {
      const education = [];
      const data = [];
      for (const edu in res) {
        education.push(edu);
        data.push(res[edu]);
      }

      setEducation(education);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <DoughnutChart items={education} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function LanguageAnalyze() {
  const [language, setLanguage] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getLanguagesAnalyze().then((res) => {
      const language = [];
      const data = [];
      for (const lang in res) {
        language.push(lang);
        data.push(res[lang]);
      }

      setLanguage(language);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <NightingaleChart items={language} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function PositionAnalyze() {
  const [position, setPosition] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getPositionbAnalyze().then((res) => {
      const position = [];
      const data = [];
      for (const pos in res) {
        position.push(pos);
        data.push(res[pos]);
      }

      setPosition(position);
      setData(data);
    });
  }, []);
  const onReady = () => {
    setLoading(false);
  };
  return (
    <Spin tip="Loading" spinning={loading}>
      <ScrollablePieChart items={position} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function CategoryAnalyze() {
  const [category, setCategory] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getCategoryAnalyze().then((res) => {
      const category = [];
      const data = [];
      for (const cat in res) {
        category.push(cat);
        data.push(res[cat]);
      }

      setCategory(category);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <BasicPieChart items={category} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function SalaryAnalyze() {
  const [salary, setSalary] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getSalaryAnalyze().then((res) => {
      const salary = [];
      const data = [];
      for (const sal in res) {
        salary.push(sal);
        data.push(res[sal]);
      }

      setSalary(salary);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <PyramidChart items={salary} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function CompanyAnalyze() {
  const [company, setCompany] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getCompanyAnalyze().then((res) => {
      const company = [];
      const data = [];
      for (const com in res) {
        company.push(com);
        data.push(res[com]);
      }

      setCompany(company);
      setData(data);
    });
  }, []);

  const onReady = () => {
    setLoading(false);
  };

  return (
    <Spin tip="Loading" spinning={loading}>
      <TreeMapChart items={company} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function ExperienceAnalyze() {
  const [experience, setExperience] = useState([]);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    Api.getExperienceAnalyze().then((res) => {
      const experience = [];
      const data = [];
      for (const exp in res) {
        experience.push(exp);
        data.push(res[exp]);
      }

      setExperience(experience);
      setData(data);
    });
  }, []);
  const onReady = () => {
    setLoading(false);
  };
  return (
    <Spin tip="Loading" spinning={loading}>
      <HalfPieChart items={experience} data={data} onChartReady={onReady} />
    </Spin>
  );
}

function ChartDiv({ title, children }) {
  return (
    <div className="bg-white p-4 rounded-lg shadow-lg text-center m-4">
      <div className="text-3xl font-bold">{title}</div>
      <div className="mt-4">{children}</div>
    </div>
  );
}

ChartDiv.propTypes = {
  title: PropTypes.string,
  children: PropTypes.element,
};

function Analyze() {
  return (
    <Content className="min-h-screen mt-16 mb-16 ml-32 mr-32">
      <Row className="">
        <Col span={12}>
          <ChartDiv title="城市分布">
            <CityAnalyze />
          </ChartDiv>
        </Col>
        <Col span={12}>
          <ChartDiv title="学历要求">
            <EducationAnalyze />
          </ChartDiv>
        </Col>
      </Row>
      <Row>
        <Col span={12}>
          <ChartDiv title="热门语言占比">
            <LanguageAnalyze />
          </ChartDiv>
        </Col>
        <Col span={12}>
          <ChartDiv title="岗位分布">
            <PositionAnalyze />
          </ChartDiv>
        </Col>
      </Row>
      <Row>
        <Col span={12}>
          <ChartDiv title="岗位分类分布">
            <CategoryAnalyze />
          </ChartDiv>
        </Col>
        <Col span={12}>
          <ChartDiv title="公司分布">
            <CompanyAnalyze />
          </ChartDiv>
        </Col>
      </Row>
      <Row>
        <Col span={12}>
          <ChartDiv title="经验要求分析">
            <ExperienceAnalyze />
          </ChartDiv>
        </Col>
        <Col span={12}>
          <ChartDiv title="薪资分析">
            <SalaryAnalyze />
          </ChartDiv>
        </Col>
      </Row>
    </Content>
  );
}

export default Analyze;
