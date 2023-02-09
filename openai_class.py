import openai
import env_variables
class oai:

    def question(gpt_prompt):
        openai.api_key = env_variables.variabbles.OPEN_AI_KEY

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=gpt_prompt,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        return response['choices'][0]['text']
