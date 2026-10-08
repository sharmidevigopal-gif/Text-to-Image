import torch
from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")

prompt = input("Enter your image prompt: ")

image = pipe(
    prompt,
    num_inference_steps=20
).images[0]

image.save("generated_image.png")

print("Image generated successfully!")
print("Saved as: generated_image.png")