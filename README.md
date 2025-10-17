
Project Management App 
===================================================

Project Overview
--------
The Web-Based Project Management System is a complete solution to manage organizational
projects online. It replaces manual Excel sheets by allowing admins and employees to collaborate
in real time, track deadlines, update task progress, and record delay remarks through a web
interface.

Objectives
--------
- Provide a simple yet powerful online dashboard for tracking projects.
- Allow Admins to manage and assign projects.
- Allow Employees to update project completion and delay remarks.
- Replace manual Excel updates with real-time data synchronization.
- Enable export of project data in CSV format for reporting.

Technology Stack
--------
Frontend: React.js (Vite) with Axios for HTTP requests.
Backend: Django REST Framework for API and authentication.
Database: SQLite (lightweight and built-in for development).
Authentication: JSON Web Token (JWT) for secure login.
Libraries Used: reportlab, dj-database-url, corsheaders, djangorestframework-simplejwt.


High-level features implemented
--------
- JWT authentication (djangorestframework-simplejwt)
- Admin & Employee roles (Django is_staff marks Admin)
- Project model: fields per assignment (employee, project_name, customer, priority, quantity, subtask, remarks, due_date, completion, delay, delay_remarks)
- Delay calculation is automatic on the backend.
- Excel/CSV export endpoint.
- React frontend with login, employee dashboard (update tasks), and admin dashboard (view all tasks in table, filter, export CSV).

Quick start (Linux / WSL / macOS)
--------------------------------
1. Backend
   cd backend
   Create virtual environment: python3 -m venv venv
   Activate it: .\venv\Scripts\Activate.ps1
   Install packages: pip install -r requirements.txt
   Make migrations: python manage.py makemigrations projects
   # Configure PostgreSQL in pm_backend/settings.py or set DATABASE_URL env var
   Migrate database: python manage.py migrate
   Create superuser: python manage.py createsuperuser  # create admin (is_staff)
   python manage.py loaddata sample_data.json
   Run backend server: python manage.py runserver

2. Frontend
   cd frontend
   Install dependencies: npm install
   Start frontend: npm run dev
   # By default frontend expects backend at http://localhost:8000

THANKYOU!
Contact - sanjanakm31
