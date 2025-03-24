// Home.jsx
import React, { useEffect, useState } from 'react';
import Filter from '../components/Filter';
import ProductList from '../components/ProductList';
import Loading from '../components/Loading';
import { fetchAllProducts, fetchProductsByCategory } from '../api/apiClient';
import { Typography, Container } from '@mui/material';

const Home = () => {
  const [products, setProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('')

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setPage(1);
  };

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true); // start loading
      try {
        const response = selectedCategory
          ? await fetchProductsByCategory(selectedCategory, page)
          : await fetchAllProducts(page);
        setProducts(response);
      } catch (err) {
        console.error('Error fetching data:', err);
        setError(err)
      } finally {
        setLoading(false); // stop loading
      }
    };

    fetchData();
  }, [selectedCategory, page]);

  return (
    <Container>
      <Typography variant="h3" align="center" sx={{ color: 'white', mt: 2, mb: 2 }}>
        BestBuy Database
      </Typography>

      <Filter onChange={handleCategoryChange} />
      
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
