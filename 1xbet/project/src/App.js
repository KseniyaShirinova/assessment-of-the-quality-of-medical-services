import logo from './logo.svg';
import './App.css';
import MainContainer from "./UI/Main/main-container"
import Main from "./UI/Main/main";
import 'bootstrap/dist/css/bootstrap.min.css';
import TomskAmbulance from "./UI/TomskAmbulance/TomskAmbulance";
import {BrowserRouter, Route} from "react-router-dom";

function App() {
  return (
      <BrowserRouter>
        <Route exact path="/" render={() => <MainContainer />}/>
        <Route path="/tomsk_ambulance" render={() => <TomskAmbulance/>}/>
        </BrowserRouter>
  );
}

export default App;
