/* eslint-disable react/prop-types */

import { useState } from 'react';
import { socket } from '../socket';

const MessageForm = ({ token, roomCode }) => {
    const [text, setText] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    async function handleSubmit(event) {
        event.preventDefault();

        if (!text) return;

        setIsLoading(true);
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/api/${roomCode}/messages`,
                {
                    method: 'POST',
                    headers: {
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text }),
                }
            );

            const result = await response.json();
            if (result.error) {
                console.log(result.error);
                return;
            }
            // console.log(result.data);
            setText('');
            const data = { message: result.data, room: roomCode };
            socket.timeout(5000).emit('message', data, () => {
                setIsLoading(false);
            });
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
            <button disabled={isLoading}>
                <i className='fa-solid fa-paper-plane text-2xl hover:text-3xl'></i>
            </button>
        </form>
    );
};
export default MessageForm;
