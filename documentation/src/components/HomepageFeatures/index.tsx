import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import React from 'react';

type FeatureItem = {
  title: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: '⚙️ Seamless Automation',
    description: (
      <>
        Take full advantage of Python's flexibility to automate routine tasks on your Synology NAS. Whether it's managing backups, organizing files, or scheduling system maintenance, you can create powerful scripts that save you time and effort.
      </>
    ),
  },
  {
    title: '📈 Continuous Growth',
    description: (
      <>
        With 300+ APIs and 25+ implementations, we provide a rich set of features to interact with your NAS. We're continuously expanding the package, adding new APIs and enhancements to keep up with the latest updates and user needs. 
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--5')}>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row center-content">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
