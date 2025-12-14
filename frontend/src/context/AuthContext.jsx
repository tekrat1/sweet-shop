import { createContext, useState } from "react";
import api from "../api/api";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = async (email, password) => {
    const formData = new URLSearchParams();
    formData.append("username", email); // 🔑 FastAPI expects "username"
    formData.append("password", password);

    const res = await api.post("/auth/login", formData, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    localStorage.setItem("access_token", res.data.access_token);
    setUser({ isAdmin: res.data.is_admin });
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
