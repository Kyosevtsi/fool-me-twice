import { useState } from "react";

import espFlag from "../../images/esp_svg.svg";
import rusFlag from "../../images/rus_svg.svg";

const CreatePage = props => {
    const [language, setLanguage] = useState("ESP");  // currently: 0=ESP, 1=RUS
    const [maxPlayers, setMaxPlayers] = useState(4);

    return (
        <div>
            <h2>Game Settings</h2>

            <h3>Select Language</h3>
            <button className={`lang-option${language === "ESP" ? " selected-setting" : ""}`} onClick={() => setLanguage("ESP")}><img src={espFlag} style={{ height: 50, width: 75}}/></button>
            <button className={`lang-option${language === "RUS" ? " selected-setting" : ""}`} onClick={() => setLanguage("RUS")}><img src={rusFlag} style={{ height: 50, width: 75}}/></button>

            <h3>Select Player Count</h3>
            <button className={`playercount${maxPlayers === 2 ? " selected-setting" : ""}`} onClick={() => setMaxPlayers(2)}>2</button>
            <button className={`playercount${maxPlayers === 3 ? " selected-setting" : ""}`} onClick={() => setMaxPlayers(3)}>3</button>
            <button className={`playercount${maxPlayers === 4 ? " selected-setting" : ""}`} onClick={() => setMaxPlayers(4)}>4</button>            
            
            <button onClick={props.onContinue}>Continue</button>
        </div>
    );
}

export default CreatePage;