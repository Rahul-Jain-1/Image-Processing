# Image Processing App

This is a Streamlit application for performing various image processing operations using the Python Imaging Library (PIL). Users can upload an image and apply operations such as rotation, cropping, converting to grayscale, blurring, sharpening, and brightness adjustment.

You can use the application online at this [link](https://operations-image-1.streamlit.app/).

## Features

- **Rotate**: Rotate the image by a specified number of degrees.
- **Crop**: Crop the image by specifying the top, bottom, left, and right crop percentages.
- **Convert to Grayscale**: Convert the image to grayscale.
- **Blur**: Apply a Gaussian blur to the image with a specified radius.
- **Sharpen**: Sharpen the image with a specified factor.
- **Brightness Adjustment**: Adjust the brightness of the image with a specified factor.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/image-processing-app.git
   cd image-processing-app
   
2. Install the required packages:
  ```sh
  pip install -r requirements.txt
  ```

## Usage 
1. Run the Streamlit app:
  ```sh
    streamlit run app.py
  ```
2. Open your web browser and go to http://localhost:8501.
3. Use the sidebar to upload an image and select the desired operation.
4. Adjust the parameters for the selected operation using the provided sliders.
5. The processed image will be displayed in the main window.
6. Click the "Save Image" button to save the processed image as processed_image.jpg. 
