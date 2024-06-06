import './AboutUpdate.css'
import axios from 'axios'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'

export default function AboutUpdate() {

    const navigate = useNavigate()

    const [formHotel, setFormHotel] = useState({
        titre: '',
        description: '',
        image: '',
        localisation: '',
        video: ''
    });


    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/hotel/")
            .then((response) => {
                setFormHotel(response.data.hotels);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const handleChange = (e) => {
        const {name, value, type, files} = e.target
        if (type === 'file' && files.length > 0) {
            setFormHotel({...formHotel, [name]: files[0]})
        } else {
            delete formHotel['image']
        }
        if (type !== 'file') {
            setFormHotel({...formHotel, [name]: value})
        }
    }

    const updateHotel = async (e) => {
        e.preventDefault()
        try {
            await axios.put(`http://127.0.0.1:8000/api/updateHotel/`, formHotel,{
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(res => console.log(res.data))
        } catch (error) {
            console.log(error);
        }
        navigate('/admin/about')
    }

    return (
        <div className="update-home h-full" data-aos="fade-up" data-aos-duration="1000">
            <h1 className='pl-5 pt-3'><b>Update About</b></h1>
            <div className='update-home-content py-5 px-5 h-[100%]'>
                <div className='backoffice-header'>
                    <Link className='back' to={'/admin/about'}><button>Back</button></Link>
                </div>
                <form className='flex flex-col gap-3' onSubmit={updateHotel}>
                    <label>Title :</label>
                    <input type="text" name='titre' value={formHotel.titre} onChange={(e) => handleChange(e)} />
                    <label>Description :</label>
                    <input type="text" name='description' value={formHotel.description} onChange={(e) => handleChange(e)} />
                    <label>Location :</label>
                    <input type="text" name='localisation' value={formHotel.localisation} onChange={(e) => handleChange(e)} />
                    <label>Video :</label>
                    <input type="text" name='video' value={formHotel.video} onChange={(e) => handleChange(e)} />
                    <div className='flex items-center gap-5'>
                        <label>Image :</label>
                        <input type="file" name='image' onChange={(e) => handleChange(e)} />
                    </div>
                    <button type="submit" className='btn'>Confirm</button>
                </form>
            </div>
        </div>
    )
}