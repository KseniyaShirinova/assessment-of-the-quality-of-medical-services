import React from "react";
import Header from "./Header/Header";
import Content from "./Content/Content";
import Footer from "./Footer/Footer";
import * as axios from "axios";

const Main=(props)=>{
    if(props.data.Data.status==false) {
        axios.get("http://localhost:3001").then(response => {
            console.log(response)
            props.setData(response.data[0])
        })
    }
    return(
        <div className="main-content">
            <Header class_header={"header_container"}></Header>
            <Content data={props.data}></Content>
            <Footer></Footer>
        </div>
    )
}
export default Main;