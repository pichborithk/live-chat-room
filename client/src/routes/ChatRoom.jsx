import { useEffect, useState } from 'react';
import { useNavigate, useOutletContext, useParams } from 'react-router-dom';
import { MessageForm } from '../components';
import { socket } from '../socket';

const ChatRoom = () => {
    const { token, userData } = useOutletContext();
    const [messages, setMessages] = useState([]);

    const { roomCode } = useParams();
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
        socket.emit('join', { room: roomCode });
        console.log('Socket connected');

        return () => {
            socket.emit('leave', { room: roomCode });
            socket.disconnect();
            console.log('Socket disconnected');
        };
    }, []);

    useEffect(() => {
        function onMessageEvent(data) {
            setMessages(prev => [...prev, data]);
        }

        socket.on('message', onMessageEvent);
        const messages = document.getElementById('messages');
        messages.scrollTo(0, messages.scrollHeight);

        return () => {
            socket.off('message', onMessageEvent);
        };
    }, [messages]);

    async function getMessages() {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/api/rooms/${roomCode}`,
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
                navigate('/');
                return;
            }
            // console.log(result);
            setMessages(result.data);
            // navigate('/');
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <div className='shadow-full w-full p-4 flex flex-col gap-2 max-h-screen min-h-screen pt-16'>
            <h1 className='text-center text-4xl font-bold'>ChatRoom</h1>
            <div
                className='flex flex-col w-full flex-1 gap-2 py-2 overflow-y-auto'
                id='messages'
            >
                <div className='flex flex-col justify-end gap-2 px-2 flex-1'>
                    {messages?.map(message => (
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
            <MessageForm token={token} roomCode={roomCode} />
        </div>
    );
};
export default ChatRoom;
