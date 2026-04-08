# User Auth API 🛡️

## Project Idea 💡

**User Auth API** is a Django REST API project for **user registration, login, and role-based access control**.  
It is designed for applications that require secure authentication and user management.

---

## Features ✨

- User Registration (Sign Up) 🔑
- User Login 🔐
- Role-based Access Control (Admin vs User) 👥
- Input Validation ✅
- Consistent JSON Error Responses ⚠️

---

## Tech Stack 🛠️

- **Django REST Framework** – To build API endpoints and handle requests/responses.
- **MySQL** – Relational database to store user data such as names, emails, and passwords.
- **mysql-connector-python** – For direct SQL queries if needed.
- **.env file** – To securely store sensitive information such as database credentials and secret keys.
- **Serializers** – Convert Django models to JSON and vice versa for API communication.

---

Installation ⚙️
Clone the repository:
git clone https://github.com/YOUR_USERNAME/user_auth_api.git
cd user_auth_api
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
Install dependencies:
pip install -r requirements.txt
Set up environment variables in .env:
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=user_auth_db
DB_USER=root
DB_PASSWORD=password
Run migrations:
python manage.py migrate
Run the server:
python manage.py runserver
