import "./Admin.css";
import { NavLink } from "react-router-dom";

export default function Admin() {
  return (
    <div className="admin_left">
      <div className="admin_left_title">
        <h1 className="title">BIENVENUE ADMIN</h1>
      </div>
      <div className="test">
        <div className="admin_left_menu">
          <div className="admin_left_menu_item">
            <NavLink to='/admin/'>
              <h2>HOME</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/about'>
              <h2>ABOUT</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/staff'>
              <h2>STAFF</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink  to='/admin/services'>
              <h2>SERVICES</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/testimonials'>
              <h2>TESTIMONIAL</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/blog'>
              <h2>BLOG</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/faq'>
              <h2>FAQ</h2>
            </NavLink>
          </div>
          <div className="admin_left_menu_item">
            <NavLink to='/admin/contact'>
              <h2>CONTACT</h2>
            </NavLink>
          </div>
        </div>
        <div className="img">
          <NavLink to={"/"}>
            <img src="/images/home-3/logo.png" alt="website_logo"></img>
          </NavLink>
        </div>
      </div>
    </div>
  );
}
