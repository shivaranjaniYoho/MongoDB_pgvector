
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Test the connection
client.admin.command("ping")
print("MongoDB connected successfully!")

# Select database
db = client["hr_task2"]

# Create collections
employees = db["employees"]
departments = db["departments"]

# Clear old practice data
employees.delete_many({})
departments.delete_many({})

# Insert one employee using insert_one()
employees.insert_one({
    "name": "Arun",
    "department": "IT",
    "department_id": 1,
    "salary": 60000
})

print("First employee inserted successfully!")

# Insert remaining employees using insert_many()
employees.insert_many([
    {
        "name": "Bala",
        "department": "HR",
        "department_id": 2,
        "salary": 45000
    },
    {
        "name": "Charan",
        "department": "IT",
        "department_id": 1,
        "salary": 65000
    },
    {
        "name": "Deepa",
        "department": "Sales",
        "department_id": 3,
        "salary": 50000
    },
    {
        "name": "Ezhil",
        "department": "HR",
        "department_id": 2,
        "salary": 55000
    }
])

print("Remaining 4 employees inserted successfully!")
print("Total employees:", employees.count_documents({}))

# Find employees in IT department
print("\nEmployees in IT department:")

for employee in employees.find({"department": "IT"}):
    print(employee)

# Update Arun's salary
update_result = employees.update_one(
    {"name": "Arun"},
    {"$set": {"salary": 65000}}
)

print("\nMatched documents:", update_result.matched_count)
print("Modified documents:", update_result.modified_count)

# Display updated employee
updated_employee = employees.find_one({"name": "Arun"})
print("Updated employee:", updated_employee)

# Aggregation: Average salary per department
print("\nAverage salary per department:")

pipeline = [
    {
        "$match": {
            "salary": {"$gt": 0}
        }
    },
    {
        "$group": {
            "_id": "$department",
            "average_salary": {"$avg": "$salary"}
        }
    }
]

results = employees.aggregate(pipeline)

for result in results:
    print(result)

# Insert department documents
departments.insert_many([
    {"_id": 1, "department_name": "IT"},
    {"_id": 2, "department_name": "HR"},
    {"_id": 3, "department_name": "Sales"}
])

print("\nDepartments inserted successfully!")

# Join employees with departments using $lookup
print("\nEmployees with department details:")

lookup_pipeline = [
    {
        "$lookup": {
            "from": "departments",
            "localField": "department_id",
            "foreignField": "_id",
            "as": "department_info"
        }
    }
]

results = employees.aggregate(lookup_pipeline)

for result in results:
    print(result)

# Close connection
client.close()
print("\nMongoDB connection closed!")
