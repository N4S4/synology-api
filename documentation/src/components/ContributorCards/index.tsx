import { fade, slideUp } from "@site/src/motion/variants";
import { getRepoContributors } from "@site/src/services/api";
import { motion } from "motion/react";
import React, { useEffect, useState, MouseEvent } from "react";
import { isMobile } from "react-device-detect";
import { ImSpinner9 } from "react-icons/im";

interface CardProps {
  username: string;
  avatar_url: string;
}

const Card: React.FC<CardProps> = ({ username, avatar_url }) => {
  let hoverTimeout: NodeJS.Timeout;

  const handleMoseEnter = (event: MouseEvent) => {
    const element = event.currentTarget as HTMLDivElement;
    hoverTimeout = setTimeout(() => {
      element.classList.add('avatar-hovered');
      element.classList.add('shadow--tl');
    }, 500);
  }

  const handleMoseLeave = (event: MouseEvent) => {
    clearTimeout(hoverTimeout);
    const element = event.currentTarget as HTMLDivElement;
    element.classList.remove('avatar-hovered');
    element.classList.remove('shadow--tl');
  }

  return (
    <motion.div
      className="avatar avatar__photo avatar__photo--lg margin--sm"
      whileHover={{
        width: '4.5rem',
        height: '4.5rem',
      }}
      transition={{
        width: '0.3s ease', 
        height: '0.3s ease',
		    scale: '0.3s cubic-bezier(0.36, -0.04, 0, 1.08)'
      }}
      onMouseEnter={isMobile ? () => (false) : handleMoseEnter}
      onMouseLeave={isMobile ? () => (false) : handleMoseLeave}
    >
      <img
        alt={`${username} Profile`}
        src={avatar_url}
      />
      <motion.div 
        className="user-info"
        initial="hidden"
        whileHover="visible"
        variants={fade}
        transition={{ delay: 0.5 }}
      >
        <p className="margin-bottom--none text--break text--bold">{username}</p>
        <a
          href={`https://github.com/N4S4/synology-api/commits?author=${username}`}
          target="_blank"
          rel="noreferrer"
          className="text--light"
        >
          See contributions
        </a>
      </motion.div>
    </motion.div>
  );
}

const ContributorCards = () => {
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(null);

  useEffect(() => {
    const init = async () => {
      const contributors = await getRepoContributors();
      setData(contributors);
      setLoading(false);
    };

    init();
  }, []);

  return (
    <div className="container margin-vert--xl">
      {loading && (
        <div className="row center-content margin-bottom--lg">
          <ImSpinner9 className="loading-icon" size={20} />
        </div>
      )}
      {!loading && data?.length > 0 && (
        <div className="col">
          <h2>Built by the community:</h2>
          <motion.div 
            className="row center-content margin-bottom--lg"
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true, amount: .2 }}
            variants={fade}
            transition={{ staggerChildren: 0.05 }}
          >
            {data && data.map((item) => (
              <motion.div
                key={item.id}
                variants={slideUp}
              >
                <Card  username={item.login} avatar_url={item.avatar_url} />
              </motion.div>
            ))}
          </motion.div>
        </div>
      )}
    </div>
  );
};

export default ContributorCards;