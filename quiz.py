from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

nlp = pipeline("question-answering", model="dbmdz/bert-base-turkish-128k-uncased", tokenizer="dbmdz/bert-base-turkish-128k-uncased")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

def check_answer(user_answer, correct_answers):
    for correct_answer in correct_answers:
        if user_answer.lower() in correct_answer.lower():
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    score = 0

    mcq_answers = {
        'question1': 'c',
        'question2': 'b',
        'question3': 'd'
    }

    open_ended_answers = {
        'question4': [
            'Basit bir yapay zeka modeli oluşturmak için öncelikle veri toplamanız gerekir. Daha sonra bu verileri kullanarak Scikit-learn gibi bir kütüphaneyle modeli eğitebilirsiniz. Eğittikten sonra modeli test ederek ne kadar iyi çalıştığını kontrol edersiniz.',
            'İlk olarak veri toplamalısınız, sonra Scikit-learn gibi bir kütüphane ile modeli oluşturabilirsiniz. Modeli eğittikten sonra test edin.',
            'Veri toplayarak başlayın, sonra Scikit-learn gibi bir Python kütüphanesi kullanarak modeli eğitin. Son olarak, modelin performansını kontrol etmek için test edin.'
        ],
        'question5': [
            'Python\'da bir yapay zeka modelini resimleri tanımak gibi şeyler için kullanabilirsiniz. Örneğin, bir modeli eğiterek bir fotoğrafta kedi mi köpek mi olduğunu söylemesini sağlayabilirsiniz. Başka bir örnek, bilgisayarın düşündüğünüz bir sayıyı tahmin etmeye çalıştığı basit bir oyun yapmaktır.',
            'Python\'da AI modelleri resimleri tanımak veya oyun yapmak için kullanılabilir. Örneğin, bir modeli eğiterek bir resimde kedi mi köpek mi olduğunu tanımlayabilirsiniz. Bir başka kullanım da AI\'ı basit bir oyun yapmak için kullanmaktır.',
            'Bir AI modelini Python\'da kullanarak resimleri tanıyabilirsiniz, örneğin bir fotoğrafın kedi mi köpek mi olduğunu söylemek için. Ayrıca, AI kullanarak düşündüğünüz bir sayıyı tahmin eden bir oyun yapabilirsiniz.'
        ]
    }

    user_mcq_answers = {
        'question1': request.form.get('question1'),
        'question2': request.form.get('question2'),
        'question3': request.form.get('question3')
    }
    user_open_ended_answers = {
        'question4': request.form.get('question4'),
        'question5': request.form.get('question5')
    }
    for q, a in user_mcq_answers.items():
        if mcq_answers[q] == a:
            score += 20

    if check_answer(user_open_ended_answers['question4'], open_ended_answers['question4']):
        score += 20
    if check_answer(user_open_ended_answers['question5'], open_ended_answers['question5']):
        score += 20


    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    if user:
        user.score = score
    else:
        user = User(username=username, score=score)
        db.session.add(user)
    db.session.commit()

    best_score = User.query.order_by(User.score.desc()).first().score

    return render_template('result.html', score=score, best_score=best_score)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
