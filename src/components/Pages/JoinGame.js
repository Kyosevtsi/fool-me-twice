import './JoinGame.css';

const JoinPage = props => {
    return (
        <div>
            <h2>Enter Game Code</h2>
            <input type="text" value={props.code} onChange={(e) => props.setCode(e.target.value)} />
            <button onClick={props.onContinue}>Continue</button>
        </div>
    );
}
  
export default JoinPage;