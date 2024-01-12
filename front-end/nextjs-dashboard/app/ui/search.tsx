"use client"
import React, { useState } from 'react';
import styles from '@/app/ui/styles/customer.module.css';
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import { getData } from '@/helper/data_helper/service';

interface SearchProps {
  placeholder: string;
}

interface Product {
  full_name: string;
  que_quan_tinh: string;
  dob: string;
  gender: string;
}

export default function Search({ placeholder }: SearchProps) {
  
  const [query, setQuery] = useState('');
  const [products, setProducts] = useState<Product[]>([]); // Use state for products

  const handleInputChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const inputValue = e.target.value;
    setQuery(inputValue);
    // Call the search action here (e.g., make an API request) using the inputValue
    // console.log('Search query:', inputValue);
    try {
      const fetchedProducts = await getData(`http://localhost:8000/search/person/${inputValue}`) as Product[];
      setProducts(fetchedProducts); // Update products state with fetched data
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  return (
    <div className="container">
      <div className="relative flex flex-1 flex-shrink-0">
        <label htmlFor="search" className="sr-only">
          Search
        </label>
        <input
          id="search"
          type="text"
          className="peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500"
          value={query}
          onChange={handleInputChange}
        />
        <MagnifyingGlassIcon className="absolute left-3 top-1/2 h-[18px] w-[18px] -translate-y-1/2 text-gray-500 peer-focus:text-gray-900" />
      </div>
      <div style={{ marginTop: '10px' }} className="max-h-80 ">
        <table className="text-left w-full">
          <thead className="bg-black text-white">
            <tr className={`flex w-full mb-4 sticky top-0`}>
              <th className={`${styles.sticky} p-4 w-1/4`}>HO Va Ten</th>
              <th className={`${styles.sticky} p-4 w-1/4`}>Que Quan</th>
              <th className={`${styles.sticky} p-4 w-1/4`}>Ngay Sinh</th>
              <th className={`${styles.sticky} p-4 w-1/4`}>Gioi Tinh</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr key={index} className="flex w-full mb-4 text-black border-b">
                <td className="p-4 w-1/4">{product.full_name}</td>
                <td className="p-4 w-1/4">{product.que_quan_tinh}</td>
                <td className="p-4 w-1/4">{product.dob}</td>
                <td className="p-4 w-1/4">{`${product.gender}`}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
