import kue from 'kue';

const queue = kue.createQueue();

const joby = {
    phoneNumber: '21626990456',
    message: 'verify your account',
};

const queueName = 'push_notification_code';

const job = queue.create(queueName, joby).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});