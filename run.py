#!/usr/bin/env python3
"""Navigator - Run script"""

import sys
sys.path.insert(0, 'src')

from app import create_app

app = create_app()

if __name__ == '__main__':
    print("\n=== Navigator Starting ===")
    print("http://localhost:5000")
    print("Ctrl+C to stop\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
