import React, { useState } from "react"
import { signup } from "../api/auth.js"

export default function Signup() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleSignup = async () => {
    try {
      const user = await signup(username, password)
    } catch (err) {
      console.error(err.message)
      alert("Signup failed: " + err.message)
    }
  }

  return (
    <div>
      <h2>Signup</h2>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button onClick={handleSignup}>Sign Up</button>
    </div>
  )
}
