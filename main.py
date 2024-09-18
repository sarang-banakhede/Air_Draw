'''author: Sarang Banakhede'''

from HandGesture import HandGesture
import numpy as np
from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline

def generate_image(input_image, prompt, model_id="CompVis/stable-diffusion-v1-4", strength=0.75, num_inference_steps=50):
    pipeline = StableDiffusionImg2ImgPipeline.from_pretrained(model_id)
    if torch.cuda.is_available():
        pipeline.to("cuda")
    generated_images = pipeline(prompt=prompt, image=input_image, strength=strength, num_inference_steps=num_inference_steps)
    return generated_images.images[0]

if __name__ == "__main__":
    hand = HandGesture()
    coordinates = hand.draw()
    
    img = np.ones((100, 100), np.uint8) * 255
    for coord in coordinates:
        x = int(coord[0] * 100)
        y = int(coord[1] * 100)
        if 0 <= x < 100 and 0 <= y < 100:
            img[y, x] = 0
    
    img_rgb = np.stack((img,)*3, axis=-1)
    img_pil = Image.fromarray(img_rgb.astype('uint8'), 'RGB')
    
    img_pil = img_pil.resize((256, 256), Image.LANCZOS)
    
    generated_img = generate_image(img_pil, 'colourfull house', strength=0.75, num_inference_steps=50)
    
    generated_img.save("generated_image.png")

    print("Image generated and saved successfully.")