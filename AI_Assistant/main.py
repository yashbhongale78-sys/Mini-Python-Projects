from openai import OpenAI

key = "*********************************************************************************************"

messages = []

client = OpenAI(
    api_key = key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(messages = messages,
                                                    model = "gpt-4o"
                                                    )

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message["content"]}")

if __name__ == "__main__":
    print(f"Jarvis: hi i am jarvis , how may i help you ")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)