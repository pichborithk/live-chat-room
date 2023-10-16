/* eslint-disable react/prop-types */

import { useState } from 'react';

const MessageForm = ({ token, setMessages }) => {
  const [text, setText] = useState('');

  async function handleSubmit(event) {
    event.preventDefault();

    if (!text) return;

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/messages`, {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const result = await response.json();
      if (result.error) {
        console.log(result.error);
        return;
      }
      console.log(result.data);
      setText('');
      setMessages(prev => [...prev, result.data]);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <form onSubmit={handleSubmit} className='w-full flex gap-4'>
      <input
        className='shadow-full w-full px-4 py-2 rounded-md focus:outline-sky-600'
        value={text}
        onChange={event => setText(event.target.value)}
      />
      <button>
        <i className='fa-solid fa-paper-plane text-2xl hover:text-3xl'></i>
      </button>
    </form>
  );
};
export default MessageForm;
