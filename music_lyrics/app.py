import os
import openai

# import sys
# sys.path.append('../../')

from key import key_dict

#print(key_dict['API_KEY'])
from random import choice
from flask import Flask, request, render_template

openai.api_key = key_dict['API_KEY']

app = Flask(__name__)

input_name = "Drake"


def get_story(input_name):
    artist = input_name.strip()
    prompt_text = 'Artist: {}\n\nLyrics:\n'.format(artist)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=256,
        frequency_penalty=0.5
    )

    story = response['choices'][0]['text']
    print(story)
    return story

#get_story(input_name)

@app.route('/lyrics', methods=['POST'])
def answer():
    print('answer called')
    artist = request.form['artist']
    song = request.form['song']
    prompt_text = 'Artist: {}\nSong: {}\nLyrics:\n'.format(artist, song)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=256,
        frequency_penalty=0.5
    )
    lyrics = response['choices'][0]['text']
    #lyrics = lyrics.replace("\n", "<br />")

    lyrics = lyrics.split("\n")

    return render_template('lyrics.html', lyrics=lyrics, artist=artist, song=song)

@app.route('/')
def index():
    print("at index")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)