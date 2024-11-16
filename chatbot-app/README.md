# Mercubuana University Customer Service Chatbot

This project is a customer service chatbot application created using React and Tailwind CSS. This application allows users to interact with a chatbot that provides customer service.

## Installation

1. **Clone the repository:**
   ```sh
   git clone <REPOSITORY_URL>
   cd chatbot-app
   ```

2. **Install dependencies:**
   Make sure you have Node.js and npm installed on your system. Then run the following command:
   ```sh
   npm install
   ```

## Running the Project

1. **Run the application in development mode:**
   ```sh
   npm start
   ```
   The application will run at [http://localhost:3000](http://localhost:3000).

2. **Build the application for production:**
   ```sh
   npm run build
   ```
   This will create a production build in the `build` folder.

## Project Structure

```
chatbot-app/
├── package.json
├── public/
│   ├── index.html
│   ├── manifest.json
├── README.md
├── src/
│   ├── App.css
│   ├── App.js
│   ├── assets/
│   ├── components/
│   │   ├── Chat.js
│   │   └── Message.js
│   ├── index.css
│   ├── index.js
├── tailwind.config.js
```

## Modifying the Project

1. **Changing styles:**
   - You can change global styles in 

index.css

.
   - You can also change specific component styles in 

App.css

 or add Tailwind CSS classes directly in the components.

2. **Adding or modifying components:**
   - The main components are located in the 

components

 folder.
   - For example, to change the message appearance, you can edit 

Message.js

.

3. **Changing application logic:**
   - The main application logic is in 

Chat.js

.
   - You can change how messages are sent or received by editing the 

handleSendMessage

 function.

## Running Tests

1. **Run tests:**
   ```sh
   npm test
   ```
   This will launch the test runner in interactive watch mode.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)