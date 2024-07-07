import React from 'react'

const ColorInput = ({color, setColor}) => {
    return (
        <form className="changeColorForm" onSubmit={(e)=>e.preventDefault()}>
            <input
                id='color'
                type='text'
                placeholder='Type Color'
                required
                value={color}
                onChange={(e)=>setColor(e.target.value)}
            />
        </form>
    )
}
export default ColorInput
