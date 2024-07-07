import React from 'react'

const ColorfulBox = ({color, setColor}) => {
    const boxColor = {
        backgroundColor: color
    }
    return (
        <main style={boxColor} >
            {color ? color : 'EmptyValue'}
        </main>
    )
}
export default ColorfulBox
