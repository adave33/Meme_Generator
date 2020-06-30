import React from 'react'

function Header(){
    return(
        <div>
            <form method="POST">
                <header>
                    <img width="100" height="150" src ="http://www.pngall.com/wp-content/uploads/2016/05/Trollface.png" alt="Problem?"
                    />
                    <p>Meme Generator</p> 
                </header>
                <span><a href="http://127.0.0.1:8000/logout/">Log Out</a></span>
            </form>

            
        </div>
        
    )
}

export default Header