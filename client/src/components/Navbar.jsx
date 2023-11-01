/* eslint-disable react/prop-types */

import { Link } from 'react-router-dom';

const Navbar = (token, setUserData) => {
    function handleLogOut() {
        sessionStorage.clear();
        token.setToken('');
        setUserData({});
    }

    return (
        <nav className='text-2xl font-bold bg-sky-600 w-full fixed top-0 text-gray-50'>
            <div className='mx-auto flex items-center justify-between py-2 max-w-7xl px-8'>
                <Link to='/'>Live Chat Room</Link>
                {token.token && (
                    <div className='flex gap-8'>
                        <Link to='/home'>Home</Link>
                        <Link to='/profile'>Profile</Link>
                        <Link to='/' onClick={handleLogOut}>
                            Log Out
                        </Link>
                    </div>
                )}
            </div>
        </nav>
    );
};
export default Navbar;
