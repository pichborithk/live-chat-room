import { useEffect } from 'react';
import { Link, useNavigate, useOutletContext } from 'react-router-dom';

const Home = () => {
    const { token } = useOutletContext();
    const navigate = useNavigate();

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
    }, []);

    return (
        <div className='flex flex-col shadow-full p-8 gap-4 text-center font-inter font-extrabold text-2xl rounded-md text-slate-200'>
            Home
            <Link to={'/chatroom'}>Chat Room</Link>
        </div>
    );
};
export default Home;
