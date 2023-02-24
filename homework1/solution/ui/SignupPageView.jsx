import React, { useState } from "react";
import {Link} from "react-router-dom";

const SignupPage = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleConfirmPasswordChange = (event) => {
    setConfirmPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Validate the input
    if (username === "" || email === "" || password === "" || confirmPassword === "") {
      setError("All fields are required");
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match");
      return;
    }

    fetch("http://127.0.0.1:4444/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        username,
        email,
        password
      })
    })
      .then((res) => {
        if (!res.ok) {
          console.error('Response not OK:', res.status, res.statusText);
          throw new Error(res.statusText);
        }
        return res.json();
      })
      .then((data) => {
        if (data.error) {
          setError(data.error);
        } else {
          // Save the username in local storage
          localStorage.setItem('username', username);

          // Redirect the user to the chat page
          window.location.href = '/chat';
        }
      })
      .catch((err) => {
        setError("An error occurred while trying to sign up");
        console.error(err);
      });
  };

  return (
    <div className="signup-page">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={handleUsernameChange}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={handleEmailChange}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={handlePasswordChange}
        />
        <input
          type="password"
          placeholder="Confirm password"
          value={confirmPassword}
          onChange={handleConfirmPasswordChange}
        />
        <button type="submit">Sign up</button>
      </form>
      {error !== "" && <div className="error">{error}</div>}
      <Link className="login-link" to="/">Login</Link>
    </div>
  );
};

export default SignupPage;
