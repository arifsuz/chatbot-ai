import React from 'react';
import './App.css';
import Chat from './components/Chat';
import logo from './assets/logo.png';

function App() {
  return (
    <div className="h-screen flex flex-col">
      <header className="bg-blue-600 text-white p-4 flex items-center justify-between">
        <div className="flex items-center">
          <img src={logo} alt="Logo" className="h-10 mr-4" />
          <h1 className="text-2xl text-white">Chatbot Customer Service Universitas Mercubuana</h1>
        </div>
      </header>
      <main className="flex-1 p-4 bg-gray-100">
        <Chat />
      </main>
      <footer className="bg-blue-600 text-white p-4 text-center">
        &copy; 2023 Universitas Mercubuana ( Muhamad Nur Arif ). All rights reserved.
      </footer>
    </div>
  );
}

export default App;