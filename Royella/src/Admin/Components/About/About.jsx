import { useEffect, useState } from 'react'
import axios from 'axios'
import './About.css'
import { Link } from 'react-router-dom'

export default function About() {

    const [hotel, setHotel] = useState({
        titre: '',
        description: '',
        localisation: '',
        image: '',
        video : ''
    });


    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/hotel/")
            .then((response) => {
                setHotel(response.data.hotels);
                console.log(response.data.hotels);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    return (
        <div className="update-home h-full w-[100%]" data-aos="fade-up" data-aos-duration="1000">
            <h1 className='titre pl-5 pt-3'><b>ABOUT</b></h1>
            <div className='backoffice-header'>
                <h3 className='ml-5 mt-3'>Hotel</h3>
            </div>
            {hotel ? <div className='update-home-content py-5 px-5 h-[100%] w-[100%]'>
                <div className='row-contact'>
                    <div className='flex items-center gap-10'><h4>Titre :</h4> {hotel.titre}</div>
                </div>
                <div className='row-contact'>
                    <div className='flex items-center gap-10'><h4 className='w-[15%]'>Description :</h4> {hotel.description}</div>
                </div>
                <div className='row-contact'>
                    <div className='flex items-center gap-10'><h4>Localisation :</h4> {hotel.localisation}</div>
                </div>
                <div className='row-contact media-container'>
                    <div className='flex items-center gap-10'>
                        <h4>Image & Video :</h4> 
                        <div className='media-container'>
                            <img src={`http://127.0.0.1:8000${hotel.image}`} alt={hotel.titre} />
                            <a href={`http://127.0.0.1:8000${hotel.video}`} target='_blank' rel="noreferrer">Lien vidéo <i className="gg-play-button-r"></i></a>
                        </div>
                    </div>
                </div>
                <div className='contact-footer'>
                    <Link to={'/admin/about/update'}><button>Update</button></Link>
                </div>
            </div> : null}
        </div>
    )

}