Smart E-Learning Framework
Rule Engine Application
This repository contains a 3-tier Rule Engine application that enables dynamic creation, combination, and modification of rules to determine user eligibility based on attributes like age, department, income, and spend. An Abstract Syntax Tree (AST) is utilized to represent conditional rules, allowing for flexible and complex rule evaluations.

Table of Contents
Features
Technologies Used
File Structure
Getting Started
Prerequisites
Backend Setup
Frontend Setup
Docker Setup
Usage
Contributing
License
Features
Dynamic Rule Creation: Use an AST-based structure to create rules based on attributes.
Flexible Rule Management: Modify, combine, and manage rules efficiently.
Persistent Storage: Store rules in a PostgreSQL database.
Intuitive UI: User-friendly interface for rule creation, modification, and testing.
REST API: Easily integrate rule evaluation with external applications.
Technologies Used
Frontend: React, Axios
Backend: Python, Flask
Database: PostgreSQL
Containerization: Docker, Docker Compose
File Structure
plaintext
Copy code
.
├── backend
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── ast_utils.py
│   ├── requirements.txt
│   └── config.py
├── frontend
│   ├── public
│   ├── src
│   │   ├── components
│   │   │   ├── RuleForm.js
│   │   │   ├── RuleList.js
│   │   │   └── RuleEvaluator.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── index.css
│   ├── package.json
│   └── .env
├── docker-compose.yml
└── README.md
Getting Started
Prerequisites
Node.js (v16+)
Python (v3.8+)
PostgreSQL (v12+)
Docker (Optional, for containerized setup)
Backend Setup
Setup PostgreSQL Database:

bash
Copy code
psql -U your_username -c "CREATE DATABASE rule_engine;"
Install Dependencies:

bash
Copy code
cd backend
pip install -r requirements.txt
Run the Backend Server:

bash
Copy code
python app.py
The backend server will be running at http://localhost:5000.

Frontend Setup
Install Dependencies:

bash
Copy code
cd frontend
npm install
Run the Frontend Server:

bash
Copy code
npm start
The frontend will be available at http://localhost:3000.

Docker Setup
Build and Run Containers:

bash
Copy code
docker-compose up --build
Access the Application:

Frontend: http://localhost:3000
Backend: http://localhost:5000
Stopping Containers:

bash
Copy code
docker-compose down
Usage
Creating Rules:
Use the UI or API (POST request) to define new rules in the following format:

java
Copy code
(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')
Combining Rules:
Dynamically combine and evaluate rules, generating an AST for visualization and logical processing.

Evaluating Rules:
Test rules with sample data (e.g., { "age": 35, "department": "Sales", "salary": 60000 }) to verify if conditions are met.

