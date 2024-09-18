# Hand Gesture Drawing & Image Generation
(see demo :- https://www.linkedin.com/posts/sarang-banakhede-79327823a_aiart-generativeai-computervision-activity-7242262183466684417-NSro?utm_source=share&utm_medium=member_desktop)

This project allows users to draw using hand gestures and generate images based on the drawings with the help of a Stable Diffusion model. It uses MediaPipe to detect hand landmarks and track the movement of the index finger for drawing. When the index and middle fingers come close, the drawing is paused. The drawn image is then processed and used as input to generate a new image based on a user-provided text prompt.

# Features
* Hand Gesture Detection: Utilizes MediaPipe to track hand gestures and detect when to draw based on finger positions.
* Drawing: Index finger movements are tracked to draw lines, and the drawing is paused when fingers are close together.
* Image Generation: Uses the drawn image as input to the Stable Diffusion model to generate an AI-based image from a text prompt.

# How to use
* Create a Virtual Environment (python -m venv venv)
* Activate the Virtual Environment(venv\Scripts\activate)
* Install Dependencies (pip install -r requirements.txt)
* Run main.py (python main.py)
  
# Contributing
Contributions to improve the project are welcome. Please feel free to fork the repository and submit pull requests.
