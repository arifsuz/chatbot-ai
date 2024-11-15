# backend/app/routes.py
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