import axios from 'axios'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'

export default function StaffCreate() {

    const navigate = useNavigate()

    const [formEmployees, setFormEmployees] = useState({
        nom: '',
        poste: '',
        citation: '',
        image: ''
    });

    const handleChange=(e)=>{
        const {name, value, type, files} = e.target
        setFormEmployees({...formEmployees, [name]: type === "file" ? files[0] : value})
    }


    const createEmployees = async (e) => {
        e.preventDefault()
        try {
            await axios.post('http://127.0.0.1:8000/api/createEmployees/', formEmployees, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(res => {
                console.log(res)
                console.log(formEmployees);
                navigate('/admin/staff')
        })

        } catch (error) {
            console.log(error)
        }
    }

    return (
        <div className="update-home h-full" data-aos="fade-up" data-aos-duration="1000">
            <h1 className='pl-5 pt-3'><b>Employés</b></h1>
            <div className='update-home-content py-5 px-5 h-[100%]'>
                <div className='backoffice-header'>
                    <h3>Ajouter Employés</h3>
                    <Link className='back' to={'/admin/staff'}><button>Retour</button></Link>
                </div>
                <form className='flex flex-col gap-3' onSubmit={createEmployees}>
                    <label>Nom :</label>
                    <input type="text" name='nom' value={formEmployees.nom} onChange={(e) => handleChange(e)} />
                    <label>Poste :</label>
                    <input type="text" name='poste' value={formEmployees.poste} onChange={(e) => handleChange(e)} />
                    <label>Citation :</label>
                    <input type="text" name='citation' value={formEmployees.citation} onChange={(e) => handleChange(e)} />
                    <label>Image :</label>
                    <div className='flex items-center gap-5'>
                        <input type="file" name='image' onChange={(e) => handleChange(e)} />
                    </div>
                    <button type="submit">Confirmer</button>
                </form>
            </div>
        </div>
    )
}