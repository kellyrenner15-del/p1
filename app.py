from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ------------------------
# 页面路由（全部放这里）
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/stock-risk-guide")
def stock_risk_guide():
    return render_template("stock_risk_guide.html")

@app.route("/per-explained")
def per_explained():
    return render_template("per_explained.html")

@app.route("/pbr-explained")
def pbr_explained():
    return render_template("pbr_explained.html")

@app.route("/roe-explained")
def roe_explained():
    return render_template("roe_explained.html")

# ------------------------
# SEO 文件（全部放这里）
# ------------------------
@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(app.root_path, "robots.txt")

@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.root_path, "sitemap.xml")


# ------------------------
# 只在本地运行用（只放 app.run）
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)