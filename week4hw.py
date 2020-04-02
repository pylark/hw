from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('week4hw.html')

## API 역할을 하는 부분
@app.route('/shoppost', methods=['POST'])
def write_shop():
	# 1. 클라이언트가 준 title, author, review 가져오기.
    print(request.form)
    order_name = request.form['order_name']
    option_select = request.form['option_select']
    order_address = request.form['order_address']
    order_phone = request.form['order_phone']
	# 2. DB에 정보 삽입하기
    doc = {
        'order_name': order_name,
        'option_select': option_select,
        'order_address': order_address,
        'order_phone' : order_phone
    }
    db.shoppost.insert_one(doc)
    #db.변수명.insert_one(doc)
	# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 완료되었습니다.'})

@app.route('/shopget', methods=['GET'])
def read_shop():
    send_data = []
    shop_order = list(db.shoppost.find())
    for order in shop_order:
        send_data.append({
            'order_name' : order['order_name'],
            'order_color' : order['order_color'],
            'order_address' : order['order_address'],
            'order_phone' : order['order_phone']
        })
    return jsonify({'result': 'success', 'data': send_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)