from nlp_model import NLPModel

def test_nlp_model_prediction():
    model = NLPModel()

    # Test case for positive sentiment prediction
    text_positive = "This is a good example."
    assert model.predict(text_positive) == "Positive"

    # Test case for negative sentiment prediction
    text_negative = "This is a bad example."
    assert model.predict(text_negative) == "Positive"
