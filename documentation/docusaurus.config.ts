import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Synology NAS API Python Documentation',
  tagline: 'A Python wrapper around Synology API',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://N4S4.github.io/',

  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/synology-api/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'N4S4', // Usually your GitHub org/user name.
  projectName: 'synology-api', // Usually your repo name.
  
  trailingSlash: false,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/N4S4/synology-api/tree/master/documentation/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          lastmod: 'date',
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
          createSitemapItems: async (params) => {
            const {defaultCreateSitemapItems, ...rest} = params;
            const items = await defaultCreateSitemapItems(rest);
            return items.filter((item) => !item.url.includes('/page/'));
          },
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    metadata: [
      {
        name: 'google-site-verification', // Google Search Console
        content: 'MYQkGNflCIc_-YFbk3DnMu1sFRDAEZ0sd3JGPX5l89s'
      },
      {
        name: 'keywords',
        content: 'synology, nas, api, python, wrapper, scripts, automation, pip'
      }
    ],
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
      respectPrefersColorScheme: false,
    },
    image: 'img/syno-api.jpg',
    navbar: {
      title: 'Synology API',
      logo: {
        alt: 'Synology API Logo',
        src: 'img/logo-round.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/N4S4/synology-api',
          className: 'header-github-link',
          "aria-label": 'GitHub repository',
          position: 'right',
        },
      ],
    },
    footer: {
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/category/getting-started',
            },
            {
              label: 'Supported APIs',
              to: '/docs/apis/',
            },
            {
              label: 'APIs Classes',
              to: '/docs/category/api-classes',
            },
            {
              label: 'Contribute',
              to: '/docs/category/contribute',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Telegram Dev Group',
              href: 'https://t.me/SynologyApi',
            },
          ],
        },
        {
          title: 'Github',
          items: [
            {
              label: 'Create a discussion',
              to: 'https://github.com/N4S4/synology-api/discussions',
            },
            {
              label: 'Report an issue',
              to: 'https://github.com/N4S4/synology-api/issues',
            },
            {
              label: 'Sponsor',
              to: 'https://github.com/sponsors/N4S4',
            },
          ],
        },
      ],
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
