// Displays products in a table.

import React from 'react';

const ProductList = ({ products, onDelete, loading, error }) => {
  if (loading) return <p>Loading products...</p>;
  if (error) return <p style={{ color: 'red' }}>⚠️ {error}</p>;
  if (products.length === 0) return <p>No products found.</p>;
  return (
    <div style={{ display: 'grid', gap: '1rem' }}>
      {products.products.map((product) => (
        <div
          key={product.id}
          style={{
            border: '1px solid #ccc',
            padding: '1rem',
            borderRadius: '8px',
            background: '#fafafa',
          }}
        >
          <h3>{product.name}</h3>
          <p><strong>Price:</strong> {product.price}</p>
          <p><strong>Rating:</strong> {product.rating ?? 'N/A'}</p>
          <p><strong>Category:</strong> {product.category}</p>
        </div>
      ))}
      <p>Page <input defaultValue={products.page}></input> of {products.pages}</p>
    </div>
  );
};

export default ProductList;
