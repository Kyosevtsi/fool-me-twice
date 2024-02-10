const NamePage = props => {
    return (
        <div>
            <h2>Enter name</h2>
            <input type="text" value={props.name} onChange={(e) => props.setName(e.target.value)} />
            <button onClick={() => props.handleConnect()}>Continue</button>
        </div>
    )
}

export default NamePage;