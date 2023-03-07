import openai

class GPT():
    def __init__(self, api_key) -> None:
        openai.api_key = api_key
        self.model = "gpt-3.5-turbo"

    def send(self, text, onlytext=True):
        output = openai.ChatCompletion.create(
            model = self.model, 
            messages = [
                {
                    "role": "user", 
                    "content": text
                }
            ]
        )
        if onlytext:
            return output['choices'][0]['message']['content'].strip()
        else:
            return output
