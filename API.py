(задаём ввопрос гпт чату)
import openai
# Здесь нужно указать ваш API-ключ от OpenAI
api_key = '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'
def generate_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # Выберите подходящий движок для задачи
        prompt=prompt,
        max_tokens=50,  # Максимальное количество токенов в ответе
    )
    return response.choices[0].text
# Пример вопроса о плане для доклада
question = "write a general plan for the report (world economy) your plan should contain at least 5 sections directly revealing the topic, your answer should consist only of the names of the sections.  In addition, number the names of the sections so 1,2,3, and so on"
response = generate_response(question)
# Сохранить ответ в файл 2.txt
with open("2.txt", "w", encoding="utf-8") as file:
    file.write(response)
print("Ответ сохранен в файле 2.txt")

@@@
@@@
@@@
@@@
@@@

const Telegraf = require("telegraf")
const Openai = require("openai")
const telegramToken = ""
const openaiKey = ""
const bot = new Telegraf.Telegraf(telegramToken)
const configuration = new Openai.Configuration({
    apiKey: openaiKey
})
const openai = new Openai.OpenAIApi(configuration)
bot.on("text", async (ctx) => {
    const chatResponse = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{role: "user", content: ctx.message.text}]
    })
    ctx.reply(chatResponse.data.choices[0].message.content)
})
bot.launch()

@@@
@@@
@@@
@@@
@@@

import g4f
# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True,
)
for message in response:
    print(message, flush=True, end='')
















