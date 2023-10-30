import { Link } from 'react-router-dom';

const Welcome = () => {
    // const { token } = useOutletContext();

    return (
        <div className='flex flex-col shadow-full p-8 gap-4 text-center font-inter font-extrabold text-2xl rounded-md text-slate-200'>
            <Link
                to='/login'
                className='bg-sky-600 py-4 w-60 rounded-md hover:bg-sky-800'
            >
                Login
            </Link>
            <Link
                to='/register'
                className='bg-sky-600 py-4 w-60 rounded-md hover:bg-sky-800'
            >
                Register
            </Link>
        </div>
    );
};
export default Welcome;
