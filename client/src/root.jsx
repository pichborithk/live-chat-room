import { useEffect, useState } from 'react';
import { Outlet, useNavigate } from 'react-router-dom';
import { Navbar } from './components';

const initialToken = sessionStorage.getItem('TOKEN')
    ? sessionStorage.getItem('TOKEN')
    : '';

const Root = () => {
    const [token, setToken] = useState(initialToken);
    const [userData, setUserData] = useState({});

    const navigate = useNavigate();

    async function getUserData() {
        if (!token) return;

        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/api/users/me`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${token}`,
                    },
                }
            );
            const result = await response.json();
            if (result.error) {
                sessionStorage.clear();
                setToken('');
                return;
            }
            // console.log(result);
            setUserData(result.data);
        } catch (error) {
            console.error('Catch error on fetchUserData', error);
        }
    }

    useEffect(() => {
        if (!token) {
            setUserData({});
            return;
        } else {
            getUserData();
            navigate('/home');
        }
    }, [token]);

    return (
        <div className='mx-auto flex min-h-screen max-w-7xl flex-col items-center max-h-screen justify-center text-sky-600'>
            <Navbar token={token} setUserData={setUserData} />
            <Outlet context={{ token, setToken, userData }} />
        </div>
    );
};
export default Root;
