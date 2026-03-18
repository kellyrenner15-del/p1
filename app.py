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

@app.route("/stock-risk-basics")
def stock_risk_basics():
    return render_template("stock_risk_basics.html")

@app.route("/stock-analysis-guide")
def stock_analysis_guide():
    return render_template("stock_analysis_guide.html")

@app.route("/what-is-eps")
def what_is_eps():
    return render_template("what_is_eps.html")

@app.route("/what-is-bps")
def what_is_bps():
    return render_template("what_is_bps.html")

@app.route("/dividend_yield_explained")   # ← 改成下划线
def dividend_yield_explained():
    return render_template("dividend_yield_explained.html")


@app.route("/what_is_rsi")                # ← 改成下划线
def what_is_rsi():
    return render_template("what_is_rsi.html")

@app.route("/moving_average_explained")
def moving_average_explained():
    return render_template("moving_average_explained.html")

@app.route("/macd_explained")
def macd_explained():
    return render_template("macd_explained.html")

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

@app.route("/dividend_payout_ratio_explained")
def dividend_payout_ratio_explained():
    return render_template("dividend_payout_ratio_explained.html")


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