import React, {useEffect, useState, type ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';
import { ImSpinner9 } from "react-icons/im";

import { getRepoStars } from '../services/api';
import ContributorCards from '../components/ContributorCards';
import DownloadCount from '../components/DownloadCount';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const [loading, setLoading] = useState(true);
  const [repoStars, setRepoStars] = useState<number | null>(null);

  useEffect(() => {
    const init = async () => {
      const stars = await getRepoStars();
      setRepoStars(stars);
      setLoading(false);
    };

    init();
  }, []);

  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title content">
          Synology API
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className="center-content">
          <Link
            className="custom-btn padding--md margin--md"
            to="https://github.com/N4S4/synology-api"
          >
            <span className="center-content">
              Star on GH ⭐
              {loading ? 
                <ImSpinner9 className="loading-icon" size={20} /> 
                  : 
                repoStars ? repoStars : ''
              }
            </span>
          </Link>
          <Link
            className="custom-btn padding--md margin--md"
            to="https://github.com/sponsors/N4S4"
          >
            Sponsor ❤️
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  return (
    <Layout
      title={`Home`}
      description="Community built open source Python wrapper around Synology NAS API, trusted by over 100k users."
    >
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <DownloadCount />
        <ContributorCards />
      </main>
    </Layout>
  );
}
