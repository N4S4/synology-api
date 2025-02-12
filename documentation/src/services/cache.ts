export class CacheService {
  expires: number;

  constructor(expires: number = 180000) {
    this.expires = expires;
  }

  get(key: string): any {
    const cachedData = localStorage.getItem(key);
    if (!cachedData) return null;

    try {
      const cachedJson = JSON.parse(cachedData);
      return cachedJson?.expires > Date.now() ? cachedJson.data : null;
    } catch {
      return null;
    }
  }

  getExpired(key: string): any {
    const cachedData = localStorage.getItem(key);
    if (!cachedData) return null;

    try {
      const cachedJson = JSON.parse(cachedData);
      return cachedJson.data || null;
    } catch {
      return null;
    }
  }

  set(key: string, data: any, expires?: number): void {
    const jsonData = {
      data,
      expires: Date.now() + (expires ?? this.expires),
    };

    localStorage.setItem(key, JSON.stringify(jsonData));
  }
}