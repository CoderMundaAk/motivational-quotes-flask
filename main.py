from flask import Flask, render_template, request,redirect,url_for
from quote_manager import QuoteManager



app= Flask(__name__)

manager=QuoteManager()
@app.route("/")
def home():
    quotes = manager.get_all_quotes()
    return render_template("index.html", quotes=quotes)
@app.route("/add", methods=["GET","POST"])
def add_quote():
    if request.method == "POST":
       author=request.form["author"]
       quote= request.form["quote"]
       manager.add_quote(author,quote)
       return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_quote(index):
    manager.delete_quote(index)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=10000)
    