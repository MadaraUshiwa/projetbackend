import './UpdateServices.css'
import axios from 'axios'
import { useState,useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'
import { useParams } from 'react-router-dom'

export default function UpdateServices() {

    const navigate = useNavigate()

    const [formService, setFormService] = useState({
        titre: '',
        theme: '',
        description: '',
        ordre: 0,
        image: ''
    });

    const handleChange = (e) => {
        const {name, value, type, files} = e.target
        if (type === 'file' && files.length > 0) {
            setFormService({...formService, [name]: files[0]})
        } else {
            delete formService['image']
        }
        if (type !== 'file') {
            setFormService({...formService, [name]: value})
        }
    }

    const { id } = useParams()

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/readService/${id}/` )
        .then(response => setFormService(response.data.service))
        .catch(error => console.log(error))
    }, [id]);

    console.log(formService);

    const updateService =async(e)=>{
        e.preventDefault()
        try {
            await axios.put(`http://127.0.0.1:8000/api/updateService/${id}/`, formService,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(res => console.log(res.data))
        } catch (error) {
            console.log(error);
        }
        navigate('/admin/services')
    }


return (
    <>
        {formService ? <>
            <div className="update-home h-full" data-aos="fade-up" data-aos-duration="1000">
        <h1 className='pl-5 pt-3'><b>Services</b></h1>
        <div className='update-home-content py-5 px-5 h-[100%]'>
            <div className='backoffice-header'>
                <Link className='back' to={'/admin/services'}><button>Retour</button></Link>
            </div>
            <form className='update-service' onSubmit={updateService}>
                <label>Titre : <span className='service-info'>{formService.titre}</span></label>
                <label>Theme : <span className='service-info'>{formService.theme}</span></label>
                <label>Description :</label>
                <p className='service-info'>{formService.description}</p>
                <label>Image :<img className='service-image' src={`http://127.0.0.1:8000${formService.image}`}></img></label>
                <label>Ordre :</label>
                <input type="number" name='ordre' value={formService.ordre} onChange={(e) => handleChange(e)} />
                <button type="submit">Confirmer</button>
            </form>
        </div>
    </div>
        </> :
        <p>Chargement...</p>}
    </>
)
}