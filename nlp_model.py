class NLPModel:
    def __init__(self):
        pass

    def predict(self, text):
        # A simple model function to predict text sentiment (example)
        if "good" in text.lower():
            return "Positive"
        else:
            return "Negative"
