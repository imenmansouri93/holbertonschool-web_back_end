import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// setNewSchool function
const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
  };

// displaySchoolValue function
const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, value) => {
      if (err) {
        console.error(`${err.message}`);
      } else {
        console.log(`${value}`);
      }
    });
  };

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');