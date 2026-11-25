# MongoDB + PostgreSQL pgvector Assignment

## Overview
This project demonstrates MongoDB operations using PyMongo and vector similarity search using PostgreSQL with the pgvector extension.

## 1. MongoDB (PyMongo)

### Tasks Completed
- Connected Python to MongoDB using PyMongo.
- Inserted 5 employee records using `insert_one()` and `insert_many()`.
- Retrieved employees based on department.
- Updated an employee's salary using `update_one()`.
- Used aggregation with `$match` and `$group` to calculate average salary by department.
- Used `$lookup` to combine employee and department information.

### Database Details
- Database: `hr_task2`
- Collections: `employees`, `departments`

## 2. PostgreSQL (pgvector)

### Tasks Completed
- Installed and enabled the pgvector extension.
- Created a table with a `VECTOR(3)` column.
- Inserted 4 records with vector embeddings.
- Used the `<->` operator to calculate Euclidean distance.
- Retrieved the nearest vector to `[1,2,3]`.

### SQL Example
```sql
SELECT id, name, embedding,
       embedding <-> '[1,2,3]' AS distance
FROM items
ORDER BY embedding <-> '[1,2,3]'
LIMIT 1;
```

### Expected Result
- Nearest item: Item A
- Distance: 0

## 3. MongoDB vs PostgreSQL for an HR System

- MongoDB is useful for flexible employee records with changing fields.
- MongoDB can store resumes, skills, and project details.
- PostgreSQL is suitable for structured HR data such as salaries and attendance.
- PostgreSQL provides relationships, transactions, and data consistency.
- MongoDB is suitable for flexible data, while PostgreSQL is better for structured data and reliable transactions.

## Technologies Used
- Python
- PyMongo
- MongoDB
- PostgreSQL 19
- pgvector
- VS Code
- pgAdmin 4

## Project Files
- `mongodb_task.py` – MongoDB operations using Python.
- `pgvector_task.sql` – PostgreSQL and pgvector queries.
- `README.md` – Project documentation.
- `Screenshots/` – Task execution screenshots.

## Conclusion
Successfully completed MongoDB CRUD operations, aggregation, lookup, and PostgreSQL vector similarity search using pgvector.
