import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import React from 'react';
import { motion } from 'motion/react';
import { fade, slideDown } from '@site/src/motion/variants';

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
      <motion.div 
        className="text--center padding-horiz--md"
        variants={slideDown}
        transition={{ delayChildren: 0.3, duration: .5 }}
      >
        <Heading as="h2">{title}</Heading>
        <motion.p
          variants={slideDown}
          transition={{ duration: 0.5 }}
        >
          {description}
        </motion.p>
      </motion.div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <motion.div 
          className="row center-content"
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, amount: 1 }}
          variants={fade}
          transition={{
            staggerChildren: 0.6, 
            duration: .5 
          }}
        >
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </motion.div>
      </div>
    </section>
  );
}
