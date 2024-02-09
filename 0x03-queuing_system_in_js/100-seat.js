// seat reservation system

const express = require('express');
const redis = require('redis');
const kue = require('kue');

const app = express();
const PORT = 1245;
const client = redis.createClient();
const queue = kue.createQueue();
let availableSeats = 50;
let reservationEnabled = true;
client.set('available_seats', availableSeats);

app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));

app.get('/available_seats', (_, res) => {
  client.get('available_seats', (_, seats) => {
    const numberOfAvailableSeats = seats ? +seats : 0;
    res.json({ numberOfAvailableSeats });
  });
});

app.get('/reserve_seat', (_, res) => {
  if (!reservationEnabled) return res.json({ status: 'Reservation are blocked' });
  queue.create('reserve_seat').save((err) => {
    if (err) return res.json({ status: 'Reservation failed' });
    res.json({ status: 'Reservation in process' });
  });
});

app.get('/process', (_, res) => {
  res.json({ status: 'Queue processing' });
  queue.process('reserve_seat', (job, done) => {
    client.get('available_seats', (_, seats) => {
      if (+seats === 0) {
        reservationEnabled = false;
        return done(new Error('Not enough seats available'));
      }
      availableSeats--;
      client.set('available_seats', availableSeats);
      if (availableSeats === 0) reservationEnabled = false;
      console.log(`Seat reservation job ${job.id} completed`);
      done();
    });
  });
});
