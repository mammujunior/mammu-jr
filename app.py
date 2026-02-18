from flask import session
app.secret_key = "mammujr_secret"
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/materials")
def materials():
    return render_template("materials.html")

@app.route("/audit")
def audit():
    return render_template("audit.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
from flask import request, jsonify

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Simple AI response logic (replace with real AI later)
    if "audit" in user_message.lower():
        reply = "This is an audit-related response based on your materials."
    elif "material" in user_message.lower():
        reply = "You can check the materials page for detailed PDFs and guides."
    else:
        reply = "I am here to help you with CA Audit topics! Please ask about your study material."

    return jsonify({"reply": reply})
@app.route("/ai-mentor")
def ai_mentor():
    return render_template("ai.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/audit-foundations")
def audit_foundations():
    return render_template("audit-foundations.html")
@app.route("/sa-200")
def sa_200():
    return render_template("sa-200.html")
@app.route("/sa-210")
def sa_210():
    return render_template("sa-210.html")
@app.route("/sa-200/reasonable-assurance")
def sa200_reasonable_assurance():
    return render_template("sa-200-reasonable-assurance.html")
@app.route("/sa-200/inherent-limitations")
def sa200_inherent_limitations():
    return render_template("sa-200-inherent-limitations.html")
@app.route("/sa-200/objectives")
def sa200_objectives():
    return render_template("sa-200-objectives.html")
@app.route("/sa-200/professional-skepticism")
def sa200_professional_skepticism():
    return render_template("sa-200-professional-skepticism.html")
@app.route("/sa-200/professional-judgment")
def sa200_professional_judgment():
    return render_template("sa-200-professional-judgment.html")
@app.route("/sa-200/responsibilities")
def sa200_responsibilities():
    return render_template("sa-200-responsibilities.html")
@app.route("/sa-200/audit-risk")
def sa200_audit_risk():
    return render_template("sa-200-audit-risk.html")
@app.route("/sa-200/ethics")
def sa200_ethics():
    return render_template("sa-200-ethics.html")
@app.route("/sa-200/introduction")
def sa200_introduction():
    return render_template("sa-200-introduction.html")
@app.route("/sa-200/conduct-of-audit")
def sa200_conduct_of_audit():
    return render_template("sa-200-conduct-of-audit.html")
@app.route("/sa-200/scope")
def sa200_scope():
    return render_template("sa-200-scope.html")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import request, redirect, session

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Demo login (we'll replace later)
        if username == "student" and password == "audit123":
            session["user"] = username
            return redirect("/")
    
    return render_template("login.html")
