import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import "./index.css";
import LoginPage from "./components/LoginPageView";
import ChatView from "./components/ChatView";
import SignupPage from "./components/SignupPageView";

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const username = localStorage.getItem("username");
    if (username) {
      fetch(`http://127.0.0.1:4444/login?username=${username}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          'Accept': 'application/json'
        },
      })
      .then(res => {
        if (!res.ok) {
          console.error('Response not OK:', res.status, res.statusText);
          throw new Error(res.statusText);
        }
        return res.json();
      })
      .then(data => {
        console.log("data", data)
        if (data.username === username) {
          setIsLoggedIn(true);
        } else {
          setIsLoggedIn(false);
        }
      });
    }
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        {isLoggedIn ? (
          <Route exact path="/" element={<ChatView />} />
        ) : (
          <Route exact path="/" element={<LoginPage />}  />
        )}
        <Route exact path="/chat" element={<ChatView />} />
        <Route exact path="/signup" element={<SignupPage />}  />
      </Routes>
    </BrowserRouter>

  );
};

export default App;


