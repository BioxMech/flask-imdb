from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def show_landing_page():
    try:
        return render_template("landing-page.html")
    except:
        return "An error occured"

@app.route("/search", methods=['POST'])
def form_submit():
    user_query = request.form['search_query'] # matches name attribute of query string input (HTML)
    print(user_query)
    redirect_url = url_for('.search_imdb', query_string=user_query) # match search_imdb function name (Python flask)
    print(redirect_url)
    return redirect(redirect_url)

@app.route("/search/<query_string>", methods=['GET'])
def search_imdb(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = { "q": query_string }
    headers = {
        'x-rapidapi-key': "a9f67b394bmsh3d855b0ba715489p12ec45jsnd2c21c5c47b3",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data=data)
    except:
        return render_template("error404.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)