import './Staff.css'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { useEffect, useState } from 'react'

export default function Staff() {


    const [manager, setManager] = useState(null);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/manager/")
            .then((response) => {
                if (response.data.managers) {
                    setManager(response.data.managers);
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const [employees, setEmployees] = useState(null);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/employe/")
            .then((response) => {
                if (response.data.employes) {
                    setEmployees(response.data.employes);
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const destroy = async (e) => {
        await axios.delete(`http://127.0.0.1:8000/api/deleteEmployees/${e}`)
            .then(
                res => {
                    console.log(res);
                    setEmployees(employees.filter(employee => employee.id !== e))
                }
            )
    }

    return (
        <div className='update-home h-full w-[100%]' data-aos="fade-up" data-aos-duration="1000" >
            <h1 className='titre pl-5 pt-3'><b>STAFF</b></h1>
            <div className='update-home-content py-5 px-5 h-[90%] w-[100%]'>
                <div className='facilities-container h-[40%]'>
                    <div className='backoffice-header h-[30%]'>
                        <h3>Manager</h3>
                    </div>
                    <div className="table-manager-container h-[65%]">
                        <table className='h-[100%]'>
                            <thead className='h-[15%]'>
                                <tr scope='col' className='first-col'>ID</tr>
                                <tr scope='col'>Nom</tr>
                                <tr scope='col'>Poste</tr>
                                <tr scope='col'>Citation</tr>
                                <tr scope='col'>Image</tr>
                                <tr scope='col' className='facilities-last-col'></tr>
                            </thead>
                            <tbody className='h-[90%]'>
                                {manager ?
                                    <tr>
                                        <th scope='row' className='first-col'>{manager.id}</th>
                                        <td>{manager.nom}</td>
                                        <td>{manager.poste}</td>
                                        <td>{manager.citation}</td>
                                        <td><img className='h-[100%]' src={`http://127.0.0.1:8000${manager.image}`} alt={manager.nom} /></td>
                                        <td className='facilities-last-col'>
                                            <Link to={`/admin/staff/manager/update`}><i className="gg-edit-markup"></i></Link>
                                        </td>
                                    </tr> : null}
                            </tbody>
                        </table>
                    </div>
                </div>
                <div className='facilities-container h-[60%] mt-5'>
                    <div className='backoffice-header flex-col'>
                        <h3 className='text-center w-[100%]'>Employés</h3>
                        <Link className='add' to={'/admin/staff/add'}><button>Ajouter</button></Link>
                    </div>
                    <div className="table-employees-container h-[80%] overflow-y-scroll mt-2">
                        <table className='h-full'>
                            <thead>
                                <tr scope='col' className='first-col'>ID</tr>
                                <tr scope='col'>Nom</tr>
                                <tr scope='col'>Poste</tr>
                                <tr scope='col'>Citation</tr>
                                <tr scope='col'>Image</tr>
                                <tr scope='col' className='services-last-col'></tr>
                            </thead>
                            <tbody>
                                {employees ? employees.map((employee, index) => (
                                    <tr key={index}>
                                        <th scope='row' className='first-col'>{employee.id}</th>
                                        <td>{employee.nom}</td>
                                        <td>{employee.poste}</td>
                                        <td>{employee.citation}</td>
                                        <td><img className='h-[100%] w-[60%]' src={`http://127.0.0.1:8000${employee.image}`}></img></td>
                                        <td className='services-last-col'>
                                            <Link to={`/admin/staff/update/${employee.id}`}>
                                            <i className="gg-edit-markup"></i>
                                            </Link>
                                            <i onClick={() => destroy(employee.id)} className="gg-remove delete"></i>
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