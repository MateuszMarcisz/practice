import React from 'react'

const LineElement = ({ element }) => {
    return (
        <tr>
            {Object.entries(element).map(([key, value]) => (
                <td key={key}>{typeof value === 'object' ? JSON.stringify(value) : value}</td>
            ))}
        </tr>
    );
}

// the blow one is better but it is much more complicated
// const LineElement = ({ element }) => {
//     const renderCellValue = (value) => {
//         if (typeof value === 'object' && value !== null) {
//             // Render nested object as a JSON string or recursively render its properties
//             return (
//                 <table>
//                     <tbody>
//                         {Object.entries(value).map(([nestedKey, nestedValue]) => (
//                             <tr key={nestedKey}>
//                                 <td>{nestedKey}</td>
//                                 <td>{renderCellValue(nestedValue)}</td>
//                             </tr>
//                         ))}
//                     </tbody>
//                 </table>
//             );
//         }
//         return value;
//     };
//
//     return (
//         <tr>
//             {Object.entries(element).map(([key, value]) => (
//                 <td key={key}>{renderCellValue(value)}</td>
//             ))}
//         </tr>
//     );
// }
export default LineElement
