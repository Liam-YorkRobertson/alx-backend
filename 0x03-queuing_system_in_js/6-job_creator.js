// creates job creator with kue

import kue from 'kue';

const queue = kue.createQueue();

const jobInfo = {
  phoneNumber: '1234567890',
  message: 'Hello, beep boop',
};

const job = queue.create('push_notification_code', jobInfo);

job.save(() => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
