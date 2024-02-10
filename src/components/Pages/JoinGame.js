import { useState } from "react";

import './JoinGame.css';

const JoinPage = props => {
    const [code, setCode] = useState('');
  
    return (
        <div>
            <h2>Enter Game Code:</h2>
            <input type="text" value={code} onChange={(e) => setCode(e.target.value)} />
            <button onClick={props.onContinue}>Continue</button>
        </div>
    );
}
  
export default JoinPage;