import React from 'react';
import LineElement from './LineElement'

const ContentList = ({list}) => {
    return (
        <ul>
            {list.map((element)=>(
                <LineElement
                key={element.id}
                element={element}
                />
            ))}
        </ul>
    )
}
export default ContentList
