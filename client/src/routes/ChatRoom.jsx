import { useEffect, useState } from 'react';
import { useNavigate, useOutletContext } from 'react-router-dom';
import { MessageForm } from '../components';
import { socket } from '../socket';

const ChatRoom = () => {
  const { token, userData } = useOutletContext();
  const [messages, setMessages] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    if (token) {
      getMessages();
    } else {
      navigate('/');
    }
  }, [token]);

  useEffect(() => {
    socket.connect();
    console.log('Socket connected');
    return () => {
      socket.disconnect();
      console.log('Socket disconnected');
    };
  }, []);

  useEffect(() => {
    function onMessageEvent(data) {
      setMessages(prev => [...prev, data]);
    }

    socket.on('message', onMessageEvent);

    return () => {
      socket.off('message', onMessageEvent);
    };
  }, [messages]);

  async function getMessages() {
    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/messages`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
      const result = await response.json();
      if (result.error) {
        console.log(result.error);
        sessionStorage.clear();
        return;
      }
      console.log(result);
      setMessages(result.data.messages);
      // navigate('/');
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className='shadow-full w-full p-4 flex flex-col flex-1 gap-4'>
      <div className='flex flex-col w-full flex-1'>
        <h1 className='text-center text-4xl font-bold'>ChatRoom</h1>
        <div className='flex flex-col flex-1 justify-end gap-1'>
          {messages.map(message => (
            <div
              key={message.id}
              className={`flex gap-1 items-center ${
                userData.username !== message.sender
                  ? 'self-end flex-row-reverse'
                  : ''
              }`}
            >
              <p className='bg-sky-600 text-white rounded-full w-8 h-8 text-center p-1'>
                {message.sender[0].toUpperCase()}
              </p>
              <p className='bg-sky-600 text-white rounded-full py-1 px-4'>
                {message.text}
              </p>
            </div>
          ))}
        </div>
      </div>
      <MessageForm token={token} setMessages={setMessages} />
    </div>
  );
};
export default ChatRoom;
