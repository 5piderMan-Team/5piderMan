import axios from "axios";

const serverUrl = "";

const getJobs = (city) => {
  let url = serverUrl + "/api/jobs";
  if (city !== undefined) {
    url = url + "?city=" + city;
  }

  return axios.get(url).then((response) => {
    return response.data;
  });
};

const searchJobs = (search) => {
  return axios
    .get(serverUrl + "/api/jobs/search?keyword=" + search)
    .then((response) => {
      return response.data;
    });
};

const getCitiesAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/city").then((response) => {
    return response.data;
  });
};

const getEducationAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/education").then((response) => {
    return response.data;
  });
};

const getPositionbAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/position").then((response) => {
    return response.data;
  });
};

const getLanguagesAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/language").then((response) => {
    return response.data;
  });
};

const getSalaryAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/salary").then((response) => {
    return response.data;
  });
};

const getExperienceAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/experience").then((response) => {
    return response.data;
  });
};

const getCompanyAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/company_name").then((response) => {
    return response.data;
  });
};

const getCategoryAnalyze = () => {
  return axios.get(serverUrl + "/api/analyze/category").then((response) => {
    return response.data;
  });
};

const getGPTRespond = (question) => {
  return axios
    .post(serverUrl + "/api/gpt", { input: question })
    .then((response) => {
      return response.data;
    });
};

export {
  getJobs,
  getCitiesAnalyze,
  getEducationAnalyze,
  getPositionbAnalyze,
  getLanguagesAnalyze,
  searchJobs,
  getSalaryAnalyze,
  getExperienceAnalyze,
  getCompanyAnalyze,
  getCategoryAnalyze,
  getGPTRespond,
};
