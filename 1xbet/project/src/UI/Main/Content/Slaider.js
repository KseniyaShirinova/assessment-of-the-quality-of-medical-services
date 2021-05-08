import {Carousel} from 'react-bootstrap';
import gor_klin_hospital from "./img/hospital/Городская клинческая больница №3 им. Б.И. Альперовича.jpg"
import ogayz_hospital from "./img/hospital/ОГАУЗ Больница № 2.jpg"
import tomsk_clinical_hospital from "./img/hospital/Томская городская клиническая больница.jpg"
import tomsk_psihiatr_hospital from "./img/hospital/Томская кличическия психиатрическая больница.jpg"
import classes from "./Slaider-style.module.css";
import star from "./img/Rating/pngegg.png"
import {NavLink} from "react-router-dom";

const getVisualRaiting =(result)=> {
    if (result > 4) {

        return (
            <div className="image_container">
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
            </div>
        )

    } else if (result > 3) {
        return (
            <div className="image_container">
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>

            </div>
        )
    } else if (result > 2) {
        return (
            <div className="image_container">
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>

            </div>
        )
    } else if (result > 1) {
        return (
            <div className="image_container">
                <img className={classes.img_raiting_stars} src={star}/>
                <img className={classes.img_raiting_stars} src={star}/>
            </div>
        )
    }
}

const Slaider=(props)=>{


    console.log(props.data.Data)
    debugger
    return(
        <Carousel>
            <Carousel.Item>
                <NavLink to="/tomsk_ambulance">
                    <img src="https://zdrav.tomsk.ru/storage/61552/1050-700!/001.jpg"
                     className="d-block w-100 text-center"
                     alt="First slide"
                    />
                </NavLink>
                <Carousel.Caption>
                    <h3 className={classes.title}>Томская больница скорой помощи</h3>
                    {props.data.Data.status==false ? getVisualRaiting(0) : getVisualRaiting(props.data.Data.data_Tomsk_ambulance.result)}

                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
               <NavLink to="/tomsk_ambulance"> <img src={gor_klin_hospital}
                     className="d-block w-100 text-center"
                     alt="First slide"
                />
               </NavLink>
                <Carousel.Caption>
                    <h3 className={classes.title}>Городская клинческая больница №3 им. Б.И. Альперовича</h3>
                    {props.data.Data.status==false ? getVisualRaiting(0) : getVisualRaiting(props.data.Data.data_klinikal_Hospital_3.result)}
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img src={ogayz_hospital}
                     className="d-block w-100 text-center"
                     alt="First slide"
                />
                <Carousel.Caption>
                    <h3 className={classes.title}>ОГАУЗ Больница №2</h3>
                    {props.data.Data.status==false ? getVisualRaiting(0) : getVisualRaiting(props.data.Data.data_OGAYZ_Hospital_2.result)}
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img src={tomsk_clinical_hospital}
                     className="d-block w-100 text-center"
                     alt="First slide"
                />
                <Carousel.Caption>
                    <h3 className={classes.title}>Томская городская клиническая больница</h3>
                    {props.data.Data.status==false ? getVisualRaiting(0) : getVisualRaiting( props.data.Data.data_google_okb_tomsk.result)}
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img src={tomsk_psihiatr_hospital}
                     className="d-block w-100 text-center"
                     alt="First slide"
                />
                <Carousel.Caption>
                    <h3 className={classes.title}>Томская кличическия психиатрическая больница</h3>
                    {props.data.Data.status==false ? getVisualRaiting(0) : getVisualRaiting( props.data.Data.data_okpb_Tomsk.result)}
                </Carousel.Caption>
            </Carousel.Item>
        </Carousel>
    )
}
export default Slaider