from flask import Flask, request
from db import blog_list
import math

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "Hello World!"


@app.get("/api/blogs")
def get_blogs():
    # Get blogs from pagination config settings
    cur_page = int(request.args.get('page', 1)) - 1
    search = request.args.get('search', '')

    filtered_blogs = []
    for blog in blog_list:
        if search.lower().strip() in blog["category"].lower():
            filtered_blogs.append(blog)

    items_per_page = 9
    total_posts = len(filtered_blogs)
    total_page = math.ceil(total_posts / items_per_page)
    if cur_page > total_page - 1:
        cur_page = total_page - 1
    start = cur_page * 9
    end = (cur_page + 1) * 9

    if end > total_posts:
        end = total_posts
    return {"blogs": filtered_blogs[start:end], "total_page": total_page}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True, load_dotenv=True)
