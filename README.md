# DoseAlert

DoseAlert is a cloud-based medication reminder service that helps users keep track of their medication and receive email reminders at their scheduled times.

The project was built to explore how different AWS services can work together with a Python Flask application to create a simple cloud-based system.

## How It Works

The user enters their:

* Name
* Medication name
* Email address
* Reminder time

The information is saved in AWS DynamoDB. AWS Lambda checks the stored reminders and uses Amazon SES to send an email reminder when a medication is due.

## Technologies Used

### Application

* Python
* Flask
* HTML
* CSS
* SQLite

### AWS

* Amazon DynamoDB
* AWS Lambda
* Amazon EventBridge Scheduler
* Amazon SES
* IAM

### Deployment

* GitHub
* Render

## Features

* Add a medication reminder
* Store reminder information in DynamoDB
* Automatically check reminders using AWS Lambda
* Send medication reminders through email
* Simple web interface
* Cloud-based reminder processing

## AWS Architecture

**Amazon DynamoDB** stores the medication and reminder information.

**Amazon EventBridge Scheduler** triggers the Lambda function automatically.

**AWS Lambda** checks DynamoDB for reminders that are due.

**Amazon SES** sends the reminder email to the user.

**IAM** controls access between the AWS services.

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/nadia16-tan/DoseAlert.git
```

Move into the project folder:

```bash
cd DoseAlert
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

The application will then be available at:

```text
http://localhost:5000
```

## Project Purpose

This project was created as part of my Cloud Computing learning journey. The main goal was to gain practical experience working with AWS services and understanding how different cloud services can work together to create a working application.

## Future Improvements

Some improvements I would like to make include:

* Allowing users to create multiple reminders
* Adding a way to edit or delete reminders
* Improving reminder scheduling
* Adding better error handling
* Adding authentication
* Improving the user interface
* Adding a dashboard to view active reminders

## WeThinkCode_ Verification

**WTC-WPKL6ZTN**

## Author

**Nadia Tanaka Nyamanyunzo**

Cloud Computing student project — 2026
