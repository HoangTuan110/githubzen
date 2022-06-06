from flask import Flask, get_flashed_messages, flash
from mako.lookup import TemplateLookup
from httpx import get

app = Flask(__name__)

templates = TemplateLookup(directories=["./templates"], module_directory="/tmp/mako_modules")
def serve_template(name, **kwargs):
    template = templates.get_template(name)
    template.render(**kwargs)

@app.route('/')
def index():
    quote = get("https://api.github.com/zen")
    if quote.is_error:
        flash(f"Error {quote.status_code}")
        quote = ""
    return serve_template("index.html", quote=quote, messages=get_flashed_messages())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
