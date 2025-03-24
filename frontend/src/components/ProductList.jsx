// Displays products in a table.

// ProductList.jsx
import React from 'react';

const ProductList = ({ products, onDelete, loading, error }) => {
  if (loading) return <p>Loading products...</p>;
  if (error) return <p style={{ color: 'red' }}>⚠️ {error}</p>;
  if (products.length === 0) return <p>No products found.</p>;

  console.log('products', products);

  return (
    <div style={{ margin: '3rem', backgroundColor: 'white' }}>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f5f5f5' }}>
            <th style={thStyle}>Name</th>
            <th style={thStyle}>Price</th>
            <th style={thStyle}>Rating</th>
            <th style={thStyle}>Category</th>
          </tr>
        </thead>
        <tbody>
          {products.products.map((product) => (
            <tr key={product.id}>
              <td style={tdStyle}>{product.name}</td>
              <td style={tdStyle}>{product.price}</td>
              <td style={tdStyle}>{product.rating ?? 'N/A'}</td>
              <td style={tdStyle}>{product.category}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div style={{ marginTop: '1rem' }}>
        <p>
          Page <strong><input defaultValue={products.page}></input></strong> of <strong>{products.pages}</strong>
        </p>
      </div>
    </div>
  );
};

const thStyle = {
  padding: '10px',
  border: '1px solid #ddd',
  textAlign: 'left',
};

const tdStyle = {
  padding: '10px',
  border: '1px solid #eee',
};

export default ProductList;
