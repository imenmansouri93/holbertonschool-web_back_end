import redis from 'redis';
import { promisify } from 'util';
// Create a Redis client
const client = redis.createClient();

// Convert callback-based functions to promise-based functions
const getAsync = promisify(client.get).bind(client);

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
const displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName);
        console.log(`${value}`);
    } catch (error) {
        console.error(`${err.message}`);
    }
};

setNewSchool('HolbertonSanFrancisco', '100');
(async () => {
    await displaySchoolValue('Holberton');
    await displaySchoolValue('HolbertonSanFrancisco');

    // Gracefully close the Redis connection when the script is terminated
    process.on('SIGINT', () => {
        client.quit();
    });
})();