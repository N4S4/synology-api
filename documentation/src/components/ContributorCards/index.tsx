import { getRepoContributors } from "@site/src/services/api";
import React, { useEffect, useState } from "react";
import styles from './styles.module.css';

interface CardProps {
  username: string;
  avatar_url: string;
}

const Card: React.FC<CardProps> = ({ username, avatar_url }) => {
  return (
    <div className="avatar avatar__photo avatar__photo--lg margin--sm">
      <img
        alt={`${username} Profile`}
        src={avatar_url}
      />
      <div className="user-info">

      </div>
    </div>
  );
}

const ContributorCards = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    const init = async () => {
      const contributors = await getRepoContributors();
      setData(contributors);
      console.log(data);
    };

    init();
  }, []);

  return (
    <div className="container">
      <h2>Built by the community:</h2>
      <div className="row center-content">
        {data && data.map((item) => (
          <Card key={item.id} username={item.login} avatar_url={item.avatar_url} />
        ))}
      </div>
    </div>
  );
};

export default ContributorCards;