from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

likes = 0
#hello
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/api/like', methods=['POST'])
def stuff():
  global likes
  #newlike = request.get_json()
  print(f'total likes (POST): {likes}')
  likes += 1
  return 'Success', 200

@app.route('/api/get/errything', methods=["GET"])
def stuff2():
  print(f'total likes (GET): {likes}')
  return jsonify(likes)
