from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output_image_path, font_path='D:/#Work Folder/2D_3D_Assets/Fonts/Carista.ttf'):
    # Create an image with A4 dimensions
    img = Image.new('RGB', (int(A4[0]), int(A4[1])), color='white')
    draw = ImageDraw.Draw(img)

    # Load the font
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)

    # Set initial position for drawing text
    x, y = 50, 50

    # Draw each line of text
    for line in text.split('\n'):
        draw.text((x, y), line, fill='black', font=font)
        y += font_size + 10  # Adjust the vertical spacing

    # Save the image
    img.save(output_image_path)

def create_pdf(image_path, output_pdf_path):
    # Create a PDF with A4 dimensions
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    c.drawImage(image_path, 50, 50, width=500, height=700)  # Adjust the position and size as needed
    c.save()

def main():
    # Get text input from the user
    text_input = input("Enter the text you want to convert to handwriting: ")

    # Define the paths for the image and PDF output
    image_path = 'output_image.png'
    pdf_path = 'output_document.pdf'

    # Convert text to handwriting and save it as an image
    text_to_handwriting(text_input, image_path)

    # Create a PDF document and add the handwriting image to it
    create_pdf(image_path, pdf_path)

    print(f"PDF document saved at {pdf_path}")

if __name__ == "__main__":
    main()