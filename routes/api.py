from flask import Blueprint, request, jsonify
from services import chat

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/agent", methods=["GET", "POST"])
def agent():
    queery = request.args.get("q")

    reply = chat(queery)

    return reply
