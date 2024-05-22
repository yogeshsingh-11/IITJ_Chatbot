import React, { useEffect, useRef } from 'react'
import gsap from 'gsap';
import { TextPlugin } from 'gsap/all';
import './message.css'

gsap.registerPlugin(TextPlugin);

const Message = ({id, text, type}) => {
    const textref = useRef()

    useEffect(() => {
        const element = textref.current;
        gsap.to(element, {
            text: { 
                value: text,
                delimiter: "",
                speed: 1,
            },
            ease: "",
        });
      }, [text]);

      return (
        <div className="messageContainer">
          {type === 1 && (
            <div className='hiddenBox'></div>
          )}
          <div id={id} className={type === 0 ? 'messageAreaLeft' : 'messageAreaRight'} ref={textref}></div>
          {type === 0 && (
            <div className='hiddenBox'></div>
          )}
        </div>
      ); 
}

export default Message
