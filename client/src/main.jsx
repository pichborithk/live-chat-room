import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import Root from './root';

import './index.css';
import {
    ChatRoom,
    ErrorPage,
    Home,
    Login,
    Profile,
    Register,
    Welcome,
} from './routes';

const router = createBrowserRouter([
    {
        path: '/',
        element: <Root />,
        errorElement: <ErrorPage />,
        children: [
            {
                index: true,
                element: <Welcome />,
            },
            { path: 'home', element: <Home /> },
            { path: 'profile', element: <Profile /> },
            { path: 'login', element: <Login /> },
            { path: 'register', element: <Register /> },
            { path: 'chatroom', element: <ChatRoom /> },
        ],
    },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>
);
