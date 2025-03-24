// Dropdown to select a category using Material UI components

import React, { useEffect, useState } from 'react';
import { fetchAllCategories } from '../api/apiClient';
import { Box, InputLabel, MenuItem, FormControl, Select } from '@mui/material';

/**
 * Filter component allows users to select a category from a dropdown.
 * 
 * Props:
 * - onChange: Function to handle category selection change
 */
const Filter = ({ onChange }) => {
  // State to store fetched categories
  const [categories, setCategories] = useState([]);

  // State to track currently selected category
  const [selected, setSelected] = useState('');

  // Fetch categories from backend on component mount
  useEffect(() => {
    const getCategories = async () => {
      try {
        const data = await fetchAllCategories();
        setCategories(data); // Store categories for rendering dropdown
      } catch (error) {
        console.error('Failed to fetch categories:', error.message);
      }
    };
    getCategories();
  }, []);

  // Handle dropdown value change
  const handleChange = (e) => {
    const value = e.target.value;
    setSelected(value);
    onChange(value); // Inform parent component of selected category
  };

  return (
    <Box display="flex" justifyContent="center" mt={3}>
      <FormControl sx={{ minWidth: 300, backgroundColor: 'white' }}>
        {/* Input label for dropdown */}
        <InputLabel
          id="category-select-label"
          sx={{ fontWeight: 'bold', fontSize: '1.4rem', color: '#545863' }}
        >
          Filter by Category
        </InputLabel>

        {/* Category dropdown selector */}
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
