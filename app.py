from flask import Flask, render_template, request
app = Flask(__name__)




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']

    headers = {'Authorization': 'Key f2f339a3cc374420a221fa27e58a3202'}
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    return render_template('home.html', results=response)

if __name__ == '__main__':
    app.run(debug=True)