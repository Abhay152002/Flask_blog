import os

file_path = "/opt/render/project/src/.venv/lib/python3.11/site-packages/sqlalchemy/sql/base.py"
with open(file_path, 'r') as file:
    content = file.read()

# Replace the import statement
content = content.replace("from collections import MutableMapping",
                          "from collections.abc import MutableMapping")

with open(file_path, 'w') as file:
    file.write(content)
