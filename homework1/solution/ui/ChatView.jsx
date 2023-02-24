import React, {useEffect, useState} from "react";
import ChatHistory from "./ChatHistory";
import LogoutButton from "./LogoutButton";

const ChatView = () => {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [history, setHistory] = useState([]);

  let username = localStorage.getItem("username")

  // TODO: load the chat history for the user and render it on the page
  useEffect(() => {
     fetch(`http://127.0.0.1:4444/chat_history?username=${username}`)
    .then(response => response.json())
    .then(data => {
      if (data !== undefined && data.length > 0) {
        setHistory(data)
      }
    })
    .catch(error => console.error(error));
  }, [])


  const handleQuestionChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // TODO: Send the input to an API to get the response from AI
    fetch('http://127.0.0.1:4444/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, question }),
    })
    .then(response => response.json())
    .then(data => {
      setAnswer(data.answer);
      setHistory([...history, {question, answer }]);
      setQuestion("");
    })
    .catch(error => console.error(error));
  };

  return (
    <div className="chat-view">
      <div className="left-panel">
        <ChatHistory history={history} />
        <LogoutButton></LogoutButton>
      </div>
      <div className="right-panel">
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Ask something..."
            value={question}
            onChange={handleQuestionChange}
          />
          <button type="submit">Submit</button>
        </form>
        <div className="output">{answer}</div>
      </div>
    </div>
  );
};

export default ChatView;
