// This component serves as the main landing page.
// It allows filtering products by category, paginating the results, and handles loading/error UI.

import React, { useEffect, useState } from 'react';
import Filter from '../components/Filter';                    
import ProductList from '../components/ProductList';          
import Loading from '../components/Loading';                  
import { fetchAllProducts, fetchProductsByCategory } from '../api/apiClient';
import { Typography, Container } from '@mui/material';

const Home = () => {
  // Local state to store fetched products
  const [products, setProducts] = useState([]);
  // Track selected category from Filter dropdown
  const [selectedCategory, setSelectedCategory] = useState('');
  // Track current pagination page
  const [page, setPage] = useState(1);
  // Manage loading state for UX
  const [loading, setLoading] = useState(true);
  // Capture error messages if any API call fails
  const [error, setError] = useState('');

  /**
   * Callback passed to Filter component to handle category changes.
   * Resets page to 1 on category switch.
   */
  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setPage(1); // Reset to page 1 when changing categories
  };

  /**
   * useEffect triggers when selectedCategory or page changes.
   * Fetches product data from backend API and updates local state.
   */
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true); // Start loading UI
      try {
        const response = selectedCategory
          ? await fetchProductsByCategory(selectedCategory, page)
          : await fetchAllProducts(page);
        setProducts(response); 
        setError(''); 
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err); 
      } finally {
        setLoading(false); 
      }
    };

    fetchData();
  }, [selectedCategory, page]);

  return (
    <Container>
      {/* Page Heading */}
      <Typography variant="h3" align="center" sx={{ color: 'white', mt: 2, mb: 2 }}>
        BestBuy Database
      </Typography>

      {/* Dropdown Filter */}
      <Filter onChange={handleCategoryChange} />
      
      {/* Conditional rendering: show spinner or product table */}
      {loading ? (
        <Loading />
      ) : (
        <ProductList
          products={products}
          error={error.message}
          page={page}
          totalPages={products?.pages || 1}
          onPageChange={(newPage) => setPage(newPage)}
        />
      )}
    </Container>
  );
};

export default Home;
