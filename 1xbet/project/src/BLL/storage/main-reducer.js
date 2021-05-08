const SET_DATA="SET-DATA"

let initial_state={
    status:false

}
const MainReducer=(state=initial_state,action)=>{
    let new_state;
    switch (action.type){
        case SET_DATA:
            new_state= {...action.state, status:true}
            console.log(new_state)
            return new_state
        default:
            return {...state}
    }
}
export default MainReducer;
export const setDataAC=(state)=>({type:SET_DATA,state})