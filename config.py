import os

db_host = os.environ.get('DB_HOST', default='10.0.1.185')
db_name = os.environ.get('DB_NAME', default='dashboard')
db_port = os.environ.get('DB_PORT', default='5432')
db_user = os.environ.get('DB_USER', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')

SQLALCHEMY_DATABASE_URI = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
