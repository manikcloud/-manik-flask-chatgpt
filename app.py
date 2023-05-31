@app.route("/message", methods=["POST"])
def chat_message():
    user_message = request.json["message"]

    if is_cloud_infrastructure_question(user_message):
        messages = [
            {
                "role": "system",
                "content": "You are an AI specialized in cloud infrastructure.",
            },
            {"role": "user", "content": user_message},
        ]

        model_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        bot_response = model_response["choices"][0]["message"]["content"]

        # write chat history to a file
        with open("/app/history/chat-history.txt", "a") as file:
            file.write("User: " + user_message + "\n")
            file.write("AI: " + bot_response + "\n")

        return jsonify({"message": bot_response})
    else:
        return jsonify({"message": "Please ask a question related to cloud infrastructure."})
