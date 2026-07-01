from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]
    job = request.form["job"]


    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()


    skills = [
        "python",
        "java",
        "html",
        "css",
        "javascript",
        "machine learning",
        "ai",
        "sql"
    ]


    found = []
    missing = []


    for skill in skills:

        if skill in text.lower() and skill in job.lower():
            found.append(skill)

        else:
            missing.append(skill)


    score = int((len(found)/len(skills))*100)


    return f"""

<html>

<head>

<style>

body{{
font-family: Arial;
background:#f2f2f2;
text-align:center;
}}

.card{{
background:white;
width:500px;
margin:40px auto;
padding:30px;
border-radius:15px;
}}

.score{{
font-size:30px;
color:green;
}}

</style>

</head>


<body>


<div class="card">


<h1>🤖 AI Resume Analysis</h1>


<h2 class="score">
Match Score: {score}%
</h2>


<h3>✅ Matched Skills</h3>

<p>
{found}
</p>



<h3>❌ Missing Skills</h3>

<p>
{missing}
</p>



</div>


</body>


</html>

"""


if __name__ == "__main__":
    app.run(debug=True)