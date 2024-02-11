const NamePage = props => {
    return (
        <div>
            <h2>Enter name</h2>
            <input type="text" value={props.name} onChange={(e) => props.setName(e.target.value)} />
            <button onClick={() => props.connect()}>Continue</button>
        </div>
    )
}

export default NamePage;