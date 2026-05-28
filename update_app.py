import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add import if not exists
if 'from database_config import get_database_connection' not in content:
    content = content.replace('import sqlite3\n', 'import sqlite3\nfrom database_config import get_database_connection\n', 1)

# Replace sqlite3.connect calls
content = content.replace("sqlite3.connect('vizag_bazaar.db')", "get_database_connection()")
content = content.replace("sqlite3.connect(DATABASE)", "get_database_connection()")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated app.py')
