import classes from './Header-style.module.css'

const Header=()=>{
    return (

        <div className={classes.header_container}>
            <div className={classes.header_container_mask}>
                <h2 className={classes.title}>Оценка качества медициских услуг Томской области</h2>
            </div>
        </div>
    )
}
export default Header;