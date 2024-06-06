import axios from 'axios'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'

export default function FAQCreate() {

    const navigate = useNavigate()

    const [formFAQ, setFormFAQ] = useState({
        question: '',
        response: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormFAQ({ ...formFAQ, [name]: value })
    }

    const createFAQ = async (e) => {
        e.preventDefault()
        try {
            await axios.post('http://127.0.0.1:8000/api/createFaq/', formFAQ)
                .then(res => {
                    console.log(res)
                    console.log(formFAQ);
                    navigate('/admin/faq')
                })

        } catch (error) {
            console.log(error)
        }
    }


return (
    <div className="update-home h-full" data-aos="fade-up" data-aos-duration="1000">
        <h1 className='pl-5 pt-3'><b>FAQ</b></h1>
        <div className='update-home-content py-5 px-5 h-[70%]'>
            <div className='backoffice-header'>
                <h3>Créer FAQ</h3>
                <Link className='back' to={'/admin/faq'}><button>Retour</button></Link>
            </div>
            <form className='flex flex-col gap-3' onSubmit={createFAQ}>
                <label>Question :</label>
                <input type="text" name='question' value={formFAQ.question} onChange={(e) => handleChange(e)} />
                <label>Réponse : </label>
                <input type="text" name='response' value={formFAQ.response} onChange={(e) => handleChange(e)} />
                <button type="submit">Ajouter</button>
            </form>
        </div>
    </div>
)
}