<h1> Not yet </h1># Multi-Tenant Database Stock Management System

This system is a Flask-based web application for managing stocks across multiple tenants. It uses a combination of MongoDB for user management and individual databases for each user's stock-related operations.

## Features

- Multi-tenant architecture
- User authentication and management
- Inventory tracking
- Sales management
- Outgoing stock management
- Other stock-related operations

## System Requirements

- Python 3.11
- Redis
- MySQL
- MongoDB
- Other Python packages (see `requirement-conf.python`)

## Directory Structure

[Directory structure remains the same as before]

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd alx-webstack-portfolio
   ```

2. Install the required Python packages:
   ```
   pip install -r requirement-conf.python
   ```

3. Ensure Redis, MySQL, and MongoDB are installed and running on your system.

## Environment Variables

Before running the application, you need to set up the following environment variables. For security reasons, do not hardcode these values in your application files.

### Main App Variables
```
VAR_SECRET_KEY
VAR_MONGO_DB
VAR_CURRENT_DB
VAR_LOCAL_API_URL
```

### API Variables
```
API_SECRET_KEY
API_BLUEPRINTS_URL
API_ACTIVATION_URL
API_SENDER_EMAIL
API_SENDER_PASSWORD
API_DB_PASSWORD
API_DB_USER
```

You can set these variables using the `export` command in your terminal or by adding them to your `.env` file. For example:

```bash
export VAR_SECRET_KEY='your_secret_key_here'
export VAR_MONGO_DB='your_mongo_db_name'
# ... and so on for all variables
```

Remember to keep these values secret and never commit them to version control.

## Running the Application

1. Ensure all environment variables are set.

2. Start the Flask API:
   ```
   python app.py
   ```

3. Start the main rendering application:
   ```
   python app1.py
   ```

## API Documentation

The API is located in the `api/` directory. For detailed API documentation, please refer to the API documentation file (not provided in the current structure).

## Frontend

The frontend is built using HTML templates located in the `templates/` directory. Static files (CSS, JavaScript, images) are stored in the `static/` directory.

## Database Models

Database models are defined in the `models/` directory. The system uses a combination of MongoDB (for user management) and individual databases for each user's stock-related operations.

## Services

Gunicorn service files for the API and main application are located in the `Services/` directory.

## Logging

Logs are stored in the `logs/` directory, separated into API logs, application logs, and Nginx logs.


## Support

For support, please contact: ashimwegeoffrey@gmail.com
