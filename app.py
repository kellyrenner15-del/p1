from flask import Flask, render_template

app = Flask(__name__)

# ===== 首页 =====
@app.route("/")
def home():
    return render_template("index.html")

# ===== 基礎知識 ===== 
@app.route("/per-explained")
def per_explained():
    return render_template("per_explained.html")

@app.route("/pbr-explained")
def pbr_explained():
    return render_template("pbr_explained.html")

@app.route("/roe-explained")
def roe_explained():
    return render_template("roe_explained.html")

@app.route("/what-is-eps")
def what_is_eps():
    return render_template("what_is_eps.html")

@app.route("/what-is-bps")
def what_is_bps():
    return render_template("what_is_bps.html")

@app.route("/dividend_yield_explained")
def dividend_yield_explained():
    return render_template("dividend_yield_explained.html")

@app.route("/what_is_rsi")
def what_is_rsi():
    return render_template("what_is_rsi.html")

@app.route("/moving_average_explained")
def moving_average_explained():
    return render_template("moving_average_explained.html")

@app.route("/macd_explained")
def macd_explained():
    return render_template("macd_explained.html")

# ===== 実践ガイド =====
@app.route("/beginner-guide")
def beginner_guide():
    return render_template("beginner_guide.html")

@app.route("/stock-risk-guide")
def stock_risk_guide():
    return render_template("stock_risk_guide.html")

@app.route("/bollinger_bands_explained")
def bollinger_bands_explained():
    return render_template("bollinger_bands_explained.html")

@app.route("/volume_analysis_explained")
def volume_analysis_explained():
    return render_template("volume_analysis_explained.html")

@app.route("/support_and_resistance_explained")
def support_and_resistance_explained():
    return render_template("support_and_resistance_explained.html")

@app.route("/candlestick_patterns_explained")
def candlestick_patterns_explained():
    return render_template("candlestick_patterns_explained.html")

@app.route("/how_to_read_a_balance_sheet")
def how_to_read_a_balance_sheet():
    return render_template("how_to_read_a_balance_sheet.html")

@app.route("/how_to_read_an_income_statement")
def how_to_read_an_income_statement():
    return render_template("how_to_read_an_income_statement.html")

@app.route("/how_to_read_a_cash_flow_statement")
def how_to_read_a_cash_flow_statement():
    return render_template("how_to_read_a_cash_flow_statement.html")

# ===== その他 =====
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

# ===== Sitemap（从文件读取） =====
@app.route("/sitemap.xml")
def sitemap():
    with open('static/sitemap.xml', 'r', encoding='utf-8') as f:
        xml = f.read()
    response = app.make_response(xml)
    response.headers['Content-Type'] = 'application/xml; charset=utf-8'
    return response

# ===== robots.txt =====
@app.route("/robots.txt")
def robots():
    txt = '''User-agent: *
Allow: /
Disallow: /admin/

Sitemap: https://wuelefo.com/sitemap.xml

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /
'''
    response = app.make_response(txt)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(debug=False)