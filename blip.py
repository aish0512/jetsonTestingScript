import cv2
import requests
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large")

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to PIL format
    raw_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Your question
    question = "What can you see in the picture?"

    # Process the image and question
    inputs = processor(raw_image, question, return_tensors="pt")

    # Generate answer
    out = model.generate(**inputs)

    # Decode and print the answer
    answer = processor.decode(out[0], skip_special_tokens=True)
    print("Answer:", answer)

    # Display the frame with the answer
    cv2.putText(frame, answer, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Webcam', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()

