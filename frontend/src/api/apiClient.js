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
export const fetchAllProducts = (page = 1, perPage = 10) =>
  apiClient.get(`/?page=${page}&per_page=${perPage}`);

// Fetch products by category
export const fetchProductsByCategory = (category, page = 1, perPage = 10) =>
  apiClient.get(`/category/${encodeURIComponent(category)}?page=${page}&per_page=${perPage}`);

// Delete a product by ID
export const deleteProduct = (id) =>
  apiClient.delete(`/${id}`);
