// tests job

import {
  before, after, beforeEach, describe, it,
} from 'mocha';
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  beforeEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should display error if not array', () => {
    const invalidJobs = {};
    expect(() => createPushNotificationsJobs(invalidJobs, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to queue', () => {
    const jobs = [
      { phoneNumber: '0123456789', message: 'This is the code 0123 to verify your account' },
      { phoneNumber: '9876543210', message: 'This is the code 9876 to verify your account' },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should create jobs with correct data', () => {
    const jobs = [
      { phoneNumber: '0123456789', message: 'This is the code 0123 to verify your account' },
      { phoneNumber: '9876543210', message: 'This is the code 9876 to verify your account' },
    ];
    createPushNotificationsJobs(jobs, queue);
    queue.testMode.jobs.forEach((job, index) => {
      expect(job.data).to.deep.equal(jobs[index]);
    });
  });
});
