
## Color Detection System
This project is a Python-based color detection application that identifies the name of a color based on the RGB values of a pixel. It supports two modes:

- Image Input: Detect colors by providing an image file.
- Webcam Input: Detect colors using live video feed from a webcam.


## Features
- Reads a CSV file containing color data and their respective RGB values.

- Matches RGB values from the input source (image or webcam) to the nearest color in the dataset.

- Displays the detected color name and RGB values on the screen.

- Supports double-click detection for images and real-time detection using the webcam.




## Requirements
The following Python libraries are required to run the application:

- cv2 (OpenCV): For image and webcam processing.

- pandas: For handling the CSV file containing color data.

### CSV File
A CSV file containing color names, hex values, and RGB values is necessary. This file should follow the structure:
```bash
  color,color_name,hex,R,G,B
```
Example Row:
```bash
  Red,Red,#FF0000,255,0,0
```

## Usage
### Step 1: Setup
Ensure that Python and the required libraries (opencv-python and pandas) are installed. To install the libraries, use the following command:
```bash
 pip install opencv-python pandas
```


### Step 2: Provide the CSV File
Save your color data in a CSV file (e.g., colors.csv). Update the file path in the code:

```bash
  csv_path = r'D:\ML projects\Color detection\colors.csv'
```
### Step 3: Run the Application
Execute the script using Python:
```bash
  python app.py
```

### Step 4: Select a Mode
Upon running the script, you will be prompted to select a mode:

- Image Input: Enter the path of the image file.

- Webcam Input: Use the live feed from your webcam.

## How it Works 
### Image Input Mode

- Double-click on any point in the image to detect the color at that location.

- The detected color name and RGB values will appear as a text overlay.

- Press ESC to close the image window.

### Webcam Input Mode

- The program captures live video from your webcam.

- The center pixel of the video feed is analyzed for color detection.

- Detected color information is displayed in a rectangle overlay at the top of the feed.

- Press ESC to exit the webcam mode.

## Known Issues

- Large Images: Processing large images may result in slow performance.

- Lighting Variations: Webcam detection accuracy may vary depending on lighting conditions.

### License

This project is licensed under the MIT License.

