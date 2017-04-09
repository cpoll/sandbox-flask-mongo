#!/usr/bin/env python3
from server import APP

if __name__ == "__main__":
    APP.run(debug=True, use_debugger=False, use_reloader=False)
