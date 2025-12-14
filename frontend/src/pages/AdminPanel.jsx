import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

export default function AdminPanel() {
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  const [sweets, setSweets] = useState([]);

  // Add sweet form state
  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");

  // 🔐 Admin guard
  useEffect(() => {
    if (!user || !user.isAdmin) {
      navigate("/");
    } else {
      fetchSweets();
    }
  }, [user]);

  // 📥 Fetch sweets
  const fetchSweets = async () => {
    const res = await api.get("/sweets/");
    setSweets(res.data);
  };

  // ➕ ADD SWEET
  const addSweet = async () => {
    await api.post("/sweets", {
      name,
      category,
      price: Number(price),
      quantity: Number(quantity),
    });

    setName("");
    setCategory("");
    setPrice("");
    setQuantity("");
    fetchSweets();
  };

  // ❌ DELETE SWEET
  const deleteSweet = async (id) => {
    await api.delete(`/sweets/${id}`);
    fetchSweets();
  };

  // ✏ UPDATE SWEET (simple example)
  const updateSweet = async (id) => {
    await api.put(`/sweets/${id}`, {
      price: 99, // example update
    });
    fetchSweets();
  };

  return (
    <div>
      <h2>Admin Panel</h2>

      {/* ➕ ADD SWEET FORM */}
      <h3>Add Sweet</h3>

      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        placeholder="Category"
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      />

      <input
        type="number"
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <input
        type="number"
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />

      <button onClick={addSweet}>Add Sweet</button>

      <hr />

      {/* 📋 SWEET LIST */}
      <h3>All Sweets</h3>

      {sweets.map((s) => (
        <div key={s.id} style={{ marginBottom: "10px" }}>
          <b>{s.name}</b> — ₹{s.price} — Stock: {s.quantity}

          <br />

          <button onClick={() => updateSweet(s.id)}>Update Price</button>
          <button onClick={() => deleteSweet(s.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
