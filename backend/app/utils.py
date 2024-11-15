# backend/app/utils.py
import pandas as pd
import re

def clean_text(text):
    """
    Bersihkan teks dari karakter yang tidak diinginkan.
    """
    text = re.sub(r'\s+', ' ', text)  # Menghapus spasi berlebih
    text = re.sub(r'[^\w\s]', '', text)  # Menghapus karakter non-alfanumerik
    return text.strip()

def save_conversation(user_input, response, file_path='app/data/conversations.csv'):
    # Load existing conversations
    try:
        conversations = pd.read_csv(file_path)
    except FileNotFoundError:
        conversations = pd.DataFrame(columns=['user_input', 'response'])
    
    # Append new conversation
    new_conversation = pd.DataFrame([[user_input, response]], columns=['user_input', 'response'])
    conversations = pd.concat([conversations, new_conversation], ignore_index=True)
    
    # Save back to CSV
    conversations.to_csv(file_path, index=False)