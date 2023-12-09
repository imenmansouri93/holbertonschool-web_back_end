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

const name = 'HolbertonSchools';
const values = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

for (const [key, val] of Object.entries(values)) {
    client.hset(name, key, val, (error, reply) => 
        redis.print(`Reply: ${reply}`));
}

client.hgetall(name, (error, Object) => console.log(Object));