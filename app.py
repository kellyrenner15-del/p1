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

# ===== 新增的三个页面 =====
@app.route("/dividend-payout-ratio-explained")
def dividend_payout_ratio_explained():
    return render_template("dividend_payout_ratio_explained.html")

@app.route("/stock-analysis-guide")
def stock_analysis_guide():
    return render_template("stock_analysis_guide.html")

@app.route("/stock-risk-basics")
def stock_risk_basics():
    return render_template("stock_risk_basics.html")

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

# ===== Sitemap（直接在代码中） =====
@app.route("/sitemap.xml")
def sitemap():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://wuelefo.com/</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/beginner-guide</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/per-explained</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/pbr-explained</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/roe-explained</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/what-is-eps</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/what-is-bps</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/dividend_yield_explained</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/what_is_rsi</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/moving_average_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/macd_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/stock-risk-guide</loc>
    <lastmod>2026-03-19</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/bollinger_bands_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/volume_analysis_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/support_and_resistance_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/candlestick_patterns_explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/how_to_read_a_balance_sheet</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/how_to_read_an_income_statement</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/how_to_read_a_cash_flow_statement</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/dividend-payout-ratio-explained</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/stock-analysis-guide</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/stock-risk-basics</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/about</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/contact</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/privacy</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://wuelefo.com/terms</loc>
    <lastmod>2026-03-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>'''
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