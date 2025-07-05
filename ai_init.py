from google import genai

client = genai.Client(api_key="AIzaSyA_6dBki6C_QUXtqOX1Gi2bqcYDxnOasBw")

def get_ai_response(user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    return response.text