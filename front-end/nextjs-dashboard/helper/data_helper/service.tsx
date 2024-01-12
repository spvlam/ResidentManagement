export async function getData(url: string) {
    try {
      const response = await fetch(url); // Send a GET request to the specified URL
      if (!response.ok) {
        throw new Error('Failed to fetch data'); // If the response is not OK, throw an error
      }
      const data = await response.json(); // Parse the JSON response
      return data; // Return the data
    } catch (error) {
      console.error('Error fetching data:', error); // Log any errors to the console
      throw error; // Re-throw the error to propagate it to the caller
    }
  }



  