import { Octokit } from "octokit";
import { throttling } from "@octokit/plugin-throttling";
import { CacheService } from "./cache";

const cache = new CacheService();

const OctokitThrottled = Octokit.plugin(throttling);
const octokit = new OctokitThrottled({
  throttle: {
    onRateLimit: (retryAfter, options, octokit, retryCount) => {
      octokit.log.warn(
        `Request quota exhausted for request ${options.method} ${options.url}`,
      );

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
  const data = cache.get('stars');
  if (data) {
    console.debug(`[getRepoStars] Using cache`);
    return data.length;
  }

  try {
    let data: object[] = [];
    data = await octokit.paginate("GET /repos/N4S4/synology-api/stargazers", {
      per_page: 100,
      headers: {
        "X-GitHub-Api-Version": "2022-11-28",
      },
    });

    cache.set('stars', data);
    return data.length;
  } catch (error) {
    console.error(error);

    if (cache.getExpired('stars')) {
      console.debug(`[getRepoStars] Using expired cache`);
      return cache.getExpired('stars').length;
    }

    return 0;
  }
}

export const getRepoContributors = async () => {
  const data = cache.get('contributors');
  if (data) {
    console.debug(`[getRepoContributors] Using cache`);
    return data;
  }

  try {
    let data: object[] = [];
    data = await octokit.paginate("GET /repos/N4S4/synology-api/contributors", {
      per_page: 100,
      headers: {
        "X-GitHub-Api-Version": "2022-11-28",
      },
    });

    cache.set('contributors', data);
    return data;
  }
  catch (error) {
    console.error(error);

    if (cache.getExpired('contributors')) {
      console.debug(`[getRepoContributors] Using expired cache`);
      return cache.getExpired('contributors');
    }

    return {};
  }
}

const _parseSVG = (text: string) => {
  const parsed = new DOMParser().parseFromString(text, "text/html");
  const svg = parsed.querySelector('svg');
  const textElements = svg.querySelectorAll("text");

  return textElements[textElements.length - 1].textContent;
}

export const getDownloadCount = async () => {
  const data = cache.get('downloads');
  if (data) {
    console.debug(`[getDownloadCount] Using cache`);
    return data;
  }

  try {
    const urls = {
      week: 'https://static.pepy.tech/badge/synology-api/week',
      month: 'https://static.pepy.tech/badge/synology-api/month',
      all: 'https://static.pepy.tech/badge/synology-api'
    };

    const responses = await Promise.all(
      Object.entries(urls).map(async ([key, url]) => {
        const res = await fetch(url);
        const text = await res.text();
        return [key, _parseSVG(text)];
      })
    );

    const downloadPeriods = Object.fromEntries(responses);
    cache.set('downloads', downloadPeriods);

    return downloadPeriods;
  } catch (error) {
    console.error(error);

    if (cache.getExpired('downloads')) {
      console.debug(`[getDownloadCount] Using expired cache`);
      return cache.getExpired('downloads');
    }

    return 0;
  }
}