import os 
from flask import Flask, request, abort, jsonify

from models import setup_db,Question

def create_app(test_config = None ):
    app = Flask(__name__)
    setup_db(app)

    @app.route("/questions", methods=["POST"])
    def post_questions():
        add = request.get_json()

        new_answer = add.get("answer")
        new_difficulty = add.get("difficulty")
        new_category = add.get("category")
        new_question = add.get("question")


        try:
            questions = Question(answer=new_answer, 
                                 question=new_question,
                                 category = new_category,
                                 difficulty = new_difficulty   
                                )
            questions.insert()

            print(questions)

            return jsonify({
                "success": "True",
                "questions_post":questions.format()
            })

        except:
            abort(405)

    @app.route("/")
    def index():
        return "hello woke"

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )

    return app