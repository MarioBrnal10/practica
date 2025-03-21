from app import app
from contacts import contacts

# Register the Blueprint
app.register_blueprint(contacts)

# Starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
