from flask import Flask, request, jsonify
import google.generativeai as genai
app = Flask(__name__)
genai.configure(api_key="AIzaSyC6RQEvU80oVH5c6Ug3Nn-kTPQVEgf7RIw")
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    user_query = data.get('user_query', '')
    if not user_query:
        return jsonify({'error': 'User query is required'}), 400
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_query)
        llm_response = response.text.strip() if response.text else "No response from the model"
    except Exception as e:
        llm_response = f"An error occurred: {str(e)}"
    return jsonify({'llm_response': llm_response})
if __name__ == '__main__':
    app.run(debug=True)