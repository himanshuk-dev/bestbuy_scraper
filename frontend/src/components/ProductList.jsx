// Displays products in a table.

import React from 'react';

const ProductList = ({ products, onDelete, loading, error }) => {
  if (loading) return <p>Loading products...</p>;
  if (error) return <p style={{ color: 'red' }}>⚠️ {error}</p>;
  if (!products.length) return <p>No products found.</p>;

  return (
    <div style={{ display: 'grid', gap: '1rem' }}>
      {products.map((product) => (
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
          {/* {onDelete && (
            <button
              onClick={() => onDelete(product.id)}
              style={{
                backgroundColor: '#ff5252',
                color: '#fff',
                border: 'none',
                padding: '0.5rem 1rem',
                borderRadius: '4px',
                cursor: 'pointer'
              }}
            >
              Delete
            </button>
          )} */}
        </div>
      ))}
    </div>
  );
};

export default ProductList;
