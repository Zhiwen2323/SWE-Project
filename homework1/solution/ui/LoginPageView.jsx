import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const LoginPage = () => {
  const history = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Validate the username and password
    if (username === "" || password === "") {
      setError("Username and password cannot be empty");
      return;
    }

    // TODO: Send a request to the server to verify the username and password
    // Redirect to chat page if logged in successfully

    fetch('http://127.0.0.1:4444/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password }),
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(error => {
          setError(error.message || 'Something went wrong.');
        });
      };
      // Save the username in local storage
      localStorage.setItem('username', username);

      // Redirect the user to the chat page
      window.location.href = '/chat';
    })
    .catch(error => {
      setError(error.message || 'Something went wrong.');
    });
  };

  return (
    <div className="login-page">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleUsernameChange}
        />
        <input
          type="text"
          placeholder="Password"
          value={password}
          onChange={handlePasswordChange}
        />
        <button type="submit">Login</button>
      </form>
      <Link className="signup-link" to="/signup">Create an account</Link>
      {error !== "" && <div className="error">{error}</div>}
    </div>
  );
};

export default LoginPage;
