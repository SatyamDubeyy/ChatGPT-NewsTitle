import openai
def generateTitles(title):
    openai.api_key="YOUR-CHATGPT-API-KEY" #Enter Your API Key

    model_engine="text-davinci-003"
    prompt=f"Suppose You are a News Reporter.Reword the title with minimum 55 characters and maximum 70 characters in 20 different ways. This is important, do not exceed the character minimum or maximum limits: {title}. Do not include the source of the news, or the website name"
    # print(prompt)
    completion=openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response=completion.choices[0].text
    return response