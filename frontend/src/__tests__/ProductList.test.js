// Tests for ProductList
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import ProductList from '../components/ProductList';

const mockProducts = {
  products: [
    {
      id: 1,
      name: 'Sample Product',
      price: '$100',
      rating: 4.5,
      category: 'Electronics',
    },
  ],
  pages: 5,
};

describe('ProductList Component', () => {
  test('renders products in a table', () => {
    render(
      <ProductList
        products={mockProducts}
        error={null}
        page={1}
        totalPages={5}
        onPageChange={jest.fn()}
      />
    );

    expect(screen.getByText(/Sample Product/i)).toBeInTheDocument();
    expect(screen.getByText('$100')).toBeInTheDocument();
    expect(screen.getByText('4.5')).toBeInTheDocument();
    expect(screen.getByText('Electronics')).toBeInTheDocument();
  });

  test('displays error message if error prop is present', () => {
    render(
      <ProductList
        products={mockProducts}
        error="Something went wrong"
        page={1}
        totalPages={5}
        onPageChange={jest.fn()}
      />
    );

    expect(screen.getByText(/Something went wrong/i)).toBeInTheDocument();
  });

  test('shows "No products found!" message when product list is empty', () => {
    render(
      <ProductList
        products={{ products: [] }}
        error={null}
        page={1}
        totalPages={1}
        onPageChange={jest.fn()}
      />
    );

    expect(screen.getByText(/No products found!/i)).toBeInTheDocument();
  });

  test('calls onPageChange when pagination buttons are clicked', () => {
    const mockPageChange = jest.fn();

    render(
      <ProductList
        products={mockProducts}
        error={null}
        page={2}
        totalPages={5}
        onPageChange={mockPageChange}
      />
    );

    fireEvent.click(screen.getByText(/◀ Previous/i));
    fireEvent.click(screen.getByText(/Next ▶/i));

    expect(mockPageChange).toHaveBeenCalledWith(1);
    expect(mockPageChange).toHaveBeenCalledWith(3);
  });

  test('disables prev/first on first page and next/last on last page', () => {
    const { rerender } = render(
      <ProductList
        products={mockProducts}
        error={null}
        page={1}
        totalPages={5}
        onPageChange={jest.fn()}
      />
    );

    expect(screen.getByText(/⏮ First/i)).toBeDisabled();
    expect(screen.getByText(/◀ Previous/i)).toBeDisabled();
    expect(screen.getByText(/Next ▶/i)).not.toBeDisabled();
    expect(screen.getByText(/Last ⏭/i)).not.toBeDisabled();

    rerender(
      <ProductList
        products={mockProducts}
        error={null}
        page={5}
        totalPages={5}
        onPageChange={jest.fn()}
      />
    );

    expect(screen.getByText(/⏮ First/i)).not.toBeDisabled();
    expect(screen.getByText(/◀ Previous/i)).not.toBeDisabled();
    expect(screen.getByText(/Next ▶/i)).toBeDisabled();
    expect(screen.getByText(/Last ⏭/i)).toBeDisabled();
  });
});
