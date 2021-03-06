from flask import Flask, render_template, request
from data import Articles


app = Flask(__name__)

app.debug = True


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    articles = Articles()
    # for i in articles:
    #     print(i)
    return render_template('index.html', articles=articles)


@app.route('/<id>/article', methods=['GET', 'POST'])
def detail(id):
    if request.method == 'GET':
        articles = Articles()
        print(articles[int(id)-1])
        return render_template('detail.html', article=articles[int(id)-1])


if __name__ == '__main__':
    app.run()
