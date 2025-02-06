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
  const cachedJson = JSON.parse(cachedData);
  if (cachedJson?.expires > Date.now()) {
    console.debug('[getRepoStars] Using cached data');
    return cachedJson.count;
  }

  try {
    let data: object[] = [];
    data = await octokit.paginate("GET /repos/N4S4/synology-api/stargazers", {
      per_page: 100,
      headers: {
        "X-GitHub-Api-Version": "2022-11-28",
      },
    });

    const jsonData = {
      "count": data.length,
      "expires": Date.now() + 60000 // Expires in 1 minute
    }

    localStorage.setItem('stars', JSON.stringify(jsonData));
    return data.length;
  } catch (error) {
    console.error(error);

    if (cachedJson) {
      console.debug('[getRepoStars] Using cached data');
      return cachedJson.count;
    }

    return 0;
  }
}

export const getRepoContributors = async () => {
  const cachedData = localStorage.getItem('contributors');
  const cachedJson = JSON.parse(cachedData);
  if (cachedJson?.expires > Date.now()) {
    console.debug('[getRepoStars] Using cached data');
    return cachedJson.data;
  }

  try {
    let data: object[] = [];
    data = await octokit.paginate("GET /repos/N4S4/synology-api/contributors", {
      per_page: 100,
      headers: {
        "X-GitHub-Api-Version": "2022-11-28",
      },
    });

    const jsonData = {
      "data": data,
      "expires": Date.now() + 60000 // Expires in 1 minute
    }

    localStorage.setItem('contributors', JSON.stringify(jsonData));
    return data;
  }
  catch (error) {
    console.error(error);

    if (cachedJson) {
      console.debug('[getRepoContributors] Using cached data');
      return cachedJson.data;
    }

    return 0;
  }
}