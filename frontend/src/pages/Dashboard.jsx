import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/api";
import SweetCard from "../components/SweetCard";

export default function Dashboard() {
  const [sweets, setSweets] = useState([]);
  const navigate = useNavigate();

  const fetchAllSweets = async () => {
    try {
      const res = await api.get("/sweets/");
      setSweets(res.data);
    } catch (err) {
      if (err.response?.status === 401) {
        navigate("/login");
      } else {
        console.error("Fetch sweets error:", err);
      }
    }
  };

  const purchaseSweet = async (id) => {
    await api.post(`/sweets/${id}/purchase/`);
    fetchAllSweets();
  };

  useEffect(() => {
    fetchAllSweets();
  }, []);

  return (
    <div>
      <h2>Available Sweets</h2>

      {sweets.length === 0 && <p>No sweets found</p>}

      {sweets.map((sweet) => (
        <SweetCard
          key={sweet.id}
          sweet={sweet}
          onPurchase={purchaseSweet}
        />
      ))}
    </div>
  );
}

