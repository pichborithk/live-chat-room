import { useState } from 'react';
import { Input } from '../components';
import { Link } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  return (
    <form className='flex flex-col items-center w-1/3 shadow-full gap-8 rounded-md py-8 px-12 justify-evenly bg-sky-600 text-slate-200 font-bold text-xl'>
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
