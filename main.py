import openai
import env_variables

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    import os
    import openai

    openai.api_key = env_variables.variables.OPEN_AI_KEY

    gpt_prompt = "Nalewak nb02 nie działa, czy to kwestia aplikacji?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    print(response['choices'][0]['text'])






