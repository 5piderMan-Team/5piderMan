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

export {
  getJobs,
  getCitiesAnalyze,
  getEducationAnalyze,
  getPositionbAnalyze,
  getLanguagesAnalyze,
};
