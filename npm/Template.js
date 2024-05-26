import React from 'react';

const TEMPLATE = props => {
    
    let color = '#fff';
    if (props.color)
        color = props.color;

    let width = 512;
    if (props.width)
        width = props.width;

    let height = 512;
    if (props.height)
        height = props.height;
    
    return (
        <svg viewBox={`0 0 ${width} ${height}`}>
            PATH
        </svg>
    );
}

export default TEMPLATE;