import React from "react";

const ChatHistory = ({ history }) => {
  // TODO: make the history clickable, and can resume history chat
  return (
    <ul className="history-list">
      {history.map((item, index) => (
        <li key={index}>
          <div className="history-item">
            <div className="history-input">{item.input}</div>
            <div className="history-output">{item.output}</div>
          </div>
        </li>
      ))}
    </ul>
  );
};

export default ChatHistory;
