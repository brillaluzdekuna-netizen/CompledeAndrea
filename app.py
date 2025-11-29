import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '1ACC0184_TB2_U202310988_Santur_Andrea_Actualizado'))
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
