import Header from "../Main/Header/Header";
import Content from "./Content/Content"
import Footer from "../Main/Footer/Footer";
import React from "react";


const TomskAmbulance=(props)=>{

    return(
        <div className="main-content">
            <Header class_header={"header_container"}></Header>
            <Content></Content>
            <Footer></Footer>
        </div>
    )



}
export default TomskAmbulance;