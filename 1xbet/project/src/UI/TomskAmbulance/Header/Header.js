import classes from './header-style.module.css'

const Header=(props)=>{
    return (

        <div className={classes.header_Toms_Ambulance_container}>
            <div className={classes.header_container_mask}>
                <h2 className={classes.title}>Оценка качества медициских услуг Томской области</h2>
            </div>
        </div>
    )
}
export default Header;