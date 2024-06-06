// import './CreateBlog.sass'
import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom'

export default function TestimonialCreate() {

    const [messageError, setMessageError] = useState('');

    const navigate = useNavigate();

    const [formTestimonial, setFormTestimonial] = useState({
        nom : '',
        note : '',
        image : null,
        testimon : '',
        pays : '',
        ville : '',
    });

    const handleChange=(e)=>{
        const {name, value, type, files} = e.target
        if (type === 'file' && files.length > 0) {
            setFormTestimonial({...formTestimonial, [name]: files[0]})
        } else {
            delete formTestimonial['image']
        }
        if (type !== 'file') {
            setFormTestimonial({...formTestimonial, [name]: value})
        }
    }

    const createTestimonial =async(e)=>{
        console.log(formTestimonial);
        e.preventDefault()
        if(formTestimonial.nom === '' || formTestimonial.note === '' || formTestimonial.image === null || formTestimonial.testimon === '' || formTestimonial.pays === '' || formTestimonial.ville === ''){
            setMessageError('Veuilez remplir tous les champs')
        } else {
            try {
                await axios.post('http://127.0.0.1:8000/api/createTestimonial/', formTestimonial, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(res => {
                    console.log(res)
                    navigate('/admin/testimonials')
            })
    
            } catch (error) {
                console.log(error)
            }
        }
    }

    return (
        <div className="create-home h-full" data-aos="fade-up" data-aos-duration="1000">
            <h1 className='pl-5 pt-3'><b>Créer Testimonials</b></h1>
            <div className='create-home-content py-5 px-5 h-[90%]'>
            <div className='backoffice-header'>
                    <Link className='back' to={'/admin/testimonials'}><button>Back</button></Link>
                </div>
                <form className='form-blog d-flex flex-col' onSubmit={createTestimonial}>
                    <label>Nom :</label>
                        <input type="text" name='nom' value={formTestimonial.nom} onChange={(e)=>handleChange(e)} />
                    <label>Pays :</label>
                        <input type="text" name='pays' value={formTestimonial.pays} onChange={(e)=>handleChange(e)}  />
                    <label>Ville :</label>
                        <input type="text" name='ville' value={formTestimonial.ville} onChange={(e)=>handleChange(e)}  />
                    <label>Image :</label>
                        <input type="file" name='image' onChange={(e)=>handleChange(e)}  />
                    <label>Note :</label>
                        <input type="number" name='note' value={formTestimonial.note} onChange={(e)=>handleChange(e)}  />
                    <label>Testimonial :</label>
                        <textarea className='text-black' type="text" name='testimon' value={formTestimonial.testimon} onChange={(e)=>handleChange(e)}  />
                    <div className='error' style={{display: messageError ? 'block' : 'none'}}>
                        {messageError}
                    </div>
                    <button type="submit">Add</button>
                </form>
            </div>
        </div>
    )
}