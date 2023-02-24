import React, {useState} from "react";

const ChatHistory = ({ history }) => {
  // TODO: make the history clickable, and can resume history chat
  const [input, setInput] = useState("");
  const handleClick = (event, input) => {
    event.preventDefault();
    setInput(input);
  };
  console.log(history)
  return (
    <ul className="history-list">
      {history.map((item, index) => (
        <li key={index}>
          <div className="history-item" onClick={(event) => handleClick(event, item.input)}>
            <div className="history-input">{item.question}</div>
            <div className="history-output">{item.answer}</div>
          </div>
        </li>
      ))}
    </ul>
  );
};

export default ChatHistory;
