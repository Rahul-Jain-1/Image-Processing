import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

def rotate_image(image, degrees):
    return image.rotate(degrees, expand=True)

def crop_image(image, box):
    return image.crop(box)

def grayscale_image(image):
    return image.convert('L')

def blur_image(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def sharpen_image(image, factor):
    return image.filter(ImageFilter.UnsharpMask(radius=2, percent=factor))

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def main():
    st.sidebar.title("Image Operations")
    uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    operation = st.sidebar.selectbox("Select Operation", ["None", "Rotate", "Crop", "Convert to Grayscale", "Blur", "Sharpen", "Brightness Adjustment"])
    rotation_degrees = 0
    crop_top, crop_bottom, crop_left, crop_right = 0, 0, 0, 0
    blur_radius, sharpen_factor = 0, 0
    brightness_factor = 1.0
    save_button = st.sidebar.button("Save Image")

    if operation == "Rotate":
        rotation_degrees = st.sidebar.slider("Rotation Degrees", -180, 180, 0)
    elif operation == "Crop":
        crop_top = st.sidebar.slider("Crop Top", 0, 100, 0)
        crop_bottom = st.sidebar.slider("Crop Bottom", 0, 100, 0)
        crop_left = st.sidebar.slider("Crop Left", 0, 100, 0)
        crop_right = st.sidebar.slider("Crop Right", 0, 100, 0)
    elif operation == "Blur":
        blur_radius = st.sidebar.slider("Blur Radius", 0, 10, 0)
    elif operation == "Sharpen":
        sharpen_factor = st.sidebar.slider("Sharpen Factor", 0, 300, 150)
    elif operation == "Brightness Adjustment":
        brightness_factor = st.sidebar.slider("Brightness Adjustment", 0.0, 2.0, 1.0)

    if uploaded_image is not None:
        img = Image.open(uploaded_image)

        # Apply operations based on user input
        if operation == "Rotate":
            img = rotate_image(img, rotation_degrees)
        elif operation == "Crop":
            width, height = img.size
            box = (int(crop_left / 100 * width), int(crop_top / 100 * height), 
                   int((100 - crop_right) / 100 * width), int((100 - crop_bottom) / 100 * height))
            img = crop_image(img, box)
        elif operation == "Convert to Grayscale":
            img = grayscale_image(img)
        elif operation == "Blur":
            img = blur_image(img, blur_radius)
        elif operation == "Sharpen":
            img = sharpen_image(img, sharpen_factor)
        elif operation == "Brightness Adjustment":
            img = adjust_brightness(img, brightness_factor)

        # Display the processed image
        st.image(img, caption='Processed Image', use_column_width=True)

        # Save the image if save button clicked
        if save_button:
            img.save("processed_image.jpg", format="JPEG")
            st.sidebar.success("Image saved successfully!")

if __name__ == '__main__':
    main()
