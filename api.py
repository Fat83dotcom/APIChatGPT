import openai
from gtts import gTTS
from playsound import playsound

openai.api_key = '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'

audio = 'audio.mp3'
language = 'pt-br'

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "De que é feita a terra?"},
  ]
)

print(completion.choices[0]['message']['content'])

sp = gTTS(
  text=completion.choices[0]['message']['content'],
  lang=language
)

sp.save(audio)
playsound(audio)
