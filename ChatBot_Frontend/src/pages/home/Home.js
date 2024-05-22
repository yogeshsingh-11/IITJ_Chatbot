import React, { useEffect , useState } from 'react'
import './home.css'
import ChatBotLogo from '../../assets/images/chatbot.png'
import Message from './Message';

const Home = () => {
    const [query,updateQuery] = useState('');
    const [messages, setMessages] = useState([
        {
            id: 1,
            text: "Hello, Welcome to IITJ Chat Bot",
            type: 0,
        },
    ]);

    useEffect(() => {
        const fetchBotResponse = async () => {
            if (messages.length > 1) {
                const lastMessage = messages[messages.length - 1];
                if (lastMessage.type === 1) {
                    const trimmedQuery = query.trim();
                    const url = "http://localhost:8000/api/getbotresponse";
    
                    const response = await fetch(url, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'text/plain',
                        },
                        body: trimmedQuery,
                    });
    
                    const responseData = await response.json();
                    const ans = responseData.result;
                    if (ans) {
                        addMessage(ans, 0);
                    }
                    updateQuery('');
                }
            }
        };
    
        fetchBotResponse();
    
    }, [messages]);

    const sendQuery = async ()=>{
        const trimmedQuery = query.trim();

        if(trimmedQuery){
            addMessage(trimmedQuery , 1)
        }
    }
    const addMessage = (text, type) => {
        const newMessage = { id: messages.length + 1, text, type };
        setMessages([...messages, newMessage]);
    };
    
    return (
        <div className='mainContainer'>
            <div className="mainBox">

                <div className="header">
                    <div className="headerNameBox">
                        <img src={ChatBotLogo} alt="" className='chatBotLogo' />
                        <div className='headerName'>
                            ChatBot
                        </div>
                    </div>
                </div>

                <div className="mainMessageBox">
                    {messages.map((message) => (
                        <Message key={message.id} text={message.text} type={message.type} />
                    ))}
                    {/* <Message text={"This is message right"} type={1}/>
                    <Message text={"This is message left"} type={0}/>                  */}
                </div>

                <div className="mainQueryBox">
                    <input className="queryBox" placeholder='Write your query here...' value={query} onChange={(e)=>updateQuery(e.target.value)}></input>
                    <button onClick={()=>sendQuery()}>
                        <div class="svg-wrapper-1">
                            <div class="svg-wrapper">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 24 24"
                                width="24"
                                height="24"
                            >
                                <path fill="none" d="M0 0h24v24H0z"></path>
                                <path
                                fill="currentColor"
                                d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                                ></path>
                            </svg>
                            </div>
                        </div>
                        <span>Send</span>
                    </button>

                </div>

            </div>
        </div>
  )
}

export default Home
