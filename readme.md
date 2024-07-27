# FastAPI Todo App

Welcome to the FastAPI Todo App project! This hands-on course will guide you through the process of building a
production-ready RESTful API using FastAPI and Python. By the end of this course, you will have gained practical
experience in developing APIs, building a Full Stack application, implementing authentication and authorization, setting
up production-ready databases, and deploying your FastAPI application.
[Here you can find the notes](https://persistent-branch-9d1.notion.site/FastAPI-65c7084836cf4e318b9e7ef9edece5b1) for the [FastAPI - The Complete Course 2024 (Beginner + Advanced)](https://www.udemy.com/course/fastapi-the-complete-course/).

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/) (recommended version)
- [PyCharm](https://www.jetbrains.com/pycharm/download/) (or your preferred IDE)
- Basic understanding of Python

## Getting Started

1. **Clone this repository to your local machine.**
   ```bash
   git clone https://github.com/your-username/fastapi-todo-app.git
   ```

2. **Navigate to the project directory.**
   ```bash
   cd fastapi-todo-app
   ```

3. **Set up a virtual environment for your FastAPI project.**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment.**
    - For Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. **Install project dependencies.**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- `app`: Contains the FastAPI application and related modules.
- `database`: Handles database configurations and models.
- `templates`: Holds HTML templates for the Full Stack application.

## Features Covered

- Install & Setup Python, IDE & FastAPI
- Overview of FastAPI Projects
- Installation of a virtual environment for your FastAPI project
- HTTP Request Methods (GET, POST, PUT, DELETE)
- Data Validation
- HTTP Response Status Codes
- Dynamic data and models
- Saving dynamic data to Database
- Handling user input & forms
- Advanced features like Registration, Authentication (bcrypt) & Authorization (JWT)
- Database relationships (CASCADE, etc)
- Setup production database (MySQL)
- Routing

## How to Run

1. **Run the FastAPI development server.**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the FastAPI Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to interact
   with the API.**
