import { useState } from 'react';
import axios from 'axios';
//import io from 'socket.io-client';

import CreatePage from './Pages/CreatePage';
import JoinPage from './Pages/JoinGame';
import NamePage from './Pages/NamePage';
import './FoolMeTwice.css';

export default function FoolMeTwice() {
    const [pageShown, setPageShown] = useState("home");
    const [lobbyOption, setLobbyOption] = useState("");
    const [language, setLanguage] = useState("ESP");
    const [maxPlayers, setMaxPlayers] = useState(4);    
    const [code, setCode] = useState(0);
    const [name, setName] = useState("");

    const languageMap = {
        'ESP': 0,
        'RUS': 1
    };

    const changePageHandler = selectedOption => {
        setPageShown(selectedOption);
        setLobbyOption(selectedOption);
    }

    const handleConnect = async () => {
        if (lobbyOption === "createGame") {
            gameData = {
                'language': languageMap[language],
                'numPlayers': maxPlayers
            };
            gid = await axios.post("http://localhost:5000/createLobby", gameData);  // returns game ID
            console.log(gid);
        }
    }

    return (
        <div className="container">
            {pageShown === 'home' &&
                <div className="button-container">
                    <button onClick={() => changePageHandler("createGame")}>Create Game</button>   
                    <button onClick={() => changePageHandler("joinGame")}>Join Game</button>
                </div>
            }
            {pageShown === "createGame" && <CreatePage language={language} setLanguage={setLanguage} maxPlayers={maxPlayers} setMaxPlayers={setMaxPlayers} onContinue={() => setPageShown("name")} />}
            {pageShown === "joinGame" && <JoinPage code={code} setCode={setCode} onContinue={() => setPageShown("name")} />}
            {pageShown === "name" && <NamePage name={name} setName={setName} connect={handleConnect}/>}
        </div>
    )
}
