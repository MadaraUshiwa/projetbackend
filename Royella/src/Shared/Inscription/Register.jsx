// Register.jsx
import React, { useState } from 'react';
import './Register.css';

const Register = () => {
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [photo, setPhoto] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!name || !surname || !email || !password || !photo) {
      alert('Veuillez remplir tous les champs');
      return;
    }
  
    const formData = new FormData();
    formData.append('name', name);
    formData.append('surname', surname);
    formData.append('email', email);
    formData.append('password', password);
    formData.append('photo', photo);
  
    fetch('http://127.0.0.1:8000/api/register/', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
  };

  const handlePhotoChange = (e) => {
    setPhoto(e.target.files[0]);
  };

  return (
    <form className="register-form" onSubmit={handleSubmit}>
      <div className="login_right_title">
        <h1>BIENVENUE</h1>
      </div>
      <input type="text" placeholder="Nom" onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="Prénom" onChange={(e) => setSurname(e.target.value)} />
      <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Mot de passe" onChange={(e) => setPassword(e.target.value)} />
      <input type="file" onChange={handlePhotoChange} />
      <button type="submit">S'inscrire</button>
    </form>
  );
};

export default Register;