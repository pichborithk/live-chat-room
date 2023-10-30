import { useEffect } from 'react';
import { useNavigate, useOutletContext } from 'react-router-dom';

const Profile = () => {
    const { token } = useOutletContext();
    const navigate = useNavigate();

    useEffect(() => {
        if (!token) {
            navigate('/');
        }
    }, []);

    return <div>Profile</div>;
};
export default Profile;
