CREATE EXTENSION vector;

SELECT version();

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    embedding VECTOR(3)
);     

INSERT INTO items (name, embedding)
VALUES
('Item A', '[1,2,3]'),
('Item B', '[2,3,4]'),
('Item C', '[1,1,1]'),
('Item D', '[5,5,5]');

SELECT
    id,
    name,
    embedding,
    embedding <-> '[1,2,3]' AS distance
FROM items
ORDER BY embedding <-> '[1,2,3]'
LIMIT 1;

SELECT * FROM items;