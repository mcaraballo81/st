#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
!pip install openai
import openai
openai.api_key = "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"

#using Open Ai from Python
def chatGPT_query():
  user_input = input("Ask open AI: ")
  completion = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=1000)

  print(completion.choices[0]['text'])

chatGPT_query()
