from flask import Flask, render_template, url_for
from config import LOAD_DOTENV, DEBUG

app = Flask(__name__)

posts = [
    {
        'author': 'Andi Sugandi',
        'title': 'Blog Post 1',
        'content': 'Ini adalah konten blog pertama.',
        'date_posted': 'June 1, 2019'
    },
    {
        'author': 'Andi Sugandi',
        'title': 'Blog Post 2',
        'content': 'Ini adalah konten blog kedua.',
        'date_posted': 'June 2, 2019'
    },
    {
        'author': 'Julia Novianti',
        'title': 'Blog Post 3',
        'content': 'Ini adalah konten blog ketiga.',
        'date_posted': 'June 3, 2019'
    }
]


@app.route("/")
def index():
    title_of_slider = "WE GONNA HELP YOU MAKE AN IMPACT"
    desc_of_slider = "Our expertise will guide you to success. Without Fail."
    return render_template("index.html", tite_of_slider=title_of_slider,
        desc_of_slider=desc_of_slider
    )

@app.route("/blog")
def blog():
    title_of_slider = "Hot Off The Press"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("blog.html", precomposed="OK", title="Blog", posts=posts,
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/about")
def about():
    title_of_slider = "About Us"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("about-us.html", precomposed="OK", title="About Us",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider 
    )

@app.route("/services")
def services():
    title_of_slider = "Our Services"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("services.html", precomposed="OK", title="Our Services",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/portfolio")
def portfolio():
    title_of_slider = "Our Works"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("portfolio.html", precomposed="OK", title="Our Works",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/contact")
def contact():
    title_of_slider = "Get In Touch"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("contact.html", precomposed="OK", title="Contact Us",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/project-item")
def project_item():
    title_of_slider = "Single Project"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("project-single.html", precomposed="OK", title="Single Project",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/blog-item")
def blog_item():
    title_of_slider = "Hot Off The Press"
    desc_of_slider = "Of an or game gate west face shed. ﻿no great but music too old found arose."
    return render_template("blog-single.html", precomposed="OK", title="Blog",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.route("/404")
def error_404():
    title_of_slider = "Uh Oh, a 404 Error"
    desc_of_slider = "The Page you are looking for doesn't exist or an other error occurred. Head home to try again."
    return render_template("404.html", title="404",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    )

@app.errorhandler(404)
def page_not_found(error):
    title_of_slider = "Uh Oh, a 404 Error"
    desc_of_slider = "The Page you are looking for doesn't exist or an other error occurred. Head home to try again."
    return render_template("404.html", title="404",
        title_of_slider=title_of_slider, desc_of_slider=desc_of_slider
    ), 404