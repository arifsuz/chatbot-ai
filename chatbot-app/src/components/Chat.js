import React, { useState } from 'react';
import axios from 'axios';
import Message from './Message';

const Chat = () => {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  const handleSendMessage = async () => {
    if (message.trim() === '') return;

    setChatHistory([...chatHistory, { sender: 'user', text: message }]);

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', { message });
      setChatHistory([...chatHistory, { sender: 'user', text: message }, { sender: 'bot', text: response.data.response }]);
    } catch (error) {
      setChatHistory([...chatHistory, { sender: 'user', text: message }, { sender: 'bot', text: 'Maaf, terjadi kesalahan.' }]);
    }
    setMessage('');
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4">
        {chatHistory.map((chat, index) => (
          <Message key={index} sender={chat.sender} text={chat.text} />
        ))}
      </div>
      <div className="flex p-4 border-t border-gray-300">
        <input 
          type="text" 
          value={message} 
          onChange={(e) => setMessage(e.target.value)} 
          placeholder="Tanya sesuatu..." 
          className="flex-1 p-2 border border-gray-300 rounded-lg"
        />
        <button onClick={handleSendMessage} className="ml-4 p-2 bg-blue-500 text-white rounded-lg">Kirim</button>
      </div>
    </div>
  );
};

export default Chat;