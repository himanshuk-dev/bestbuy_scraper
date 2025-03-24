// Dropdown to select a category.

import React, { useEffect, useState } from 'react';
import { fetchAllCategories } from '../api/apiClient';

const Filter = ({ onChange }) => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const getCategories = async () => {
      try {
        const data = await fetchAllCategories();
        setCategories(data);
      } catch (error) {
        console.error('Failed to fetch categories:', error.message);
      }
    };

    getCategories();
  }, []);

  const handleChange = (e) => {
    onChange(e.target.value);
  };

  return (
    <div style={{ margin: '1rem 3rem', textAlign:'center', color:'wheat', fontSize:'2vh' }}>
      <label htmlFor="category-select" style={{ marginRight: '1rem' }}>
        Filter by Category:
      </label>
      <select id="category-select" onChange={handleChange} style={{padding:'1.3vh', textAlign:'center', fontSize:'1rem'}}>
        <option value="">All</option>
        {categories.map((cat) => (
          <option key={cat} value={cat}>{cat}</option>
        ))}
      </select>
    </div>
  );
};

export default Filter;