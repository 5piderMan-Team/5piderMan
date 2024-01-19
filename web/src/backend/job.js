import axios from "axios";

const serverUrl = "";

const getJobs = () => {
  return axios.get(serverUrl + "/api/jobs").then((response) => {
    return response.data;
  });
};

export { getJobs };
