// A simple loading screen with a spinner and message using Material UI

import React from 'react';
import { CircularProgress, Box, Typography } from '@mui/material';

/**
 * Loading component to display a spinner with an optional message.
 * Useful while fetching data asynchronously.
 *
 * Props:
 * - message (string): Optional message to display below the spinner. Defaults to "Loading products..."
 */
const Loading = ({ message = "Loading products..." }) => {
  return (
    <Box
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
      mt={6} // Top margin for spacing
    >
      {/* Circular loading spinner */}
      <CircularProgress />

      {/* Loading message below the spinner */}
      <Typography
        variant="body1"
        mt={2}
        sx={{ color: 'white', fontSize: '2rem' }}
      >
        {message}
      </Typography>
    </Box>
  );
};

export default Loading;
