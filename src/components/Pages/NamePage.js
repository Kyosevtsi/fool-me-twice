const NamePage = props => {
    const [name, setName] = useState("");

    return (
        <div>
            <h2>Enter name</h2>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            <button onClick={props.onContinue}>Continue</button>
        </div>
    )
}

export default NamePage;