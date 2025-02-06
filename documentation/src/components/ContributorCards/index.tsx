import { getRepoContributors } from "@site/src/services/api";
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
    <div
      className="avatar avatar__photo avatar__photo--lg margin--sm"
      onMouseEnter={isMobile ? () => (false) : handleMoseEnter}
      onMouseLeave={isMobile ? () => (false) : handleMoseLeave}
    >
      <img
        alt={`${username} Profile`}
        src={avatar_url}
      />
      <div className="user-info">
        <p className="margin-bottom--none text--break text--bold">{username}</p>
        <a
          href={`https://github.com/N4S4/synology-api/commits?author=${username}`}
          target="_blank"
          rel="noreferrer"
          className="text--light"
        >
          See contributions
        </a>
      </div>
    </div>
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
    <div className="container">
      {loading && (
        <div className="row center-content margin-bottom--lg">
          <ImSpinner9 className="loading-icon" size={20} /> 
        </div>
      )}
      {!loading && data?.length > 0 && (
        <>
          <h2>Built by the community:</h2>
          <div className="row center-content margin-bottom--lg">
            {data && data.map((item) => (
              <Card key={item.id} username={item.login} avatar_url={item.avatar_url} />
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default ContributorCards;