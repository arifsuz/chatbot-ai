import React from 'react';

const Message = ({ sender, text }) => {
  const isUser = sender === 'user';
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div className={`max-w-xs p-3 rounded-lg ${isUser ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}>
        <p>{text}</p>
      </div>
    </div>
  );
};

export default Message;