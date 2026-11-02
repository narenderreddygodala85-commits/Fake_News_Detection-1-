import sys
sys.path.insert(0, r'.')
from app import app
print('App starting on http://127.0.0.1:5000')
app.run(host='127.0.0.1', port=5000, debug=False)