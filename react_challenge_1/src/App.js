import ColorfulBox from "./ColorfulBox";
import ColorInput from "./ColorInput";
import {useState} from "react";

function App() {
    const [color, setColor] = useState('')
    const [hexColor, setHexColor] = useState((''))
    const [isDark, setIsDark] = useState(true)

    return (
        <div className="App">
            <ColorfulBox
                color={color}
                hexColor={hexColor}
                isDark={isDark}
            />
            <ColorInput
                color={color}
                setColor={setColor}
                setHexColor={setHexColor}
                isDark={isDark}
                setIsDark={setIsDark}
            />
        </div>
    );
}

export default App;
