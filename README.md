# Project Documentation - Chatbot AI

## Overview

This project is a chatbot application built using Flask for the backend and React with Tailwind CSS for the frontend. The chatbot uses the GPT-2 model to generate responses and supports model fine-tuning.

## Project Structure

### Backend

```
backend/
    app/
        __init__.py
        __pycache__/
        data/
            conversations.csv
            dataset.csv
        fine_tune.py
        model.py
        routes.py
        utils.py
    env/
        Include/
        Lib/
            site-packages/
        pyvenv.cfg
        Scripts/
            activate
            activate.bat
            Activate.ps1
    LICENSE
    README.md
    requirements.txt
    run.py
```

### Frontend

```
frontend/
    .gitignore
    LICENSE
    package.json
    public/
        index.html
        manifest.json
    README.md
    src/
        App.css
        App.js
        assets/
        components/
        index.css
        index.js
    tailwind.config.js
```

## Backend

### 

__init__.py



This file initializes the Flask application and enables CORS.

```py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    from .routes import bp
    app.register_blueprint(bp)
    return app
```

### 

routes.py



This file defines the API routes for the chatbot and model fine-tuning.

```py
from flask import Blueprint, request, jsonify
from .model import get_response_from_model
from .fine_tune import fine_tune_model
import logging

bp = Blueprint('routes', __name__)

@bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    logging.info(f"Received message: {user_input}")
    response = get_response_from_model(user_input)
    logging.info(f"Response: {response}")
    return jsonify({'response': response})

@bp.route('/fine-tune', methods=['POST'])
def fine_tune():
    fine_tune_model()
    return jsonify({'status': 'Model fine-tuned successfully'})
```

### 

app/fine_tune.py



This file is used to fine-tune the GPT-2 model using the provided dataset.

```py
from transformers import Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd

def fine_tune_model(dataset_path='app/data/conversations.csv'):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    # Fine-tuning logic here
```

### `requirements.txt`

This file contains the list of Python dependencies required to run this project.

```
flask
flask-cors
transformers
pandas
```

### `run.py`

This file is the main entry point to run the Flask application.

```py
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

### How to Run the Backend

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Run the application by executing `python run.py`.

The application will run on `http://localhost:5000`.

### API Endpoints

#### `POST /chat`

Send a message to the chatbot and get a response.

- **Request Body**: `{ "message": "Your message here" }`
- **Response**: `{ "response": "Chatbot response" }`

#### `POST /fine-tune`

Perform fine-tuning of the GPT-2 model with the provided dataset.

- **Response**: `{ "status": "Model fine-tuned successfully" }`

## Frontend

### `src/App.js`

The main application component that imports and displays the Chat component.

```js
import React from 'react';
import './App.css';
import Chat from './components/Chat';
import logo from './assets/logo.png';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Chat />
      </header>
    </div>
  );
}

export default App;
```

### `src/components/Message.js`

The Message component for displaying messages.

```js
import React from 'react';

const Message = ({ sender, text }) => {
  return (
    <div className={`message ${sender}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;
```

### `src/index.js`

The main JavaScript file that renders the React application into the root element in the HTML.

```js
import React from 'react';
import './index.css';
import App from './App';
import { createRoot } from 'react-dom/client';

const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

### `tailwind.config.js`

Configuration for Tailwind CSS.

```js
module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
```

### How to Run the Frontend

1. Navigate to the 

frontend

 directory.
2. Install the dependencies by running `npm install`.
3. Start the development server by running `npm start`.

The application will run on `http://localhost:3000`.

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### `npm test`

Launches the test runner in the interactive watch mode.

### `npm run build`

Builds the app for production to the `build` folder.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## Authors
**Developed by :**
**Muhamad Nur Arif**
**(41523010147)**

### 🔗 Link
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ariftsx.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arifsuz)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marif8/)
[![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ariftsx/)
