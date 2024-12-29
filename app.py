import cv2
import pandas as pd

# Function to read the CSV file and return a DataFrame
def load_csv(csv_path):
    try:
        index = ["color", "color_name", "hex", "R", "G", "B"]
        return pd.read_csv(csv_path, names=index, header=None)
    except FileNotFoundError:
        print(f"Error: The file at {csv_path} was not found.")
        exit()
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        exit()

# Function to calculate the minimum distance from all colors and get the most matching color
def get_color_name(R, G, B, csv):
    minimum = float('inf')
    cname = "Unknown"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Function to handle image path input
def detect_color_from_image(img_path, csv):
    img = cv2.imread(img_path)
    if img is None:
        print("Could not open or find the image. Please check the file path.")
        return

    clicked = False
    r = g = b = x_pos = y_pos = 0

    def draw_function(event, x, y, flags, param):
        nonlocal r, g, b, x_pos, y_pos, clicked
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicked = True
            x_pos = x
            y_pos = y
            b, g, r = img[y, x]
            b = int(b)
            g = int(g)
            r = int(r)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_function)

    while True:
        cv2.imshow("image", img)
        if clicked:
            cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
            text = get_color_name(r, g, b, csv) + f' R={r} G={g} B={b}'
            cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            if r + g + b >= 600:
                cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            clicked = False
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

# Function to handle webcam input
def detect_color_from_webcam(csv):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture video from webcam. Exiting...")
            break
        height, width, _ = frame.shape
        cx = int(width / 2)
        cy = int(height / 2)
        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
        color_name = get_color_name(r, g, b, csv)
        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 60), (255, 255, 255), -1)
        text = f"{color_name} R={r} G={g} B={b}"
        cv2.putText(frame, text, (cx - 200, 50), 2, 0.8, (b, g, r), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(frame, text, (cx - 200, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
        cv2.putText(frame, "Press ESC to exit", (10, frame.shape[0] - 10), 1, 1, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    csv_path = r'D:\ML projects\Color detection\colors.csv'
    csv = load_csv(csv_path)

    choice = input("How do you want to detect the color?\n1. Providing Image\n2. Using Webcam\nEnter your choice (1 or 2): ").strip()
    if choice == '1':
        img_path = input("Please enter the path to the image file: ").strip()
        detect_color_from_image(img_path, csv)
    elif choice == '2':
        detect_color_from_webcam(csv)
    else:
        print("Invalid choice. Please restart the program and enter a valid option.")

if __name__ == "__main__":
    main()
