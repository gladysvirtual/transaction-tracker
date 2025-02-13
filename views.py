from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import monitoring_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>Transaction Tracker</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                    display: inline-block;
                }
                h1 {
                    color: #333;
                }
                p {
                    font-size: 18px;
                    color: #666;
                }
                .button {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 16px;
                }
                .button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Transaction Tracker</h1>
                <p>Manage and track transactions with ease.</p>
                <a href="/monitoring/transactions/" class="button">View Transactions</a>
                <a href="/monitoring/login/" class="button">Login</a>
            </div>
        </body>
        </html>
    """)


# Dummy data storage
transactions = []

# Login endpoint
@monitoring_view(['POST'])
def login(request):
    data = request.data 
    username = data.get("username")
    password = data.get("password")

    if username == "test" and password == "password":  # Placeholder authentication
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
# Transactions endpoints
@monitoring_view(['GET', 'POST'])
def transactions_monitoring(request):
    global transactions
    if request.method == 'GET':
        return Response(transaction)
    
    if request.method == 'POST':
        transaction = {
            "date": request.data.get("date"),
            "amount": request.data.get("amount"),
            "description": request.data.get("description")
        }
        transaction.append(transaction)
        return Response(transaction, status=status.HTTP_201_CREATED)
    
    #transaction list function
transactions = [
    {"date": "2025-02-13", "amount": 100.50, "description": "Grocery Shopping"},
    {"date": "2025-02-12", "amount": 50.75, "description": "Restaurant"},
    {"date": "2025-02-11", "amount": 20.00, "description": "Bus Fare"},
    {"date": "2025-02-07", "amount": 50.75, "description": "Restaurant"},
    {"date": "2024-12-31", "amount": 20.00, "description": "Bus Fare"},
    {"date": "2024-12-25", "amount": 50.75, "description": "Restaurant"},
    {"date": "2024-12-22", "amount": 20.00, "description": "Bus Fare"},
]

def transaction_list(request):
    return render(request, "transactions.html", {"transactions": transactions})
