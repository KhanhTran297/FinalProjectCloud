from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def base():
    return render_template("index.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/tintuc")
def tintuc():
    return render_template("tintuc.html")

@app.route("/tuyendung")
def tuyendung():
    return render_template("tuyendung.html")

@app.route("/gioithieu")
def gioithieu():
    return render_template("gioithieu.html")

@app.route("/trungtambaohanh")
def trungtambaohanh():
    return render_template("trungtambaohanh.html")

@app.route("/lienhe")
def lienhe():
    return render_template("lienhe.html")

@app.route("/giohang")
def giohang():
    return render_template("giohang.html")

@app.route("/nguoidung")
def nguoidung():
    return render_template("nguoidung.html")
@app.route("/admin.html")
def admin():
    return render_template("admin.html")
@app.route("/chitietsanpham")
def chitietsanpham():
    return render_template("chitietsanpham.html")

if __name__=='__main__':    
    app.run(debug=True)
