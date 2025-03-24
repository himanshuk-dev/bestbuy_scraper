// Home.jsx
import React, { useEffect, useState } from 'react';
import Filter from '../components/Filter';
import ProductList from '../components/ProductList';
import { fetchAllProducts, fetchProductsByCategory } from '../api/apiClient';
import { Typography, Container } from '@mui/material';

const Home = () => {
  const [products, setProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [page, setPage] = useState(1);

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setPage(1); // reset page
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = selectedCategory
          ? await fetchProductsByCategory(selectedCategory, page)
          : await fetchAllProducts(page);
        setProducts(response);
      } catch (err) {
        console.error('Error fetching data:', err);
      }
    };

    fetchData();
  }, [selectedCategory, page]);

  return (
    <Container>
      <Typography
        variant="h3"
        align="center"
        sx={{ color: 'white', mt: 2, mb: 2 }}
      >
        BestBuy Database
      </Typography>

      <Filter onChange={handleCategoryChange} />
      <ProductList
        products={products}
        page={page}
        totalPages={products?.pages || 1}
        onPageChange={(newPage) => setPage(newPage)}
      />
    </Container>
  );
};

export default Home;
