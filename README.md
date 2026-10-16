# School Management System API

## Project Overview
This project is a RESTful API for a School Management System, developed for the StarUnion Backend Workshop final project. It provides endpoints to manage students, teachers, subjects, and grades.

## Main Features
* Role-based access control (Admin, Teacher, Student).
* JWT Authentication for all protected endpoints.
* CRUD operations for Classes, Subjects, and Attendance.
* Automated grading workflow and scheduling conflict validation.
* Data filtering and search capabilities.

## Technologies Used
* Python
* Django & Django REST Framework (DRF)
* SQLite (Development) / PostgreSQL (Production)
* JWT (JSON Web Tokens)

## Environment Variables
To run this project, you need a `.env` file. A `.env.example` is provided in the repository. Required variables include:
* `SECRET_KEY`
* `DEBUG`
* Database credentials (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`)

## Installation & How to Run Locally
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Backend-Committee/Backend-Workshop-Final-Projects.git](https://github.com/Backend-Committee/Backend-Workshop-Final-Projects.git)
   cd Backend-Workshop-Final-Projects
   git checkout mostafa-ahmed
## Documentation & Database Design
* **API Documentation (Apidog):** [https://9f6rschtrn.apidog.io]
## Database Design
* **ERD & Schema (Lucidchart):** [https://lucid.app/lucidchart/3470bd7b-4cc5-47d2-990d-3abcc06f619f/edit?viewport_loc=-1765%2C-200%2C2348%2C1536%2C0_0&invitationId=inv_c67629ab-8a76-46d4-8f45-8ba4a9195640]
