// Displays products in a styled Material UI table with pagination controls

import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Button,
  Box,
  Stack
} from '@mui/material';

/**
 * ProductList component displays a paginated table of products.
 *
 * Props:
 * - products: Object containing an array of products and pagination info
 * - error: Error message to display if fetching fails
 * - onPageChange: Function to handle page change
 * - page: Current page number
 * - totalPages: Total number of pages available
 */
const ProductList = ({ products, error, onPageChange, page, totalPages }) => {
  // Display error message if any error occurred while fetching
  if (error) {
    return (
      <Typography
        color="error"
        sx={{ textAlign: 'center', marginTop: 10, fontSize: '2rem' }}
      >
        ⚠️ {error}
      </Typography>
    );
  }

  // Show message when no products are available
  if (!products || products.products.length === 0) {
    return (
      <Typography
        sx={{ textAlign: 'center', marginTop: 10, fontSize: '2rem', color: 'red' }}
      >
        No products found!
      </Typography>
    );
  }

  return (
    <Box sx={{ justifyItems: 'center' }}>
      {/* Table displaying products */}
      <TableContainer component={Paper} sx={{ margin: 4, maxWidth: '100%' }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><strong>Name</strong></TableCell>
              <TableCell><strong>Price</strong></TableCell>
              <TableCell><strong>Rating</strong></TableCell>
              <TableCell><strong>Category</strong></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {products.products.map((product) => (
              <TableRow key={product.id}>
                <TableCell sx={{ maxWidth: '40vh', padding: 1.2 }}>{product.name}</TableCell>
                <TableCell sx={{ maxWidth: '10vh', padding: 1.2 }}>{product.price}</TableCell>
                <TableCell sx={{ maxWidth: '10vh', padding: 1.2 }}>{product.rating ?? '0'}</TableCell>
                <TableCell sx={{ maxWidth: '1vh', padding: 1.2 }}>{product.category}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      {/* Pagination controls */}
      <Box
        display="flex"
        justifyContent="center"
        sx={{
          backgroundColor: 'white',
          padding: '1rem',
          maxWidth: '90vh',
          borderRadius: 2
        }}
      >
        <Stack direction="row" spacing={2} alignItems="center">
          <Button
            variant="contained"
            color="primary"
            onClick={() => onPageChange(1)}
            disabled={page === 1}
          >
            ⏮ First
          </Button>

          <Button
            variant="outlined"
            onClick={() => onPageChange(page - 1)}
            disabled={page <= 1}
          >
            ◀ Previous
          </Button>

          <Typography variant="body1">
            Page <strong>{page}</strong> of <strong>{totalPages}</strong>
          </Typography>

          <Button
            variant="outlined"
            onClick={() => onPageChange(page + 1)}
            disabled={page >= totalPages}
          >
            Next ▶
          </Button>

          <Button
            variant="contained"
            color="primary"
            onClick={() => onPageChange(totalPages)}
            disabled={page === totalPages}
          >
            Last ⏭
          </Button>
        </Stack>
      </Box>
    </Box>
  );
};

export default ProductList;
