from flask import Blueprint, request, jsonify
from services import chat
from prompts import classification_prompt, browser_action_prompt, summarizer_prompt, conversation_action_prompt
import json

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/agent", methods=["GET", "POST"])
def agent():
    queery = request.args.get("q")

    reply = chat(queery)

    return reply


# Classifies the user intent
@api_bp.route("/classify", methods=["POST"])
def classify():
    prompt = request.get_json().get("q")
    # prompt = request.args.get("q")
    res = chat(classification_prompt.replace("{{USER_MESSAGE}}", prompt), max_tokens=50)
    try:
        return json.loads(res)
    except Exception as e:
        print(e)
        return (res)


# AI response
@api_bp.route("/ai-response", methods=["POST"])
def aiResponse():
    data = request.get_json()
    intent = data.get("intent")
    message = data.get("message")
    snapshot = str(data.get("snapshot"))

    if intent == "browser_action":
        res = chat((browser_action_prompt.replace("{{USER_MESSAGE}}", message)).replace("{{PAGE_SNAPSHOT}}", snapshot))
    elif intent == "page_question":
        res = chat((summarizer_prompt.replace("{{USER_MESSAGE}}", message)).replace("{{PAGE_SNAPSHOT}}", snapshot))
    elif intent == "conversation":
        res = chat(conversation_action_prompt.replace("{{USER_MESSAGE}}", message))

    try:
        return json.loads(res)
    except Exception as e:
        return (e)