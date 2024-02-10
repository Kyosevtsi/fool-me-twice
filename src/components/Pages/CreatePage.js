import { useState } from "react";
import "./CreatePage.css"

import espFlag from "../../images/esp_svg.svg";
import rusFlag from "../../images/rus_svg.svg";

const CreatePage = props => {
    return (
        <div>
            <h2>Game Settings</h2>

            <h3>Select Language</h3>
            <button className={`lang-option${props.language === "ESP" ? " selected-setting" : ""}`} onClick={() => props.setLanguage("ESP")}><img src={espFlag} style={{ height: 50, width: 75}}/></button>
            <button className={`lang-option${props.language === "RUS" ? " selected-setting" : ""}`} onClick={() => props.setLanguage("RUS")}><img src={rusFlag} style={{ height: 50, width: 75}}/></button>

            <h3>Select Player Count</h3>
            <button className={`playercount${props.maxPlayers === 2 ? " selected-setting" : ""}`} onClick={() => props.setMaxPlayers(2)}>2</button>
            <button className={`playercount${props.maxPlayers === 3 ? " selected-setting" : ""}`} onClick={() => props.setMaxPlayers(3)}>3</button>
            <button className={`playercount${props.maxPlayers === 4 ? " selected-setting" : ""}`} onClick={() => props.setMaxPlayers(4)}>4</button>            
            
            <button onClick={props.onContinue}>Continue</button>
        </div>
    );
}

export default CreatePage;