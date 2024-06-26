from transformers import ViltProcessor, ViltForQuestionAnswering
import torch
import cv2
from PIL import Image
from icecream import ic

def load_models():
    """Load model and processor."""
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    return model, processor

def get_frame_from_camera(camera):
    """Capture a frame from the camera."""
    ret, frame = camera.read()
    if not ret:
        raise ValueError("Failed to capture frame")
    return frame

def get_answer(model, processor, frame, question):
    """Get the predicted answer for a given question and frame."""
    image = Image.fromarray(frame)
    inputs = processor(image, question, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]

def main():
    # Initialize models and processor
    model, processor = load_models()

    # Initialize webcam
    cap = cv2.VideoCapture('/dev/video0')

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
        ret, frame = cap.read(cv2.CAP_OPENNI_BGR_IMAGE)
        print(frame.shape)

        cv2.imshow('Frame', frame)
        question = input("Question >>> ")
        answer = get_answer(model, processor, frame, question)
        print("Predicted answer:", answer)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
