from flask import Blueprint, request, jsonify
from services import chat
from prompts import browser_planner
import json

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/agent", methods=["GET", "POST"])
def agent():
    queery = request.args.get("q")
    reply = chat(queery)

    return reply

# Classifies the user intent
@api_bp.route("/planner", methods=["POST"])
def classify():
    req_body = json.loads(request.get_json())

    intent = req_body.get("intent")
    instruction = req_body.get("instruction")
    context_memory = req_body.get("history")
    snapshot = str(req_body.get("snapshot"))

    formatted_prompt = browser_planner.replace("{{INTENT}}", intent).replace("{{INSTRUCTION}}", instruction).replace("{{HISTORY}}", context_memory).replace("{{PAGE_SNAPSHOT}}", snapshot)
    
    res = chat(formatted_prompt)
    try:
        return json.loads(res)
    except Exception as e:
        print(e)
        return (res)

# # AI response
# @api_bp.route("/visual-planner", methods=["POST"])
# def aiResponse():
#     req_body = json.loads(request.get_json())

    # intent = req_body.get("intent")
    # instruction = req_body.get("instruction")
    # context_memory = req_body.get("history")
    # snapshot = str(req_body.get("snapshot"))

#     formatted_prompt = visual_analyzer.replace("{{INTENT}}", intent).replace("{{INSTRUCTION}}", instruction).replace("{{HISTORY}}", context_memory).replace("{{PAGE_SNAPSHOT}}", snapshot)

#     res = chat(formatted_prompt)

#     try:
#         return json.loads(res)
#     except Exception as e:
#         return (e)