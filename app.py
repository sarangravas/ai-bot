from flask import Flask,render_template,request
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def AI_bot():
    reply=""
    user_msg=""
    if request.method=='POST':
        user_msg=request.form.get("msg")
        model=ChatGoogleGenerativeAI(
        Model="gemini-2.5-flash",
        api_key=os.getnew("GOOGLE_API_KEY")
        )
        reply=model.invoke(user_msg).content
    return render_template("index.html",reply=reply,user_msg=user_msg)


if __name__=="__main__":
   app.run(port=4000)