import React, { useState } from 'react';
import axios from 'axios';
import './Login.css';

export default function Login() {
    const [formLogin, setFormLogin] = useState({
        username: '',
        password: ''
    })

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await axios.post('http://127.0.0.1:8000/api/login/', formLogin);
        localStorage.setItem('access_token', response.data.access_token);
        localStorage.setItem('role', response.data.role);
        console.log(response);
        window.location.href = "/";
    };

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormLogin({...formLogin, [name]: value});
    }

    console.log(formLogin);

    return (
        <div className="login">
            <div className="login_right">
                <div className="login_right_title">
                    <h1>BIENVENUE</h1>
                </div>
                <div className="login_right_form">
                    <form onSubmit={handleSubmit}>
                        <div className="login_right_form_email">
                            <label htmlFor="username">E-mail</label>
                            <input type="text" id="email" name='username' value={formLogin.username} onChange={e => handleChange(e)} />
                        </div>
                        <div className="login_right_form_password">
                            <label htmlFor="password">Password</label>
                            <input type="password" id="password" name='password' value={formLogin.password} onChange={e => handleChange(e)} />
                        </div>
                        <div className="login_right_form_submit">
                            <button type="submit">Connexion</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}