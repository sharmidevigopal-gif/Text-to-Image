import os
import torch
import gradio as gr
from diffusers import StableDiffusionPipeline


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_ID = "runwayml/stable-diffusion-v1-5"
OUTPUT_DIR = "generated_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# LOAD AI MODEL
# ============================================================

print("=" * 60)
print("AI TEXT-TO-IMAGE GENERATOR")
print("=" * 60)
print("Loading AI model...")
print("Please wait...")

try:
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        dtype=torch.float32
    )

    # Use CPU
    pipe = pipe.to("cpu")

    print("AI model loaded successfully!")

except Exception as e:
    print("ERROR while loading model:")
    print(e)
    raise


# ============================================================
# IMAGE GENERATION
# ============================================================

def generate_image(prompt, steps):

    if prompt is None or not prompt.strip():

        return (
            None,
            None,
            "⚠️ Please enter a text prompt."
        )

    try:

        print()
        print("=" * 60)
        print("Generating image...")
        print("Prompt:", prompt)
        print("Steps:", steps)
        print("=" * 60)

        image = pipe(
            prompt=prompt,
            num_inference_steps=int(steps)
        ).images[0]

        # Count existing images
        existing_files = [
            file for file in os.listdir(OUTPUT_DIR)
            if file.endswith(".png")
        ]

        image_number = len(existing_files) + 1

        filename = f"generated_image_{image_number}.png"

        filepath = os.path.abspath(
            os.path.join(
                OUTPUT_DIR,
                filename
            )
        )

        # Save image
        image.save(filepath)

        print("Image generated successfully!")
        print("Saved:", filepath)

        return (
            filepath,
            filepath,
            f"✅ Image generated successfully!\n\n"
            f"Prompt: {prompt}\n\n"
            f"Saved as: {filename}"
        )

    except Exception as e:

        print("ERROR:", e)

        return (
            None,
            None,
            f"❌ Error generating image:\n{str(e)}"
        )


# ============================================================
# CLEAR FUNCTION
# ============================================================

def clear_all():

    return (
        "",
        None,
        None,
        ""
    )


# ============================================================
# CUSTOM CSS
# ============================================================

custom_css = """

#title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
}

#subtitle {
    text-align: center;
    font-size: 18px;
}

#footer {
    text-align: center;
    font-size: 14px;
}

"""


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(
    title="AI Text-to-Image Generator",
    css=custom_css
) as app:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.Markdown(
        """
        <div id="title">
        🖼️ AI Text-to-Image Generator
        </div>

        <div id="subtitle">
        Transform your imagination into images using Artificial Intelligence
        </div>
        """
    )

    gr.Markdown("---")


    # --------------------------------------------------------
    # MAIN GENERATOR
    # --------------------------------------------------------

    with gr.Row():

        # LEFT SIDE
        with gr.Column():

            gr.Markdown(
                """
                ## ✍️ Create Your Image

                Enter a description of the image you want AI to create.
                """
            )

            prompt = gr.Textbox(
                label="Image Prompt",
                placeholder=(
                    "Example: A beautiful sunset over a mountain"
                ),
                lines=5
            )

            steps = gr.Slider(
                minimum=10,
                maximum=30,
                value=20,
                step=1,
                label="AI Generation Steps",
                info=(
                    "More steps can improve quality but "
                    "will increase generation time."
                )
            )

            with gr.Row():

                generate_button = gr.Button(
                    "🎨 Generate Image",
                    variant="primary"
                )

                clear_button = gr.Button(
                    "🧹 Clear"
                )


        # RIGHT SIDE
        with gr.Column():

            gr.Markdown(
                """
                ## 🖼️ Generated Image
                """
            )

            output_image = gr.Image(
                label="Result",
                type="filepath"
            )

            download_button = gr.File(
                label="💾 Download Generated Image",
                interactive=False
            )

            status = gr.Textbox(
                label="Generation Status",
                interactive=False,
                lines=4
            )


    gr.Markdown("---")


    # --------------------------------------------------------
    # EXAMPLE PROMPTS
    # --------------------------------------------------------

    gr.Markdown(
        """
        ## 💡 Example Prompts
        """
    )

    gr.Examples(
        examples=[
            ["A beautiful sunset over a mountain"],

            ["A futuristic city with flying cars at night"],

            ["A cute puppy playing in a garden"],

            ["A fantasy castle surrounded by clouds"],

            ["An astronaut walking on Mars"],

            ["A magical forest with glowing trees"],

            ["A colorful peacock in an Indian garden"],

            ["A traditional Indian village during sunset"],

            ["A robot exploring an alien planet"],

            ["A beautiful waterfall surrounded by green forest"]
        ],
        inputs=prompt
    )


    gr.Markdown("---")


    # --------------------------------------------------------
    # HOW THE SYSTEM WORKS
    # --------------------------------------------------------

    gr.Markdown(
        """
        ## 🔄 How It Works

        **1️⃣ Text Prompt**

        The user enters a natural-language description.

        **2️⃣ Text Understanding**

        The Stable Diffusion model interprets the description.

        **3️⃣ AI Image Generation**

        The AI generates an image based on the prompt.

        **4️⃣ Image Display**

        The generated image is displayed in the application.

        **5️⃣ Save and Download**

        The generated image is automatically saved and can be downloaded.
        """
    )


    gr.Markdown("---")


    # --------------------------------------------------------
    # ABOUT PROJECT
    # --------------------------------------------------------

    with gr.Accordion(
        "📚 About This Project",
        open=False
    ):

        gr.Markdown(
            """
            ## AI-Based Text-to-Image Generator

            This project demonstrates the use of Artificial
            Intelligence and Deep Learning to generate images
            from natural language text prompts.

            ### Technologies

            - Python
            - PyTorch
            - Hugging Face Diffusers
            - Stable Diffusion
            - Gradio
            - Pillow

            ### Model

            Stable Diffusion v1.5

            ### Input

            Natural language text prompt

            ### Output

            AI-generated image
            """
        )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    gr.Markdown(
        """
        <div id="footer">

        **AI Text-to-Image Generator**

        Developed using Python, PyTorch, Diffusers and Stable Diffusion.

        </div>
        """
    )


    # ========================================================
    # BUTTON ACTIONS
    # ========================================================

    generate_button.click(
        fn=generate_image,
        inputs=[
            prompt,
            steps
        ],
        outputs=[
            output_image,
            download_button,
            status
        ]
    )


    clear_button.click(
        fn=clear_all,
        inputs=[],
        outputs=[
            prompt,
            output_image,
            download_button,
            status
        ]
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("Starting Gradio application...")
    print("=" * 60)
    print()
    print("Open this address in your browser:")
    print("http://127.0.0.1:7860")
    print()

    app.launch()