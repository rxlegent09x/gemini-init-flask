from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from ai_init import get_ai_response

app = Flask(__name__)
CORS(app)
@app.route('/chat', methods=['POST',"GET"])
def chat():
    user_input = request.data.decode('utf-8')
    print(f"User Input: {user_input}")
    return (get_ai_response(user_input))

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)



# #  x = request.data
#     y = json.loads(x.decode('utf-8'))
#     print(y)
#     return jsonify({
#         'message': 'Hello, World!',
#     })