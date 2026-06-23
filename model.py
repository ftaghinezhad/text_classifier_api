def predict(text):

    text = text.lower()

    if "love" in text:
        return "positive"

    return "negative"
