// ProductList.jsx
import React from 'react';

const ProductList = ({ products, loading, error, onPageChange, page, totalPages }) => {
  if (loading) return <p>Loading products...</p>;
  if (error) return <p style={{ color: 'red' }}>⚠️ {error}</p>;
  if (!products || products.length === 0) return <p>No products found.</p>;

  return (
    <div >
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
    </div>
     <div style={{ margin: '1rem', display: 'flex', gap: '1rem', backgroundColor: 'white', padding:'1rem', width:'30rem'}}>
     <button onClick={() => onPageChange(page - 1)} disabled={page <= 1}>
       ◀ Previous
     </button>
     <span>
       Page <strong>{page}</strong> of <strong>{totalPages}</strong>
     </span>
     <button onClick={() => onPageChange(page + 1)} disabled={page >= totalPages}>
       Next ▶
     </button>
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
