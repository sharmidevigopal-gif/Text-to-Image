# AI Text-to-Image Generator

## Project Description

AI Text-to-Image Generator is a Python-based application that uses Artificial Intelligence and Deep Learning to generate images from natural-language text prompts.

The application uses the Stable Diffusion v1.5 model with Hugging Face Diffusers and provides a simple Gradio web interface.

## Technologies Used

- Python
- PyTorch
- Hugging Face Diffusers
- Stable Diffusion v1.5
- Gradio
- Pillow

## Features

- Generate images from text prompts
- Adjustable AI generation steps
- Display generated images
- Automatically save generated images
- Download generated images
- Clear input and output
- Example prompts for easy testing
- Simple Gradio web interface

## Project Structure

```text
Text-to-Image/
│
├── app.py
├── generate.py
├── requirements.txt
├── .gitignore
└── README.md

Requirements
Python 3.x
Internet connection
Sufficient RAM and storage
CPU support

The Stable Diffusion model is downloaded when the application is run for the first time.

Installation and Setup
1. Clone the Repository
git clone https://github.com/sharmidevigopal-gif/Text-to-Image.git
2. Open the Project Folder
cd Text-to-Image
3. Create a Virtual Environment

For Windows:

python -m venv venv
4. Activate the Virtual Environment

For Windows PowerShell:

venv\Scripts\Activate.ps1
5. Install Required Packages
pip install -r requirements.txt
6. Run the Application
python app.py
7. Open the Application

After starting the program, open the following address in your web browser:

http://127.0.0.1:7860
How to Use
Enter a text description in the Image Prompt box.
Select the required AI Generation Steps.
Click Generate Image.
Wait while Stable Diffusion generates the image.
The generated image will appear in the application.
The image is automatically saved in the generated_images folder.
Use the download option to save the generated image.
Example Prompts
A beautiful sunset over a mountain
A futuristic city with flying cars at night
A cute puppy playing in a garden
A fantasy castle surrounded by clouds
An astronaut walking on Mars
A magical forest with glowing trees
A colorful peacock in an Indian garden
A traditional Indian village during sunset
A robot exploring an alien planet
A beautiful waterfall surrounded by green forest
How the System Works
Text Prompt
     ↓
Stable Diffusion Model
     ↓
AI Image Generation
     ↓
Generated Image
     ↓
Display and Save Image
Output

The generated images are automatically stored in:

generated_images/
Model

Stable Diffusion v1.5

Model ID:

runwayml/stable-diffusion-v1-5
Important Note

The application currently runs the Stable Diffusion model using the CPU. Image generation may therefore take some time depending on the computer's hardware.

An internet connection is required when the model needs to be downloaded
