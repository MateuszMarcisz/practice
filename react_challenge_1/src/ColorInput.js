import React from 'react';
import colorNames from 'colornames'

const ColorInput = ({color, setColor, setHexColor, isDark, setIsDark}) => {
    return (
        <form className="changeColorForm" onSubmit={(e) => e.preventDefault()}>
            <input
                id='color'
                type='text'
                placeholder='Type Color Name'
                required
                value={color}
                onChange={(e) => {
                    setColor(e.target.value);
                    setHexColor(colorNames(e.target.value));
                }}
                autoFocus
                aria-label="Type Color Name"
            />
            <button
                type='button'
                onClick={()=>setIsDark(!isDark)}
                >
                Toggle Text Color
            </button>
        </form>
    )
}
export default ColorInput
