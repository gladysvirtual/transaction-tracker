# transaction-tracker
Transaction Tracker is a simple mobile and web-based application that allows users to log in, view their transaction history, and submit new transactions. The backend is built using Django, providing RESTful API endpoints to manage transaction data
Features
•	User authentication (basic username and password verification)
•	View a list of transactions
•	Submit new transactions (date, amount, description)
•	Backend API built with Django
Technologies Used
•	Backend: Django (Python)
•	Frontend: Flutter (for mobile application)
•	Database: In-memory storage (for testing)
•	API: Django REST Framework (DRF)
Installation Guide
Prerequisites
•	Python 3.x installed
•	Django installed (pip install django djangorestframework)
•	Flutter installed (for frontend development)
Setup
1.	Clone the repository:
2.	git clone https://github.com/yourusername/transaction-tracker.git
cd transaction-tracker
3.	Install dependencies:
pip install -r requirements.txt
4.	Run database migrations:
python manage.py migrate
5.	Start the Django server:
python manage.py runserver
6.	The API will be available at http://127.0.0.1:8000/
API Endpoints
Authentication
•	POST /login/ – Accepts username and password, returns success/failure.
Transactions
•	GET /transactions/ – Returns a list of transactions.
•	POST /transactions/ – Accepts a JSON object { "date": "YYYY-MM-DD", "amount": 100.0, "description": "Payment" } and stores it.
Usage
1.	Run the backend server.
2.	Use Postman or a web browser to test API endpoints.
3.	Develop and connect the Flutter frontend to interact with the API.

