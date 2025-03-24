// Home.jsx
import React, { useEffect, useState } from 'react';
import Filter from '../components/Filter';
import ProductList from '../components/ProductList';
import { fetchAllProducts, fetchProductsByCategory } from '../api/apiClient';

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
  }, [selectedCategory, page]); // Include dependencies

  return (
    <div>
      <h1 style={{ textAlign:'center', color:'white', fontSize:'8vh' }}>BestBuy Database</h1>
      <Filter onChange={handleCategoryChange} />
      <ProductList
  products={products}
  // loading={loading}
  // error={error}
  page={page}
  totalPages={products?.pages || 1}
  onPageChange={(newPage) => setPage(newPage)}
/>

    </div>
  );
};

export default Home;
