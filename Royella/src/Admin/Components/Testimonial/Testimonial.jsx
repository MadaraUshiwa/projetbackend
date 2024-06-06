import { Link } from 'react-router-dom'
import axios from 'axios'
import { useEffect, useState } from 'react'
import './Testimonial.css'
import { FaStar } from "react-icons/fa";

export default function Testimonial() {


    const [testimonial, setTestimonial] = useState(null);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/testimonial/")
            .then((response) => {
                if (response.data.testimonials) {
                    setTestimonial(response.data.testimonials);
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const destroy = async (e) => {
        await axios.delete(`http://127.0.0.1:8000/api/deleteTestimonial/${e}`)
            .then(
                res => {
                    console.log(res);
                    setTestimonial(testimonial.filter(testi => testi.id !== e))
                }
            )
    }

    return (
        <div className='update-home h-full w-[100%]' data-aos="fade-up" data-aos-duration="1000" >
            <h1 className='titre pl-5 pt-3'><b>TESTIMONIALS</b></h1>
            <div className='update-home-content py-5 px-5 h-[90%] w-[100%]'>
                <div className='facilities-container h-[100%]'>
                    <div className='backoffice-header'>
                        <Link className='add' to={'/admin/testimonials/add'}><button>Ajouter</button></Link>
                    </div>
                    <div className="table-testi-container h-[80%] overflow-y-scroll">
                        <table className='h-full'>
                            <thead>
                                <tr scope='col' className='first-col'>ID</tr>
                                <tr scope='col'>Nom</tr>
                                <tr scope='col'>Note</tr>
                                <tr scope='col' className='facilities-last-col'></tr>
                            </thead>
                            <tbody>
                                {testimonial ? testimonial.map((testi, index) => (
                                    <tr key={index}>
                                        <th scope='row' className='first-col'>{testi.id}</th>
                                        <td>{testi.nom}</td>
                                        <td className='flex gap-3'>
                                            {testi.note} 
                                            <FaStar key={index} className="w-[14px] h-[14px] lg:w-[16px] lg:h-[16px] text-khaki" />
                                        </td>
                                        <td className='facilities-last-col'>
                                            <i onClick={() => destroy(testi.id)} className="gg-remove delete"></i>
                                        </td>
                                    </tr>
                                )) : null}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    )
}