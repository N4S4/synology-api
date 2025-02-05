import { Octokit } from "octokit";
import { throttling } from "@octokit/plugin-throttling";

const OctokitThrottled = Octokit.plugin(throttling);

const octokit = new OctokitThrottled({
  throttle: {
    onRateLimit: (retryAfter, options, octokit, retryCount) => {
      octokit.log.warn(
        `Request quota exhausted for request ${options.method} ${options.url}`,
      );

      if (retryCount < 1) {
        octokit.log.info(`Retrying after ${retryAfter} seconds!`);
        return true;
      }

      throw new Error("Request quota exhausted");
    },
    onSecondaryRateLimit: (retryAfter, options, octokit) => {
      octokit.log.warn(
        `SecondaryRateLimit detected for request ${options.method} ${options.url}`,
      );
    },
  },
});

export const getRepoStars = async () => {
  const cachedData = localStorage.getItem('stars');
  if (cachedData && JSON.parse(cachedData)?.expires > Date.now()) {
    return JSON.parse(localStorage.getItem('stars')!).count;
  }

  let data: object[] = [];
  data = await octokit.paginate("GET /repos/N4S4/synology-api/stargazers", {
    per_page: 100,
    headers: {
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });

  const jsonData = {
    "count": data.length,
    "expires": Date.now() + 600000 // Expires in 10 minutes
  }

  localStorage.setItem('stars', JSON.stringify(jsonData));
  return data.length;
}

export const getRepoContributors = async () => {
  const cachedData = localStorage.getItem('contributors');
  if (cachedData && JSON.parse(cachedData)?.expires > Date.now()) {
    return JSON.parse(localStorage.getItem('contributors')!).data;
  }
  
  let data: object[] = [];
  data = await octokit.paginate("GET /repos/N4S4/synology-api/contributors", {
    per_page: 100,
    headers: {  
      "X-GitHub-Api-Version": "2022-11-28",
    },
  });

  const jsonData = {
    "data": data,
    "expires": Date.now() + 600000 // Expires in 10 minutes
  }

  localStorage.setItem('contributors', JSON.stringify(jsonData));
  return data;
}