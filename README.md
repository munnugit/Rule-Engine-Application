# Rule-Engine-Application

Rule Engine Application
This is a simple 3-tier Rule Engine application that allows for dynamic creation, combination, and modification of rules to determine user eligibility based on attributes like age, department, income, and spend. The application uses an Abstract Syntax Tree (AST) to represent conditional rules.

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
Create dynamic rules using an AST-based structure.
Combine and modify rules efficiently.
Store and manage rules using a PostgreSQL database.
Simple UI to create, combine, and test rules.
RESTful API to interact with rules and evaluate them.
Technologies Used
Frontend: React, Axios
Backend: Python, Flask, PostgreSQL
Database: PostgreSQL
Containerization: Docker, Docker Compose
File Structure
arduino
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
Docker (Optional, if using Docker setup)
Backend Setup
Setup PostgreSQL Database: Create a new database named rule_engine.

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
The server will be running at http://localhost:5000.

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
The application will be available at http://localhost:3000.

Docker Setup
Build and Run Containers:

bash
Copy
docker-compose up --build
Access Application:

Frontend: http://localhost:3000
Backend: http://localhost:5000
Stopping Containers:

bash
Copy code
docker-compose down
Usage
Creating Rules: Use the UI or POST request via API to define new rules using an expression like:

Copy code
(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')
Combining Rules: Combine existing rules dynamically and generate an AST.

Evaluating Rules: Provide sample data (e.g., { "age": 35, "department": "Sales", "salary": 60000 }) and test if the rule applies.
