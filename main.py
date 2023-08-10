from tkinter import Tk, filedialog, ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("550x550")
        self.root.title("Watermark App")

        self.image_path = ""
        self.logo_path = ""
        self.watermarked_image = None
        self.font_path = "WinterSong-owRGB.ttf"  # Replace with the correct font path

        self.frm = ttk.Frame(root, padding=30)
        self.frm.pack()

        self.image_label = ttk.Label(self.frm)
        self.image_label.pack()

        self.upload_button = ttk.Button(self.frm, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_button = ttk.Button(self.frm, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            image = Image.open(self.image_path)
            self.display_image(image)

    def display_image(self, image):
        image.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(image)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def add_watermark(self):
        if not self.image_path:
            return

        watermark_text = "Your Watermark Here"
        watermark_color = (255, 255, 255, 0)  # White with transparency

        image = Image.open(self.image_path)
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size

        draw.font = ImageFont.truetype(self.font_path, 20)  # Use self.font_path
        draw.text((image_width - 190, image_height - 45), text=watermark_text, font=draw.font, fill=watermark_color)

        # Convert the image to RGB mode before saving as JPEG
        rgb_image = image.convert("RGB")

        self.watermarked_image = rgb_image

        self.display_image(image)
        output_path = "watermarked_image.jpg"  # Specify the desired output path
        self.watermarked_image.save(output_path, format="JPEG", quality=95)  # Save as JPEG with 95% quality

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    app.run()

