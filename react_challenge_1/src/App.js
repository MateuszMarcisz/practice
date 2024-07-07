import './App.css';
import ColorfulBox from "./ColorfulBox";
import ColorInput from "./ColorInput";
import {useState} from "react";

function App() {
    const [color, setColor] = useState('')

    return (
        <div className="App">
            <ColorfulBox
                color={color}
                setColor={setColor}
            />
            <ColorInput
                color={color}
                setColor={setColor}
            />
        </div>
    );
}

export default App;
