import React from 'react';

const LogoutButton = () => {
  const handleClick = () => {
    // Remove the username from local storage
    localStorage.removeItem('username');

    // Redirect the user to the login page
    window.location.href = '/chat';
  };

  return (
    <button onClick={handleClick}>Logout</button>
  );
};

export default LogoutButton;