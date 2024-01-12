import styles from '@/app/ui/styles/customer.module.css'; // Import styles from the specified module
import Search from '@/app/ui/search';
import {getData} from '@/helper/data_helper/service'

// Define the structure of a Product
interface Product {
  name: string;
  color: string;
  category: string;
  price: number;
}

// Define the props for the ProductTable component
interface ProductTableProps {
  products: Product[];
}

// Function to fetch data from the API
// async function getData(url: string): Promise<Product[]> {
//   try {
//     const response = await fetch(url); // Send a GET request to the specified URL
//     if (!response.ok) {
//       throw new Error('Failed to fetch data'); // If the response is not OK, throw an error
//     }
//     const data = await response.json(); // Parse the JSON response
//     return data as Product[]; // Return the data as an array of Product objects
//   } catch (error) {
//     console.error('Error fetching data:', error); // Log any errors to the console
//     throw error; // Re-throw the error to propagate it to the caller
//   }
// }

// ProductTable component
async function ProductTable(){
  let products = await getData("http://localhost:8000/") as Product[]
  return (
    <div className="container">
       <Search placeholder="Search..."  />
      
    </div>
  );
};

export default ProductTable;
