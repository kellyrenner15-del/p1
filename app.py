from flask import Flask, render_template, send_from_directory, request, jsonify
import os

app = Flask(__name__)


# =========================
# 页面路由
# =========================
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


# =========================
# search（可选，占位防报错）
# =========================
@app.route("/search")
def search():
    q = (request.args.get("q") or "").strip()
    return render_template("index.html", q=q)


# =========================
# SEO 文件
# =========================
@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(app.root_path, "robots.txt")


@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.root_path, "sitemap.xml")


# =========================
# API（以后可给 JS 用）
# =========================
@app.route("/api/basic_result")
def api_basic_result():
    q = (request.args.get("q") or "").strip()
    has_number = any(ch.isdigit() for ch in q)

    return jsonify({
        "type": f"コード入力：{q}" if has_number else f"名称入力：{q}",
        "risk": "中（参考）" if has_number else "低〜中（参考）",
        "note": "公開情報を元にした要約表示です。詳細はLINEで確認できます。"
    })
@app.route("/terms")
def terms():
    return render_template("terms.html")

# =========================
# 启动
# =========================
if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug)