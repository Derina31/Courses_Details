"""Routes for the course resource.
"""

from run import app
from flask import request
from http import HTTPStatus



@app.route("/course/<int:id>", methods=['GET'])
def id():
    return 'id'

if __name__ :
    app.run()
    ("Get a course by id.\n"
     "\n"
     "    :param int id: The record id.\n"
     "    :return: A single course (see the challenge notes for examples)\n"
     "    :rtype: object\n"
     "    ")

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['GET'])
def get_courses():
    return 'course'

@app.route("/course", methods=['GET'])
def get_course():
    return "page-number" % get_courses

@app.route("/course", methods=['GET'])
def get_course():
    return "page-size" % get_courses

@app.route("/course", methods=['GET'])
def get_course():
    return "title-words" % get_courses




if __name__ == "__main__":
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE


@app.route("/course", methods=['POST'])
def create_course():
    return create_course('id', 'course_name')

    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    return 'courses'
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE


class Flask(object):
    pass