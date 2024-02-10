import { Fragment, useState, useEffect } from 'react';

export default function FoolMeTwice() {
    const [pageShown, setPageShown] = useState("home");

    return (
        <Fragment>
            <button onClick={() => setPageShown()}/> 
            <HomePage />
            <gameSettingsPage />
            <gamePage />
        </Fragment>
    )
}