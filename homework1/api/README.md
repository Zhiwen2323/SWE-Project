# Chat GPT Flask App
This is a simple Flask app that uses OpenAI's GPT-3 API to respond to chat messages. Your task is to extend this app and turn it into a full-fledged chat app.

## Tasks
1. Store the chat history:
   - Implement a way to store the chat history in database.
   - Add a new endpoint that returns the chat history.

2. Implement authentication:
   - The endpoint that allows users to log in has been added for you, you need to finish it properly
   - Add a new endpoint that allows users to logout.
   - Add authentication to the /chat endpoint, so that only logged-in users can use it.

3. Add error handling:
   - Add error handling to the endpoints, to return meaningful error messages to the client.