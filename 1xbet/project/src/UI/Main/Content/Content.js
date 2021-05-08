import classes from "./Content-style.module.css";
import Slaider from "./Slaider";


const  Content=(props)=>{
    return(
        <div className={classes.content_container}>
            <div className={classes.hospital}>
                <h2 className={classes.group_title}>Больницы</h2>
                <Slaider data={props.data}></Slaider>
            </div>
        </div>
    )
}
export default Content;