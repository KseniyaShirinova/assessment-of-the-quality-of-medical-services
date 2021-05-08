import React from "react";
import {combineReducers,createStore} from "redux";
import MainReducer from "./main-reducer";

const reducers=combineReducers({
    Data:MainReducer
})

let store=createStore(reducers);

export default store;