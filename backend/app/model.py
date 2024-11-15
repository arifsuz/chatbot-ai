# backend/app/model.py
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
    # Load fine-tuned model
    model = GPT2LMHeadModel.from_pretrained("./fine_tuned_model")
    tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_model")
    
    # Tokenize input
    inputs = tokenizer(user_input, return_tensors="pt")
    
    # Generate response
    outputs = model.generate(inputs['input_ids'], max_length=50)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

def get_response_from_model(user_input):
    # Load the dataset
    dataset = load_dataset('app/data/dataset.csv')
    
    # Clean the user input
    user_input = clean_text(user_input)
    
    # Find the best match for the user input in the dataset
    for index, row in dataset.iterrows():
        if user_input.lower() in row['pertanyaan'].lower():
            response = row['jawaban']
            save_conversation(user_input, response)
            return response
    
    # If no match found, generate a response using the model
    response = generate_response(user_input)
    save_conversation(user_input, response)
    return response