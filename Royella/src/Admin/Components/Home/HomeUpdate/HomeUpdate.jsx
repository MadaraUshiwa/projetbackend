import '../Home.css'
import axios from 'axios'
import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'

export default function UpdateHome() {

    const { id } = useParams()
    const navigate = useNavigate()

    const [formBanner, setFormBanner] = useState({
        titre : '',
        stars : 0,
        image : null
    });

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/lireBanner/${id}/` )
        .then(response => {
            setFormBanner(response.data.banner)
            console.log(response.data.banner);
        })
        .catch(error => console.log(error))
    }, [id]);

    const handleChange=(e)=>{
        const {name, value, type, files} = e.target
        if (type === 'file' && files.length > 0) {
            setFormBanner({...formBanner, [name]: files[0]})
        } else {
            delete formBanner['image']
        }
        if (type !== 'file') {
            setFormBanner({...formBanner, [name]: value})
        }
    }

    const updateBanner =async(e)=>{
        e.preventDefault()
        console.log(formBanner.image);
        try {
            await axios.put(`http://127.0.0.1:8000/api/updateBanner/${id}/`, formBanner,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(res => console.log(res.data))
        } catch (error) {
            console.log(error);
        }
        navigate('/admin/')
    }

    return(
        <div className='update-home h-full ' data-aos="fade-up" data-aos-duration="1000">
            <h1 className=' titre pl-5 pt-3'>MODIFICATION BANNER</h1>
            <div className='update-home-content py-5 px-5 h-[100%]'>
                <div className='backoffice-header'>
                </div>
                <form className='form' onSubmit={updateBanner}>
                    <label>Title :</label>
                        <input type="text" name='titre' value={formBanner.titre} onChange={(e)=>handleChange(e)} />
                    <label>Rating :</label>
                        <div className='rating-container'>
                            <input className='rating' type="number" name='stars' value={formBanner.stars} onChange={(e)=>handleChange(e)}  />
                            <p>(0-5)</p>
                        </div>
                    <label>Image :</label>
                    <div className='flex gap-5'>
                        <img className='w-[25%]' src={`http://127.0.0.1:8000${formBanner.image}`} alt={formBanner.titre}></img>
                        <input type="file" name='image' onChange={(e)=>handleChange(e)}  />
                    </div>    
                    <button className='confirm' type="submit">Confirm</button>
                    <Link className='back' to={'/admin'}><button>Back</button></Link>
                </form>
            </div>
        </div>
    )
}