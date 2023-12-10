function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

    const queueName = 'push_notification_code_3';

    jobs.forEach((joby) => {
        const job = queue.create(queueName, joby).save((err) => {
            if (!err) console.log(`Notification job created: ${job.id}`);
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        });

        job.on('failed', (errMessage) => {
            console.log(`Notification job ${job.id} failed: ${errMessage}`);
        });

        job.on('progress', (process) => {
            console.log(`Notification job ${job.id} ${process}% complete`)
        });
    });
}

export default createPushNotificationsJobs;