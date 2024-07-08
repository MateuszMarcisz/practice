import React from 'react'

const LineElement = (element) => {
    return (
        <li className='element'>
            {JSON.stringify(element.element)}
        </li>
    )
}
export default LineElement
