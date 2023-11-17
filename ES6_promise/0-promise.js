function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      // Simulate an asynchronous API call (you would replace this with your actual API call)
      setTimeout(() => {
        const success = true; // Simulate success or failure
        if (success) {
          resolve("Data from the API"); // Resolve with the data
        } else {
          reject(new Error("Failed to fetch data from the API")); // Reject with an error
        }
      }, 2000); // Simulating a 2-second API call
    });
  }