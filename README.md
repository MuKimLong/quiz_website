## Quiz Web Application
### Overview

This project is a web-based quiz application designed to test users' knowledge in artificial intelligence (AI) using Python. The application allows users to answer multiple-choice and open-ended questions, calculates their scores, and displays the results.

### Features

Multiple-choice questions and open-ended questions
Score calculation based on user answers
Displays the highest score and user's score on the result page
Developed using Flask, a lightweight web framework for Python
Uses SQLAlchemy for database interactions
Includes a pre-trained BERT model for natural language processing (NLP) to evaluate open-ended answers

## Technologies Used

Flask
SQLAlchemy
Hugging Face Transformers (BERT model)
HTML/CSS for front-end

## Project Structure

quiz-app/
│
├── app.py (Main application file)
├── quiz.db (SQLite database)
├── templates/
│   ├── index.html (Main quiz page)
│   └── result.html (Result page)
└── README.md (Project documentation)

## Installation and Setup

Clone the repository:
git clone https://github.com/your-username/quiz-app.git
cd quiz-app

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Open your web browser and navigate to:
http://127.0.0.1:5000

## Usage

On the main page (index.html), users can enter their username and answer the quiz questions.
After submitting the answers, users are redirected to the result page (result.html) where they can see their score and the highest score achieved.
