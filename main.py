from flask import Flask, url_for, request, render_template, redirect
from login_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, title='Тренировки в полёте')


@app.route('/')
@app.route('/index/<title>')
def index(title="Миссия на марс"):
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {"title": "Автоматический ответ",
             "surname": "Watny",
             "name": "Mark",
             "education": "выше среднего",
             "profession": "штурман марсохода",
             "sex": "male",
             "motivation": "Всегда мечтал застрять на Марсе!",
             "ready": "True"}
    return render_template("auto_answer.html", **param)


# @app.route('/')
# def title():
#     return f"""<!doctype html>
#                  <html lang="en">
#                    <head>
#                      <meta charset="utf-8">
#                    </head>
#                    <body>
#                      <h2>Миссия Колонизация Марса</h2>
#                    </body>
#                  </html>"""
#
#
# @app.route('/index/')
# def index():
#     return f"""<!doctype html>
#                  <html lang="en">
#                    <head>
#                      <meta charset="utf-8">
#                    </head>
#                    <body>
#                      <h3>И на Марсе будут яблони цвести!</h3>
#                    </body>
#                  </html>"""


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


@app.route('/list_prof/')
@app.route('/list_prof/<prof>')
def list_prof(prof='ol'):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', prof=prof, title='Список', professions=professions)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                     <html lang="en">
                       <head>
                         <meta charset="utf-8">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                         <title>Предложение</title>
                       </head>
                       <body>
                         <h1>Результаты отбора</h1>
                         <h3>Претендента на участие в миссии {nickname}:</h3>
                         <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                         <div class="alert alert-light" role="alert">составляет {rating}</div>
                         <div class="alert alert-warning" role="alert">Желаем удачи!</div>
  
                       </body>
                     </html>"""


@app.route('/choice/<planet_name>')
def offer(planet_name):
    planets = {'Меркурий': ["Это самая маленькая планета солнечной системы;", "Самая близкая к Солнцу;",
                            "Год на нём значительно короче — всего 88 земных суток;",
                            "Является одной из двух каменистых планет;", "Нет полноценной атмосферы."],
               'Венера': ["вторая планета от Солнца;", "её размеры и масса очень близки к земным;",
                          "окутана очень плотным слоем облаков;", "нагревается до 480°C;",
                          "День - около 243 земных суток."],
               'Земля': ["третья планета от Солнца;", "крупнейшая в земной группе;", "хорошо различимы сезоны года;",
                         "Земля имеет спутник — Луну;", "Очень красива!"],
               'Марс': ["Эта планета близка к земле;", "На ней много необходимых ресурсов;", "Есть вода и атмосфера;",
                        "Небольшое магнитное поле;", "Она просто красива!"],
               'Юпитер': ["самая большая из планет-гигантов;", "является газовым гигантом;",
                          "Сильнейшее в системе магнитное поле;", "четыре крупнейших спутника Юпитера;",
                          "Юпитер — имя римского царя богов."],
               'Сатурн': ["Шестая планета от Солнца;", "металлосиликатное ядро;", "впечатляющая система из семи колец;",
                          "82 спутника;", "Наклон оси Сатурна напоминает земной."],
               'Уран': ["Седьмая планета от Солнца;", "Атмосфера планеты окрашена в однородный сине-зелёный цвет;",
                        "ядро состоит изо льдов;",
                        "самая холодная планета в системе;", "окружён кольцами."],
               'Нептун': ["ледяной гигант;", "самая далёкая от Солнца планета;", "Год длится примерно 165 земных лет;",
                          "Атмосфера состоит из соединений гелия и водорода;", "каменное ядро."]}
    planet = planets.get(planet_name)
    return f"""<!doctype html>
                     <html lang="en">
                       <head>
                         <meta charset="utf-8">
                         <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                         crossorigin="anonymous">
                         <title>Предложение</title>
                       </head>
                       <body>
                         <h1>Мое предложение: {planet_name}</h1>
                         <div class="alert alert-secondary" role="alert">{planet[0].capitalize()}</div>
                         <div class="alert alert-success" role="alert">{planet[1].capitalize()}</div>
                         <div class="alert alert-secondary" role="alert">{planet[2].capitalize()}</div>
                         <div class="alert alert-warning" role="alert">{planet[3].capitalize()}</div>
                         <div class="alert alert-danger" role="alert">{planet[4].capitalize()}</div>
                       </body>
                     </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Реклама с картинкой</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                            width="300" height="300" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-secondary" role="alert">Человечество вырастает из детства.</div>
                        <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                        <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="alert alert-warning" role="alert">И начнем с Марса!</div>
                        <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
