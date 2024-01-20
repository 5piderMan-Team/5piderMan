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

export { getJobs };
