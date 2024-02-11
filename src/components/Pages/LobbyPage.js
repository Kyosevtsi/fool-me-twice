import { useEffect, useState } from "react";
import { io } from "socket.io-client";

const socket = io("http://localhost:5000");

const LobbyPage = props => {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        socket.on("updatePlayers", data => {
            if (data.gameID === props.code) {
                setPlayers(data.players);
            }
        });

        return () => {
            socket.off("updatePlayers");
        };
    }, [props.code]);

    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Player Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {players.map((name, index) => (
                        <tr key={index}>
                            <td>{name}</td>
                            <td>0</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {players.length === props.maxPlayers ? <p>All players found! Starting game.</p> : <p>Waiting for players.</p>}
            <p>Lobby Code: {props.code}</p>
        </div>
    );
}

export default LobbyPage;
