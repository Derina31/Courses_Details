"""Routes for the course resource.""
-------------------------------------------------------------------------
Challenge general notes:
-------------------------------------------------------------------------

1. Bonus points for returning sensible HTTP codes from the API routes
2. Bonus points for efficient code (e.g. title search)
"""

from flask import Flask


app = Flask(__name__)

# Import the API routes
@app.route('/')
def The_Art_of_Scala():
    return 'The Art of Scala!'

if __name__ == '__main__':
    app.run()


# Required because app is imported in other modules    app.run(debug=True)
