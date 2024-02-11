import { useEffect, useState } from 'react';
import axios from 'axios';
import io from 'socket.io-client';
import logo from '../images/foolmetwice.jpg'; // Import the image file

import CreatePage from './Pages/CreatePage';
import JoinPage from './Pages/JoinGame';
import NamePage from './Pages/NamePage';
import LobbyPage from './Pages/LobbyPage';
import './FoolMeTwice.css';

const socket = io("http://localhost:5000");

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
        console.log("Reached here");
        if (lobbyOption === "createGame") {
            let res = await axios.get(`http://localhost:5000/createLobby?language=${languageMap[language]}&numPlayers=${maxPlayers}&name=${name}`);  // returns game id
            console.log(res.data);
            setCode(res.data.gameID);
            pageShown("lobby");
        } else {  // lobbyOption === 'joinGame'
            socket.emit("join", JSON.stringify({gameID: code, username: name}));
            pageShown("lobby");
        }
    }

    return (
        <div className="container">
    {pageShown === "home" &&  <img src={logo} alt="Logo" />} {/* Include the image */}
    {pageShown === 'home' &&
        <div className="button-container">
            <button onClick={() => changePageHandler("createGame")}>Create Game</button>   
            <button onClick={() => changePageHandler("joinGame")}>Join Game</button>
        </div>
    }
    {pageShown === "createGame" && <CreatePage language={language} setLanguage={setLanguage} maxPlayers={maxPlayers} setMaxPlayers={setMaxPlayers} onContinue={() => setPageShown("name")} />}
    {pageShown === "joinGame" && <JoinPage code={code} onContinue={() => setPageShown("name")} />}
    {pageShown === "name" && <NamePage name={name} setName={setName} connect={handleConnect}/>}
    {pageShown === "lobby" && <LobbyPage lobbyOption={lobbyOption} maxPlayers={maxPlayers} code={code}/>}
</div>

    )
}
