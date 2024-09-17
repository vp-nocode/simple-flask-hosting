from app import app, db
from app.models import User

with app.app_context():  # After the first launch, this line can be deleted.
    db.create_all()  # After the first launch, this line can be deleted.

if __name__ == '__main__':
    app.run(debug=True)
