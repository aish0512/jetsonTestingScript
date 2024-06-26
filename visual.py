# Imports

from transformers import ViltProcessor, ViltForQuestionAnswering

from PIL import Image

import torch

from icecream import ic

def load_models():

    """Load model and processor."""

    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    return model, processor

def show_image(img_path):

    """Open and display an image."""

    image = Image.open(img_path)

    image.show()

    return image

def get_answer(model, processor, image, question):

    """Get the predicted answer for a given question and image."""

    inputs = processor(image, question, return_tensors="pt")

    with torch.no_grad():

        outputs = model(**inputs)

    logits = outputs.logits

    idx = logits.argmax(-1).item()

    return model.config.id2label[idx]

def main():

    # Initialize models and processor

    model, processor = load_models()

    # Display image

    img_path = "dog.jpeg"

    image = show_image(img_path)

    # Suggested questions

    suggestions = [

        "How many trees are there?",

        "What breed is the dog?",

        "What color is the bicycle?",

        "How many wheels has the bicycle?"

    ]

    ic(suggestions)

    # Question and Answer loop

    while True:

        question = input("Question >>> ")

        answer = get_answer(model, processor, image, question)

        print("Predicted answer:", answer)

if __name__ == "__main__":

    main()