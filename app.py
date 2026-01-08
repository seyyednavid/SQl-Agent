from flask import Flask, render_template, request
from agent.sql_agent_01 import agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            result = agent.invoke({"messages": [{"role": "user", "content": question}]})
            answer = result["messages"][-1].content
    return render_template("index.html", answer=answer)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)