from flask import Flask,render_template,request
import pyjokes

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    lang=request.args.get('language','en')
    joke=pyjokes.get_joke(language=lang)
    return render_template('Joke_HTML.html',joke=joke,lang=lang)
    #return f'<h3>{joke}</h3>'
@app.route('/MultipleJokes')
def jokes():
    jokes=pyjokes.get_jokes()
    return f'<h3>{jokes}</h3>'
if __name__== "__main__":
    app.run(debug=True)