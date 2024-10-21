# smart-elearning-framework

# Rule Engine Application

This is a simple 3-tier Rule Engine application that allows for dynamic creation, combination, and modification of rules to determine user eligibility based on attributes like age, department, income, and spend. The application uses an Abstract Syntax Tree (AST) to represent conditional rules.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create dynamic rules using an AST-based structure.
- Combine and modify rules efficiently.
- Store and manage rules using a PostgreSQL database.
- Simple UI to create, combine, and test rules.
- RESTful API to interact with rules and evaluate them.

## Technologies Used
- Frontend: React, Axios
- Backend: Python, Flask, PostgreSQL
- Database: PostgreSQL
- Containerization: Docker, Docker Compose

## File Structure

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


## Getting Started
 rerequisites
- Node.js (v16+)
- Python (v3.8+)
- PostgreSQL (v12+)
- Docker (Optional, if using Docker setup)

### Backend Setup
1. Setup PostgreSQL Database:
   Create a new database named `rule_engine`.
   bash
   psql -U your_username -c "CREATE DATABASE rule_engine;"
   

2. Install Dependencies:
   bash
   cd backend
   pip install -r requirements.txt
 

3. Run the Backend Server:
  bash
   python app.py
  
   The server will be running at `http://localhost:5000`.

### Frontend Setup
1. Install Dependencies:
bash
   cd frontend
   npm install


2. Run the Frontend Server:
   bash
   npm start
  
   The application will be available at `http://localhost:3000`.

### Docker Setup
1. Build and Run Containers:
   bash
   docker-compose up --build


2. Access Application:
   - Frontend: `http://localhost:3000`
   - Backend: `http://localhost:5000`

3. Stopping Containers:
  bash
   docker-compose down
  

## Usage
1. Creating Rules:
   Use the UI or POST request via API to define new rules using an expression like:
  
   (age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')
   

2. Combining Rules:
   Combine existing rules dynamically and generate an AST.

3. Evaluating Rules:
   Provide sample data (e.g., `{ "age": 35, "department": "Sales", "salary": 60000 }`) and test if the rule applies.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

