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
  newlike = request.get_json()
  print(newlike)
  likes = likes + 1
  return 'Success', 200

@app.route('/api/get/errything', methods=["GET"])
def stuff2():
  print(jsonify(likes))
  return jsonify(likes)

if __name__ == "__main__":
  app.run()