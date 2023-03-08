import openai
from gtts import gTTS
from playsound import playsound
from confidencial import senha

openai.api_key = senha

audio = 'audio.mp3'
language = 'pt-br'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Me faça um texto sobre: 'o poder permeia a sociedade'"},
  ]
)

print(completion.choices[0]['message']['content'])

sp = gTTS(
  text=completion.choices[0]['message']['content'],
  lang=language
)

sp.save(audio)
playsound(audio)
