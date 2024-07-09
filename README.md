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

![quiz2](https://github.com/MuKimLong/quiz_website/assets/108682681/6bc2c4ac-7e32-4521-b0d8-ed90e3620d39)
![quiz2bucuk](https://github.com/MuKimLong/quiz_website/assets/108682681/f508cf8c-cd3a-4efd-9661-93196868a701)
![quiz3](https://github.com/MuKimLong/quiz_website/assets/108682681/30c87fcc-64b1-4b29-a8c6-001b20f938c2)
![quiz4](https://github.com/MuKimLong/quiz_website/assets/108682681/99173f30-1410-4424-b30d-52b21cdc7ff6)




