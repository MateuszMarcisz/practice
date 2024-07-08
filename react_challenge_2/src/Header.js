import React from 'react'

const Header = ({resource, setResource}) => {
    return (
        <header>
            <button
                onClick={() => setResource('users')}
                className={resource === 'users' ? 'active' : ''}
            >
                Users
            </button>
            <button
                onClick={() => setResource('posts')}
                className={resource === 'posts' ? 'active' : ''}
            >
                Posts
            </button>
            <button
                onClick={() => setResource('comments')}
                className={resource === 'comments' ? 'active' : ''}
            >
                Comments
            </button>
        </header>
    )
}
export default Header
