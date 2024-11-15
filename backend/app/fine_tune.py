# backend/app/fine_tune.py
from transformers import Trainer, TrainingArguments, GPT2LMHeadModel, GPT2Tokenizer
import pandas as pd

def fine_tune_model(dataset_path='app/data/conversations.csv'):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    
    # Load and tokenize dataset
    conversations = pd.read_csv(dataset_path)
    dataset = conversations['user_input'].tolist() + conversations['response'].tolist()
    encodings = tokenizer(dataset, return_tensors="pt", padding=True, truncation=True)
    
    # Define Trainer and TrainingArguments
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
    
    # Fine-tune model
    trainer.train()
    
    # Save the fine-tuned model
    model.save_pretrained("./fine_tuned_model")
    tokenizer.save_pretrained("./fine_tuned_model")