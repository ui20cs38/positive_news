from flask import Flask
from textblob import TextBlob
import requests
import json



app = Flask(__name__)

@app.route("/members")
def members():
    response_API = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=b65dabe6d3904d6082531a05cca6ba4a')   
    data = response_API.text
    parse_json = json.loads(data)
    count = 0
    data = []
    for i in range (len(parse_json['articles'])):
        text = parse_json['articles'][i]['title']
        blob = TextBlob(text)
        k = blob.sentiment.polarity
        # print(k)
        if(k>=0):
            print(text)
            print(parse_json['articles'][i]['urlToImage'])
            count = count + 1
            title = text
            image = parse_json['articles'][i]['urlToImage']
            url = parse_json['articles'][i]['url']
            if(image!=None):
                data.append([title, image, url])
    

    # data = json.dumps(data)
    
    return data

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')