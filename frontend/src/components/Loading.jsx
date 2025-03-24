// Loading screen before data is loaded


import React from 'react';
import { CircularProgress, Box, Typography } from '@mui/material';

const Loading = ({ message = "Loading products..." }) => {
  return (
    <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" mt={6}>
      <CircularProgress />
      <Typography variant="body1" mt={2} sx={{color: 'white', fontSize: '2rem'}}>{message}</Typography>
    </Box>
  );
};

export default Loading;
