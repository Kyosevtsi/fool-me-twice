import { useState } from "react";

const CreatePage = props => {
    return (
        <div>
            <h2>Game Settings</h2>
            <button onClick={props.onContinue}>Continue</button>
        </div>
    );
}

export default CreatePage;