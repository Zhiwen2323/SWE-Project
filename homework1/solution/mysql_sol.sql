/* users table */
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

/* chat_history table */
CREATE TABLE chat_history (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  question TEXT NOT NULL,
  answer TEXT NOT NULL
);

/* questions table */
CREATE TABLE questions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  question TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

/* answers table */
CREATE TABLE answers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  question_id INT,
  answer TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);