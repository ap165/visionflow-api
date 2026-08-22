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
    try:
        # 1. Get the audio file from the request
        if "audioFile" not in request.files:
            return jsonify({"error": "No audio file provided"}), 400
            
        audio_file = request.files["audioFile"]
        
        # Read the raw bytes into memory and get the mime type (e.g., 'audio/webm')
        audio_bytes = audio_file.read()
        mime_type = audio_file.content_type 

        
        context_memory = request.form.get("history", "")
        snapshot = request.form.get("snapshot",  "")

        instructions = "Please listen to the attached audio and act on it."
        formatted_prompt = browser_planner.replace(
            "{{USER_MESSAGE}}", instructions
        ).replace(
            "{{HISTORY}}", context_memory
        ).replace("{{PAGE_SNAPSHOT}}", snapshot)
        
        # 4. Pass the prompt AND the audio bytes directly to your chat function
        res = chat(
            prompt=formatted_prompt, 
            audio_bytes=audio_bytes, 
            mime_type=mime_type
        )
        
        return json.loads(res)

    except Exception as e:
        print(f"Error in classify: {e}")
        return jsonify({"error": str(e)}), 500