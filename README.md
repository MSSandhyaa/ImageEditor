# ImageEditor

This code implements a simple image editor using `tkinter` for the graphical user interface (GUI) and `Pillow` (PIL) for image manipulation. The application allows users to perform various image editing operations such as cropping, resizing, adjusting brightness, applying filters, and saving the image in different formats.

The editor starts by providing a button to open an image from the file system. Once the image is loaded, it is displayed in a resizable preview. The user can apply a series of modifications to the image, such as cropping it based on user-defined coordinates, resizing it to specified dimensions, or adjusting its brightness using a slider. Users can also apply filters like grayscale, blur, and edge enhancement.

Undo functionality is implemented, allowing users to revert to the previous state of the image by clicking the undo button. The image can be saved in different formats, including JPEG and PNG, and users can compress the image to reduce its size by adjusting the quality.

The program supports an easy-to-use interface where each editing function has its corresponding input field or button. An image is displayed dynamically as changes are made, providing immediate feedback to the user. The image is stored in a global variable, allowing for seamless modifications and undo operations.

The design of this image editor is aimed at providing basic editing capabilities while keeping the interface simple and user-friendly. Through the use of `Pillow` for image manipulation and `tkinter` for the GUI, this project demonstrates how Python can be leveraged to create a  image editor with essential features.
