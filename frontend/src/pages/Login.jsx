import React, {useState} from 'react'
import API from '../api'

export default function Login(){
  const [username,setUsername]=useState('')
  const [password,setPassword]=useState('')
  const [err,setErr]=useState('')
  const submit = async (e)=>{
    e.preventDefault()
    try{
      const res = await API.post('/token/', {username, password})
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
      window.location = '/'
    }catch(err){
      setErr('Login failed. Check credentials.')
    }
  }
  return (<div style={{padding:20}}>
    <h2>Login</h2>
    <form onSubmit={submit}>
      <div><input placeholder="username" value={username} onChange={e=>setUsername(e.target.value)} /></div>
      <div><input placeholder="password" type="password" value={password} onChange={e=>setPassword(e.target.value)} /></div>
      <button type="submit">Login</button>
    </form>
    {err && <p style={{color:'red'}}>{err}</p>}
  </div>)
}
