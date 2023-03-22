from transformers import pipeline


class TextGenerator:
    def __init__(self, tokenizer, model):
        self.tokenizer = tokenizer
        self.model = model

        # Instantiate a text generation pipeline
        self.text_generator = pipeline("text-generation", tokenizer=tokenizer, model=model)

    def generate(self, context: str, max_length: int):

        # Generate text
        return self.text_generator(context, max_length=max_length)
