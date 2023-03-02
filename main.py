from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def title():
    return f"""<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                   </head>
                   <body>
                     <h2>Миссия Колонизация Марса</h2>
                   </body>
                 </html>"""


@app.route('/index/')
def index():
    return f"""<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                   </head>
                   <body>
                     <h3>И на Марсе будут яблони цвести!</h3>
                   </body>
                 </html>"""


@app.route('/promotion')
def promotion():
    a = ["Человечество вырастает из детства.</p>",
         "Человечеству мала одна планета.</p>",
         "Мы сделаем обитаемыми безжизненные пока планеты.</p>",
         "И начнем с Марса!</p>",
         "Присоединяйся!</p>"]
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Рекламная кампания</title>
                  </head>
                  <body>
                    <h2>{'<p>'.join(a)}</h2>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
