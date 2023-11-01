import { useEffect } from 'react';
import { Link, useNavigate, useOutletContext } from 'react-router-dom';

const Home = () => {
    const { token, userData } = useOutletContext();
    const navigate = useNavigate();

    async function createRoom() {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/api/rooms/create`,
                {
                    method: 'POST',
                    headers: {
                        Authorization: `Bearer ${token}`,
                        'Content-Type': 'application/json',
                    },
                }
            );

            const result = await response.json();
            if (result.error) {
                console.log(result.error);
                return;
            }
            navigate(`/chatroom/${result.data.code}`);
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
    }, [token]);

    return (
        <div className='flex flex-col shadow-full p-8 gap-4 text-center font-inter font-extrabold text-2xl rounded-md text-slate-200'>
            <h1 className='text-4xl'>Rooms</h1>
            <div>
                {userData.rooms?.map((room, index) => (
                    <Link key={index} to={`/chatroom/${room}`}>
                        Enter: {room}
                    </Link>
                ))}
            </div>
            <button
                className='bg-sky-600 p-4 text-xl rounded-md'
                onClick={createRoom}
            >
                Create Room
            </button>
        </div>
    );
};
export default Home;
