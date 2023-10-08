import { Outlet } from 'react-router-dom';

const route = () => {
  return (
    <div className='mx-auto flex min-h-screen max-w-7xl flex-col items-center justify-center text-sky-600'>
      <Outlet />
    </div>
  );
};
export default route;
