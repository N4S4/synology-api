import { getDownloadCount } from "@site/src/services/api";
import React, { useEffect, useState } from "react";
import { motion } from "motion/react"
import { ImSpinner9 } from "react-icons/im";
import { FiExternalLink } from "react-icons/fi";
import { fade, slideDown } from "@site/src/motion/variants";

interface CounterProps {
  title: string;
  count: string;
}

const Counter: React.FC<CounterProps> = ({ title, count }) => {
  const titleMap = {
    week: "Week",
    month: "Month",
    all: "All Time",
  }
  return (
    <motion.div 
      className="col center-content-col" 
      style={{ gap: '1rem' }}
      variants={slideDown}
      transition={{ delayChildren: 0.3 }}
    >
      <h3 className="margin--none">{titleMap[title]}</h3>
      <div className="counter-number">
        <motion.p
          className="margin--none"
          variants={slideDown}
        >
          {count}
        </motion.p>
      </div>
    </motion.div>
  );
};

const DownloadCount = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    const init = async () => {
      const downloads = await getDownloadCount();
      setData(downloads);
      setLoading(false);
    };

    init();
  }, []);

  return (
    <div className="container">
      {loading && (
        <div className="row center-content margin-bottom--lg">
          <ImSpinner9 className="loading-icon" size={20} />
        </div>
      )}
      {!loading && data && (
        <div className="col ">
          <div style={{ display: 'flex' }}>
            <h2 className="margin-right--sm">Download Trends</h2>
            <a href="https://pepy.tech/projects/synology-api" target="_blank" rel="notarget">
              <FiExternalLink />
            </a>
          </div>
          <motion.div
            className="row center-content margin-bottom--lg"
            style={{ gap: '6vw' }}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: .5 }}
            variants={fade}
            transition={{ staggerChildren: 0.4 }}
          >
            {Object.entries(data).map(([key, value]) => (
              <Counter key={key} title={key} count={String(value)} />
            ))}
          </motion.div>
        </div>
      )}
    </div>
  );
};

export default DownloadCount;