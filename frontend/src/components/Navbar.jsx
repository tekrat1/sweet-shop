import { Link } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useContext(AuthContext);

  return (
    <nav>
      <Link to="/">Home</Link>

      {!user && (
        <>
          {" | "}
          <Link to="/login">Login</Link>
          {" | "}
          <Link to="/register">Register</Link>
        </>
      )}

      {user?.isAdmin && (
        <>
          {" | "}
          <Link to="/admin">Admin</Link>
        </>
      )}

      {user && (
        <>
          {" | "}
          <button onClick={logout}>Logout</button>
        </>
      )}
    </nav>
  );
}
