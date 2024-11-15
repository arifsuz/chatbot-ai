# Bacnkend - Chatbot AI

This application is a Flask-based chatbot that uses the GPT-2 model to generate responses and supports model fine-tuning. The application also provides an API to interact with the chatbot and perform model fine-tuning.

## Project Structure

```
app/
    __init__.py
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
            pip/
```

## File and Code Explanation

### `app/__init__.py`

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

### `app/routes.py`

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

### `app/fine_tune.py`

This file is used to fine-tune the GPT-2 model using the provided dataset.

```py
from transformers import Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd

def fine_tune_model(dataset_path='app/data/conversations.csv'):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    
    conversations = pd.read_csv(dataset_path)
    dataset = conversations['user_input'].tolist() + conversations['response'].tolist()
    encodings = tokenizer(dataset, return_tensors="pt", padding=True, truncation=True)
    
    training_args = TrainingArguments(
        output_dir="./model_output",
        num_train_epochs=1,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=encodings['input_ids'],
    )
    
    trainer.train()
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")
```

### `app/model.py`

This file is used to load the dataset, generate responses from the GPT-2 model, and get responses from the model.

```py
import pandas as pd
from .utils import save_conversation, clean_text
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_dataset(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=';')
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def generate_response(user_input):
    model = GPT2LMHeadModel.from_pretrained("./fine_tuned_model")
    tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_model")
    
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

def get_response_from_model(user_input):
    dataset = load_dataset('app/data/dataset.csv')
    user_input = clean_text(user_input)
    
    for index, row in dataset.iterrows():
        ...
```

### `app/utils.py`

This file contains utility functions for cleaning text and saving conversations.

```py
import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def save_conversation(user_input, response, file_path='app/data/conversations.csv'):
    try:
        conversations = pd.read_csv(file_path)
    except FileNotFoundError:
        conversations = pd.DataFrame(columns=['user_input', 'response'])
    
    new_conversation = pd.DataFrame([[user_input, response]], columns=['user_input', 'response'])
    conversations = pd.concat([conversations, new_conversation], ignore_index=True)
    conversations.to_csv(file_path, index=False)
```

### `env/Scripts/Activate.ps1`

This file is a PowerShell script to activate the Python virtual environment.

```ps1
<#
.Synopsis
Activate a Python virtual environment for the current PowerShell session.
.Description
Pushes the python executable for a virtual environment to the front of the
$Env:PATH environment variable and sets the prompt to signify that you are
in a Python virtual environment. Makes use of the command line switches as
well as the `pyvenv.cfg` file values present in the virtual environment.
.Parameter VenvDir
Path to the directory that contains the virtual environment to activate. The
default value for this is the parent of the directory that the Activate.ps1
script is located within.
.Parameter Prompt
The prompt prefix to display when this virtual environment is activated. By
default, this prompt is the name of the virtual environment folder (VenvDir)
surrounded by parentheses and followed by a single space (ie. '(.venv) ').
.Example
Activate.ps1
Activates the Python virtual environment that contains the Activate.ps1 script.
.Example
Activate.ps1 -Verbose
Activates the Python virtual environment that contains the Activate.ps1 script,
and shows extra information about the activation as it executes.
.Example
Activate.ps1 -VenvDir C:\Users\MyUser\Common\.venv
Activates the Python virtual environment located in the specified location.
.Example
...
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

## How to Run the Project

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Run the application by executing `python run.py`.

The application will run on `http://localhost:5000`.

## API Endpoints

### `POST /chat`

Send a message to the chatbot and get a response.

- **Request Body**: `{ "message": "Your message here" }`
- **Response**: `{ "response": "Chatbot response" }`

### `POST /fine-tune`

Perform fine-tuning of the GPT-2 model with the provided dataset.

- **Response**: `{ "status": "Model fine-tuned successfully" }`

This documentation includes an explanation of the project structure, a description of each file and line of code, and how to run the project and use the available API endpoints.