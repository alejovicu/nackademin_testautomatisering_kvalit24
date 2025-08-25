import React, { useState, useEffect } from "react";
import Signup from "./components/Signup.jsx";
import Login from "./components/Login.jsx";
import { api } from "./api.js";

export default function App() {
  const [token, setToken] = useState(() => localStorage.getItem("token") || null);
  const [user, setUser] = useState(null);
  const [screen, setScreen] = useState("login"); // "login" or "signup"
  const [newProductName, setNewProductName] = useState("");
  const [allProducts, setAllProducts] = useState([]); // For admin

  // Fetch current user after login
  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);

      const fetchUser = async () => {
        try {
          const data = await api("/user", "GET", null, token);
          setUser(data);

          // If admin, fetch all products
          if (data.id === 1) {
            const products = await api("/products", "GET", null, token);
            setAllProducts(products);
          }
        } catch (err) {
          console.error("Failed to fetch user:", err.message);
        }
      };

      fetchUser();
    } else {
      localStorage.removeItem("token");
      setUser(null);
      setAllProducts([]);
    }
  }, [token]);

  // Logout function
  const handleLogout = () => {
    setToken(null);
    setUser(null);
    setAllProducts([]);
    setScreen("login");
  };

  // Admin-only: create new product
  const handleCreateProduct = async () => {
    if (!newProductName) return;
    try {
      const product = await api("/products", "POST", { name: newProductName }, token);
      setAllProducts((prev) => [...prev, product]);
      setNewProductName("");
    } catch (err) {
      alert("Failed to create product: " + err.message);
    }
  };

  // Admin-only: delete product
  const handleDeleteProduct = async (id) => {
    try {
      await api(`/product/${id}`, "DELETE", null, token);
      setAllProducts((prev) => prev.filter((p) => p.id !== id));
    } catch (err) {
      alert("Failed to delete product: " + err.message);
    }
  };

  // Before login: show Login or Signup screen
  if (!token) {
    return (
      <div>
        <h1>Nackademin Course App</h1>
        {screen === "login" ? (
          <>
            <Login setToken={setToken} />
            <p>
              Don't have an account?{" "}
              <button onClick={() => setScreen("signup")}>Sign Up</button>
            </p>
          </>
        ) : (
          <>
            <Signup />
            <p>
              Already have an account?{" "}
              <button onClick={() => setScreen("login")}>Login</button>
            </p>
          </>
        )}
      </div>
    );
  }

  // After login but user info still loading
  if (!user) return <p>Loading user info...</p>;

  // After login and user loaded
  return (
    <div>
      <h1>Nackademin Course App</h1>
      <button onClick={handleLogout} style={{ marginBottom: "10px" }}>
        Logout
      </button>

      <h2>Welcome, {user.username}!</h2>

      {user.id === 1 ? (
        // Admin view: all products
        <div>
          <h3>All Products:</h3>
          {allProducts.length === 0 ? (
            <p>No products available.</p>
          ) : (
<div
  style={{
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(150px, 1fr))",
    gap: "10px",
  }}
>
  {allProducts.map((product) => (
    <div
      key={product.id}
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        borderRadius: "5px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
      }}
    >
      <span>{product.name}</span>
      <button
        onClick={() => handleDeleteProduct(product.id)}
        style={{ padding: "2px 5px", fontSize: "0.8rem" }}
      >
        Delete
      </button>
    </div>
  ))}
</div>
          )}

          <div style={{ marginTop: "20px" }}>
            <h3>Admin: Add New Product</h3>
            <input
              type="text"
              placeholder="Product Name"
              value={newProductName}
              onChange={(e) => setNewProductName(e.target.value)}
            />
            <button onClick={handleCreateProduct}>Create Product</button>
          </div>
        </div>
      ) : (
        // Normal user view: assigned products only
        <div>
          <h3>Your Products:</h3>
          {user.products.length === 0 ? (
            <p>No products assigned.</p>
          ) : (
            <div
              style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fill, minmax(150px, 1fr))",
                gap: "10px",
              }}
            >
              {user.products.map((product) => (
                <div
                  key={product.id}
                  style={{
                    border: "1px solid #ccc",
                    padding: "10px",
                    borderRadius: "5px",
                  }}
                >
                  {product.name}
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
