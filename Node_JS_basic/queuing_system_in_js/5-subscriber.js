import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient();

// Event listener for successful connection
subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Event listener for connection errors
subscriber.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the "holberton school channel"
const channel = 'holberton school channel';
subscriber.subscribe(channel);

subscriber.on('message', (receivedChannel, message) => {
    console.log(`${receivedChannel}: ${message}`);


    // Check if the message is "KILL_SERVER"
    if (message === 'KILL_SERVER') {
        // Unsubscribe and quit
        subscriber.unsubscribe(channel);
        subscriber.quit();
    }
})