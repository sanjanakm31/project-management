
Project Management App — React + Django + PostgreSQL
===================================================

Contents
--------
- backend/    -> Django REST API (pm_backend)
- frontend/   -> React app (created with Vite)
- README contains instructions to run locally.

High-level features implemented
- JWT authentication (djangorestframework-simplejwt)
- Admin & Employee roles (Django is_staff marks Admin)
- Project model: fields per assignment (employee, project_name, customer, priority, quantity, subtask, remarks, due_date, completion, delay, delay_remarks)
- Delay calculation is automatic on the backend.
- Excel/CSV export endpoint.
- React frontend with login, employee dashboard (update tasks), and admin dashboard (view all tasks in table, filter, export CSV).

Important notes
- This package is a functional skeleton to submit as your assignment. For production, extra hardening, validation, and UI polish are recommended.
- Database: PostgreSQL is recommended. Settings in backend/README show how to configure. If you don't have PostgreSQL, the backend defaults to SQLite for quick testing.

Quick start (Linux / WSL / macOS)
--------------------------------
1. Backend
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   # Configure PostgreSQL in pm_backend/settings.py or set DATABASE_URL env var
   python manage.py migrate
   python manage.py createsuperuser  # create admin (is_staff)
   python manage.py loaddata sample_data.json
   python manage.py runserver

2. Frontend
   cd frontend
   npm install
   npm run dev
   # By default frontend expects backend at http://localhost:8000

Deliverable
----------
A zip file containing the full project is included with this message. Unzip and follow README instructions.

Credentials for demo (after you run createsuperuser, you can also use this sample employee created by fixture):
- admin: admin@example.com / adminpass123 (if created via fixture)
- employee: employee1@example.com / employeepass

Good luck! If anything breaks when you test locally, tell me what error you see and I'll fix it quickly.
