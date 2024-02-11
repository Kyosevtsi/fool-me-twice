import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const LobbyPage = props => {
    const [players, setPlayers] = useState(null);

    return (
        <div>
            {/*<table>
                {Array(4).fill(true).map((_, i) => < key={i} />)}
    </table>*/}
            <p>Waiting for players.</p>
            <p>All players found! Starting game.</p>
            <p>Lobby Code: {props.code}</p>
        </div>
    )
}

export default LobbyPage;