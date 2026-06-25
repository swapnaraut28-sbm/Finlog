import { useState , useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
const [message, setMessage] = useState("Connecting to backend...")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/health")
      .then(res => res.json())
      .then(data => setMessage(data.status))
      .catch(err => setMessage("Failed to connect to backend."));
  }, [])

 return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', fontFamily: 'sans-serif' }}>
      <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px', textAlign: 'center' }}>
        <h1>PyStack Pilot Dashboard 🚀</h1>
        <p style={{ color: message.includes('running') ? 'green' : 'red', fontWeight: 'bold' }}>
          {message}
        </p>
      </div>
    </div>
  )
}

export default App
