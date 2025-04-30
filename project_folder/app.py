from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime
import os  # تمت إضافة مكتبة os لحل الأخطاء

app = Flask(__name__, template_folder='templates')

# إعدادات قاعدة البيانات
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "registrat",
    "charset": "utf8mb4" 
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.after_request
def add_ngrok_headers(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if not request.form:
        return jsonify({"error": "لم يتم إرسال بيانات!"}), 400
    
    try:
        name = request.form['name']
        committee = request.form['committee']
        session_attended = request.form['session_attended']
    except KeyError as e:
        return jsonify({"error": f"الحقل {e} مطلوب!"}), 400

    entry_time = datetime.now()
    
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO user_entries (name, committee, sessions_attended, entry_time) VALUES (%s, %s, %s, %s)",
            (name, committee, session_attended, entry_time)
        )
        db.commit()
    except mysql.connector.Error as err:
        return jsonify({"error": f"خطأ في قاعدة البيانات: {err}"}), 500
    finally:
        cursor.close()
        db.close()

    return jsonify({"message": "تم حفظ البيانات بنجاح 🎉"}), 201
@app.route('/amr-hassan')  # <-- أضف هذا المسار هنا
def motivation():
    return render_template('amr-hassan.html')

@app.route('/test')
def test_files():
    template_path = os.path.join(app.root_path, 'templates')
    files = os.listdir(template_path)
    return jsonify({"template_files": files})

if __name__ == '__main__':
    print("مسار القوالب:", os.path.join(app.root_path, 'templates'))
    app.run(host="0.0.0.0", port=5000, debug=True)