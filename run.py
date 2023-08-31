from app import app
from flask_cors import CORS

if __name__ == "__main__":
    CORS(app)

    app.run(host="127.0.0.1", port=5001)
