import ButtonNum from "./component/ButtonNum"

const ReactApp = () => {
    return(
        <div>
          <ButtonNum text={1} value={1} />
        </div>
    )
        
}

ReactDOM.render(<ReactApp/>, document.getElementById('react-app'))