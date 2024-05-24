import { useEffect } from "react";
import AOS from "aos";
import "aos/dist/aos.css";
import HelmetChanger from "../Shared/Helmet/Helmet";
import { Outlet } from "react-router-dom";
import Admin from "../Admin/Components/Admin/Admin";

export default function MainAdmin() {
    useEffect(() => {
        AOS.init();
        AOS.refresh();
    }, []);

    return (
        <>
            <HelmetChanger title="Back Office" />
            <div className="flex w-screen h-screen">
                <Admin className="w-[25%]"/>
                    <div className="w-[75%]">
                        <Outlet />
                    </div>
            </div>
        </>
    )
}