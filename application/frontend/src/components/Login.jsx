import React, { useState } from "react"
import { login } from "../api/auth.js"

export default function Login({ setToken }) {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = async () => {
    try {
      const data = await login(username, password)
      setToken(data.access_token)
    } catch (err) {
      console.error(err.message)
      alert("Login failed: " + err.message)
    }
  }

  return (
    <div>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button className="button-primary" onClick={handleLogin}>Login</button>
    </div>
  )
}
