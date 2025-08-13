from flask import Flask, request, render_template # type: ignore
from langchain_ollama.llms import OllamaLLM # type: ignore
from langchain_core.prompts import ChatPromptTemplate # type: ignore


def sum_model(text):
    template = """Question: {input_text}
    Summerize the text into 50 words"""
    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model="gemma3:1b")
    chain = prompt | model
    input_user  = {"input_text": text}
    output = chain.invoke(input_user )
    return output



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("human_input")

        # You can process the input here (e.g., send to AI model)
        response = sum_model(user_input)
        # response = f"You said: {user_input}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)



