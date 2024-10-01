from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up the Google Generative AI API Key
genai.configure(api_key="AIzaSyA7KBSVOz1xTKq8-4oLczseKZ5ORVS0c88")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Model configuration for generation
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)


class StudentResponse(BaseModel):
    response: str
    algorithm: str
    history: List[str] = []  # Stores the conversation history


@app.post("/ai-response")
async def ai_response(student_response: StudentResponse):
    """Call Google Generative AI (Gemini) to generate a dynamic Socratic follow-up question one at a time."""
    try:
        # Prepare the chat history (previous questions and responses)
        history = student_response.history

        # Create a chat session with the previous conversation history
        chat_session = model.start_chat(
            history=history
        )

        # Refine the prompt to request only one Socratic question
        prompt = (
            f"The student said: '{student_response.response}' about {student_response.algorithm}. "
            f"Please provide only one Socratic follow-up question based on this."
        )

        # Send the prompt to the model and get the next question
        response = chat_session.send_message(prompt)

        # Add the current response to the history
        history.append(f"Student: {student_response.response}")
        history.append(f"Assistant: {response.text}")

        # Return the current follow-up question and updated conversation history
        return {
            "ai_response": response.text,
            "updated_history": history
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import google.generativeai as genai
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Set up the Google Generative AI API Key
# genai.configure(api_key="AIzaSyA7KBSVOz1xTKq8-4oLczseKZ5ORVS0c88")

# # CORS settings - allow the React frontend origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # React frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Model configuration for generation
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config
# )

# class StudentResponse(BaseModel):
#     response: str
#     algorithm: str
#     history: List[str] = []  # Stores the conversation history

# @app.post("/ai-response")
# async def ai_response(student_response: StudentResponse):
#     """Call Google Generative AI (Gemini) to generate a dynamic Socratic follow-up question one at a time."""
#     try:
#         # Prepare the chat history (previous questions and responses)
#         history = student_response.history

#         # Create a chat session with the previous conversation history
#         chat_session = model.start_chat(
#             history=history
#         )

#         # Refine the prompt to request only one Socratic question
#         prompt = (
#             f"The student said: '{student_response.response}' about {student_response.algorithm}. "
#             f"Please provide only one Socratic follow-up question based on this."
#         )

#         # Send the prompt to the model and get the next question
#         response = chat_session.send_message(prompt)

#         # Add the current response to the history
#         history.append(f"Student: {student_response.response}")
#         history.append(f"Assistant: {response.text}")

#         # Return the current follow-up question and updated conversation history
#         return {
#             "ai_response": response.text,
#             "updated_history": history
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
