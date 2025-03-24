// API helper for API requests

import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000/data'; 

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Fetch all products with optional pagination
export const fetchAllProducts = async (page = 1, perPage = 10) => {
    try {
      const response = await apiClient.get(`/?page=${page}&per_page=${perPage}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching all products:', error.message);
      throw error;
    }
  };
  
  // Fetch products by category
  export const fetchProductsByCategory = async (category, page = 1, perPage = 10) => {
    try {
      const response = await apiClient.get(`/category/${encodeURIComponent(category)}?page=${page}&per_page=${perPage}`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching products for category "${category}":`, error.message);
      throw error;
    }
  };
  
  // Delete a product by ID
  export const deleteProduct = async (id) => {
    try {
      const response = await apiClient.delete(`/${id}`);
      return response.data;
    } catch (error) {
      console.error(`Error deleting product with ID ${id}:`, error.message);
      throw error;
    }
  };