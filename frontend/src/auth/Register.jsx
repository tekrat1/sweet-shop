import api from "../api/api";
import { useState } from "react";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const submit = async () => {
    await api.post("/auth/register", { email, password });
    alert("Registered successfully");
  };

  return (
    <div>
      <h2>Register</h2>
      <input onChange={e => setEmail(e.target.value)} />
      <input type="password" onChange={e => setPassword(e.target.value)} />
      <button onClick={submit}>Register</button>
    </div>
  );
}
