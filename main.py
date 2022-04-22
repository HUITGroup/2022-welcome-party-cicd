from flask import Flask, Response, request, render_template
import caliculate as cal

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return Response(response=render_template('index.html', status=200))
    if request.method == 'POST':
        raw_num1 = request.form.get('num1')
        raw_num2 = request.form.get('num2')
        ope = request.form.get('operator')
        if len(raw_num1) == 0 or len(raw_num2) == 0:
            return Response(response=render_template('index.html', answer='error', status=200))

        num1 = int(raw_num1)
        num2 = int(raw_num2)

        if ope == 'add':  # 加算
            return Response(response=render_template('index.html', answer=str(cal.add(num1, num2)), status=200))
        elif ope == 'sub':  # 減算
            return Response(response=render_template('index.html', answer=str(cal.sub(num1, num2)), status=200))
        elif ope == 'mul':  # 乗算
            return Response(response=render_template('index.html', answer=str(cal.mul(num1, num2)), status=200))
        elif ope == 'div':  # 除算
            return Response(response=render_template('index.html', answer=str(cal.div(num1, num2)), status=200))
        else:
            return Response(response=render_template('index.html', answer='error', status=200))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
