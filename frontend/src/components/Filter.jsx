// Dropdown to select a category.

import React, { useEffect, useState } from 'react';
import { fetchAllCategories } from '../api/apiClient';
import { Box, InputLabel, MenuItem, FormControl, Select } from '@mui/material';

const Filter = ({ onChange }) => {
  const [categories, setCategories] = useState([]);
  const [selected, setSelected] = useState('');

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
    const value = e.target.value;
    setSelected(value);
    onChange(value);
  };

  return (
    <Box display="flex" justifyContent="center" mt={3}>
      <FormControl sx={{ minWidth: 300, backgroundColor: 'white' }}>
        <InputLabel id="category-select-label" sx={{ fontWeight: 'bold' ,fontSize:'1.4rem', color: '#545863'}} color='blue'>Filter by Category</InputLabel>
        <Select
          labelId="category-select-label"
          id="category-select"
          value={selected}
          label="Filter by Category"
          onChange={handleChange}
        >
          <MenuItem value="">All</MenuItem>
          {categories.map((cat) => (
            <MenuItem key={cat} value={cat}>
              {cat}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
};

export default Filter;
