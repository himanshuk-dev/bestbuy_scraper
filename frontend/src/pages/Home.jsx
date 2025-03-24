// Home.jsx
import React, { useEffect, useState } from 'react';
import Filter from '../components/Filter';
import ProductList from '../components/ProductList';
import { fetchAllProducts, fetchByCategory } from '../api/apiClient';

const Home = () => {
  const [products, setProducts] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [page, setPage] = useState(1);

  const handleCategoryChange = async (category) => {
    setSelectedCategory(category);
    setPage(1); // reset page
  };

  const fetchData = async () => {
    try {
      const response = selectedCategory
        ? await fetchByCategory(selectedCategory, page)
        : await fetchAllProducts(page);
      setProducts(response.data.products);
    } catch (err) {
      console.error('Error fetching data:', err);
    }
  };

  useEffect(() => {
    fetchData();
  }, [selectedCategory, page]);

  return (
    <div>
      <Filter onChange={handleCategoryChange} />
      <ProductList products={products} />
    </div>
  );
};

export default Home;
