from flask import jsonify

from app import app


@app.errorhandler(404)
def handler_404(err):
    error = {"name": err.name, "message": err.description}
    return jsonify({"success": False, "error": error}), 404


@app.errorhandler(403)
def handler_403(err):
    error = {"name": err.name, "message": err.description}
    return jsonify({"success": False, "error": error}), 403
