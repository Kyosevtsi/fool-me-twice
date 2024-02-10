import { Fragment, useState, useEffect } from 'react';

import CreatePage from './Pages/CreatePage';
import JoinPage from './Pages/JoinGame';
import NamePage from './Pages/NamePage';

export default function FoolMeTwice() {
    const [pageShown, setPageShown] = useState("home");

    return (
        <Fragment>
            {pageShown === 'home' &&
                <div>
                    <button onClick={() => setPageShown("createGame")}>Create Game</button>   
                    <button onClick={() => setPageShown("joinGame")}>Join Game</button>
                </div>
            }
            {pageShown === "createGame" && <CreatePage onContinue={() => setPageShown("name")} />}
            {pageShown === "joinGame" && <JoinPage onContinue={() => setPageShown("name")} />}
            {pageShown === "name" && <NamePage />}
        </Fragment>
    )
}