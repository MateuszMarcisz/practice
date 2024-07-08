import React from 'react';
import ContentList from './ContentList'

const Content = ({list}) => {

    return (
        <>
            {list.length ? (
                <ContentList
                    list={list}
                />
            ) : (
                <p style={{marginTop: '2rem'}}>List is empty</p>
            )}
        </>
    )
}
export default Content
