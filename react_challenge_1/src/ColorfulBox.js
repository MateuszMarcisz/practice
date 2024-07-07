import React from 'react'

const ColorfulBox = ({color, hexColor, isDark}) => {
    const boxColor = {
        backgroundColor: color,
        color: isDark ? '#000' : '#FFF'
    }
    return (
        <section className="colorful_box" style={boxColor} >
            <p>{color ? color : 'EmptyValue'}</p>
            <p>{hexColor ? hexColor : null}</p>
        </section>
    )
}
export default ColorfulBox
