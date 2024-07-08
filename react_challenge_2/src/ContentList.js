import React from 'react';
import LineElement from './LineElement'


const ContentList = ({ list }) => {
    const headers = Object.keys(list[0]);

    return (
        <table>
            <thead>
                <tr>
                    {headers.map(header => (
                        <th key={header}>{header}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {list.map((element) => (
                    <LineElement key={element.id} element={element} />
                ))}
            </tbody>
        </table>
    );
}
export default ContentList
