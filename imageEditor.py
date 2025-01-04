from tkinter import Tk, filedialog, Button, Label, Entry, messagebox, Scale, HORIZONTAL
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

# Global variables
original_image = None
edited_image = None
undo_stack = []

# Function to open an image
def open_image():
    global original_image, edited_image, undo_stack
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        original_image = Image.open(file_path)
        edited_image = original_image.copy()
        undo_stack.clear()
        display_image(edited_image)

# Function to display an image
def display_image(img):
    img.thumbnail((300, 300))  # Resizing the image for display
    tk_image = ImageTk.PhotoImage(img)
    image_label.config(image=tk_image)
    image_label.image = tk_image

# Function to save the current state after the undo application
def save_state():
    global undo_stack, edited_image
    if edited_image:
        undo_stack.append(edited_image.copy())

# Function to undo the last change
def undo():
    global edited_image, undo_stack
    if undo_stack:
        edited_image = undo_stack.pop()
        display_image(edited_image)
    else:
        messagebox.showinfo("Info", "No more actions to undo.")

# Function to crop the image
def crop_image():
    global edited_image
    if edited_image:
        try:
            left = int(crop_left.get())
            top = int(crop_top.get())
            right = int(crop_right.get())
            bottom = int(crop_bottom.get())

            if right <= left or bottom <= top:
                messagebox.showerror("Error", "Right must be greater than left and bottom must be greater than top.")
                return

            save_state()
            edited_image = edited_image.crop((left, top, right, bottom))
            display_image(edited_image)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for cropping.")
    else:
        messagebox.showerror("Error", "No image loaded!")

# Function to resize the image
def resize_image():
    global edited_image
    if edited_image:
        try:
            width = int(resize_width.get())
            height = int(resize_height.get())
            save_state()
            edited_image = edited_image.resize((width, height))
            display_image(edited_image)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for resizing.")
    else:
        messagebox.showerror("Error", "No image loaded!")

# Function to adjust brightness
def adjust_brightness(value):
    global edited_image
    if edited_image:
        enhancer = ImageEnhance.Brightness(original_image)
        edited_image = enhancer.enhance(float(value))
        display_image(edited_image)

# Function to apply filters
def apply_filter(filter_type):
    global edited_image
    if edited_image:
        save_state()
        if filter_type == "grayscale":
            edited_image = edited_image.convert("L")
        elif filter_type == "blur":
            edited_image = edited_image.filter(ImageFilter.BLUR)
        elif filter_type == "edge":
            edited_image = edited_image.filter(ImageFilter.FIND_EDGES)
        display_image(edited_image)
    else:
        messagebox.showerror("Error", "No image loaded!")

# Function to compress the image
def compress_image():
    global edited_image
    if edited_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            save_state()
            edited_image.save(file_path, "JPEG", quality=30)  # Save with reduced quality
            messagebox.showinfo("Success", "Image compressed and saved successfully!")
    else:
        messagebox.showerror("Error", "No image loaded!")

# Function to convert image format
def convert_format():
    global edited_image
    if edited_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", "*.*")])
        if file_path:
            save_state()
            edited_image.save(file_path)  # Save in the selected format
            messagebox.showinfo("Success", "Image format converted and saved successfully!")
    else:
        messagebox.showerror("Error", "No image loaded!")

# Function to save the edited image
def save_image():
    if edited_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("JPEG files", "*.jpg"),
                                                            ("All files", "*.*")])
        if file_path:
            edited_image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
    else:
        messagebox.showerror("Error", "No image loaded!")

# Create the GUI
root = Tk()
root.title("Image Editor")

# Buttons and labels
Button(root, text="Open Image", command=open_image).grid(row=0, column=0, pady=10, padx=10)
Button(root, text="Save Image", command=save_image).grid(row=0, column=1, pady=10, padx=10)
Button(root, text="Undo", command=undo).grid(row=0, column=2, pady=10, padx=10)
Button(root, text="Compress Image", command=compress_image).grid(row=0, column=3, pady=10, padx=10)
Button(root, text="Convert Format", command=convert_format).grid(row=0, column=4, pady=10, padx=10)

# Cropping
Label(root, text="Crop (left, top, right, bottom):").grid(row=1, column=0, columnspan=4)
crop_left = Entry(root, width=5)
crop_left.grid(row=2, column=0, padx=5)
crop_top = Entry(root, width=5)
crop_top.grid(row=2, column=1, padx=5)
crop_right = Entry(root, width=5)
crop_right.grid(row=2, column=2, padx=5)
crop_bottom = Entry(root, width=5)
crop_bottom.grid(row=2, column=3, padx=5)
Button(root, text="Crop", command=crop_image).grid(row=2, column=4, padx=10)

# Resizing
Label(root, text="Resize (width x height):").grid(row=3, column=0, columnspan=3)
resize_width = Entry(root, width=5)
resize_width.grid(row=4, column=0, padx=5)
resize_height = Entry(root, width=5)
resize_height.grid(row=4, column=1, padx=5)
Button(root, text="Resize", command=resize_image).grid(row=4, column=2, padx=10)

# Brightness Adjustment
Label(root, text="Adjust Brightness:").grid(row=5, column=0, columnspan=2)
brightness_scale = Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=HORIZONTAL, command=adjust_brightness)
brightness_scale.set(1.0)
brightness_scale.grid(row=6, column=0, columnspan=2, pady=10)

# Filters
Button(root, text="Grayscale", command=lambda: apply_filter("grayscale")).grid(row=7, column=0, pady=10, padx=10)
Button(root, text="Blur", command=lambda: apply_filter("blur")).grid(row=7, column=1, pady=10, padx=10)
Button(root, text="Edge Enhance", command=lambda: apply_filter("edge")).grid(row=7, column=2, pady=10, padx=10)

# Image display
image_label = Label(root)
image_label.grid(row=8, column=0, columnspan=5, pady=20)

# Run the application
root.mainloop()