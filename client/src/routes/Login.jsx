import { useEffect, useState } from 'react';
import { Input } from '../components';
import { Link, useNavigate, useOutletContext } from 'react-router-dom';

const Login = () => {
  const { token, setToken } = useOutletContext();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  useEffect(() => {
    if (token) {
      sessionStorage.setItem('TOKEN', token);
      navigate('/chatroom');
    }
  }, [token]);

  async function handleSubmit(event) {
    event.preventDefault();

    if (!username || !password) return;

    try {
      const response = await fetch(
        `${import.meta.env.VITE_API_URL}/api/users/login`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        }
      );
      const result = await response.json();
      if (result.error) {
        console.log(result.error);
        return;
      }
      console.log(result);
      setToken(result.data.token);
      // navigate('/');
    } catch (error) {
      console.error(error);
    } finally {
      setUsername('');
      setPassword('');
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className='flex flex-col items-center w-1/3 shadow-full gap-8 rounded-md py-8 px-12 justify-evenly bg-sky-600 text-slate-200 font-bold text-xl'
    >
      <h1 className='text-4xl font-bold'>Login</h1>
      <Input
        value={username}
        setValue={setUsername}
        name='username'
        type='text'
        required={true}
        label='Username'
      />
      <Input
        value={password}
        setValue={setPassword}
        name='password'
        type='password'
        required={true}
        label='Password'
      />
      <div className='w-full text-center'>
        <button className='my-4 w-full rounded-md shadow-full bg-slate-50 py-2 hover:bg-sky-800 hover:text-slate-50 text-sky-600'>
          LOGIN
        </button>
        <p className='text-base font-normal'>
          Don&apos;t have an account?{' '}
          <Link to='/register' className='underline hover:font-bold'>
            Join Us
          </Link>
        </p>
      </div>
    </form>
  );
};
export default Login;
