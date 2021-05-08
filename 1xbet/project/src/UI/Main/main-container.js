import {connect} from "react-redux";
import Main from "./main";
import {setDataAC} from "../../BLL/storage/main-reducer";

let mapStateToProps=(state)=>{
    debugger
    return{
        data:state
    }
}
let mapDispatchToProps=(dispatch)=> {
    return {
        setData:(state)=>{
            dispatch(setDataAC(state))
        }
    }
}
export default connect(mapStateToProps,mapDispatchToProps)(Main)