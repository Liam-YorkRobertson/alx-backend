// check if item is in stock

import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const app = express();
const PORT = 1245;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

app.get('/list_products', (_, res) => {
  res.json(listProducts);
});

const client = redis.createClient();
const reserveStockById = promisify(client.set).bind(client);
const getCurrentReservedStockById = async (itemId) => {
  const stock = await promisify(client.get).bind(client)(`item_${itemId}`);
  return Number(stock) || 0;
};

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = listProducts.find((p) => p.itemId === parseInt(itemId, 10));
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = listProducts.find((p) => p.itemId === parseInt(itemId, 10));
  if (!item) {
    return res.json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(itemId);
  if (currentQuantity >= item.initialAvailableQuantity) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(`item_${itemId}`, currentQuantity + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});
