import os
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import pytesseract
import pyautogui
import time
import keyboard
import random
import cv2

class ClickApp:
    def __init__(self, root):
        # Initialize the main window with semi-transparency and fullscreen attributes
        self.root = root
        self.root.title("Click to Form Rectangle and Recognize Text")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)

        # Create a canvas where clicks will be registered
        self.canvas = tk.Canvas(root, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.on_click)

        # Display instructions on the canvas
        self.label = tk.Label(root, text="Click twice anywhere to form a rectangle.",
                              anchor="center", font=('Helvetica', 14), bg='white')
        self.label.pack(pady=20)

        # Store coordinates and initialize the OCR reader
        self.coordinates = []
        
        # Control variable for continuous scanning
        self.running = False

        # Folder to save processed images
        self.image_folder = "screenshots"
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)
            
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        
        print("Application started. Ready to capture clicks.")

    def on_click(self, event):
        # Store click coordinates and handle the formation of a rectangle
        self.coordinates.append((event.x, event.y))
        print(f"Click registered at: {event.x}, {event.y}")
        if len(self.coordinates) == 2:
            print(f"Two clicks captured. Coordinates: {self.coordinates}")
            self.label.config(text=f"Rectangle formed at: {self.coordinates[0]} and {self.coordinates[1]}")
            self.root.after(500, self.start_continuous_scan)

    def start_continuous_scan(self):
        # Begin continuous scanning until a stop condition is met
        self.running = True
        self.root.withdraw()  # Hide the window
        print("Waiting for spacebar...")
        while self.running:
            if keyboard.is_pressed('esc'):
                print("Escape key pressed. Exiting...")
                self.running = False
                break
            elif keyboard.is_pressed('space'):
                start_time = time.time()
                self.process_text()
                sleep_time = random.uniform(0.05, 0.1)
                elapsed_time = time.time() - start_time
                print(f"Processing time: {elapsed_time:.3f} seconds. Sleeping for {sleep_time} seconds.")
                time.sleep(sleep_time)
        self.root.destroy()

    def process_text(self):
        # Capture the screen area defined by two clicks and process the text found in that area
        x1, y1, x2, y2 = self.coordinates[0][0], self.coordinates[0][1], self.coordinates[1][0], self.coordinates[1][1]
        image = ImageGrab.grab(bbox=(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
        image_np = np.array(image)
        image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        
        # Create masks for different gray levels
        mask_gray_94_95 = cv2.inRange(image_gray, 90, 100)
        mask_gray_254_255 = cv2.inRange(image_gray, 250, 255)
        mask_combined = cv2.bitwise_or(mask_gray_94_95, mask_gray_254_255)
        image_processed = cv2.bitwise_and(image_gray, image_gray, mask=mask_combined)
        
        # Extract the largest connected component
        _, image_thresh = cv2.threshold(image_processed, 90, 255, cv2.THRESH_BINARY)
        kernel = np.ones((1,1), np.uint8)
        image_morphed = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, kernel)
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(image_morphed, 4, cv2.CV_32S)
        largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
        largest_mask = labels == largest_label
        largest_component = np.zeros_like(image_gray)
        largest_component[largest_mask] = 255

        # Invert the colors
        final_image = cv2.bitwise_not(largest_component)
        
        # Save the processed image
        save_path = os.path.join(self.image_folder, f"processed_image_{time.time()}.png")
        cv2.imwrite(save_path, final_image)
        
        # Recognize text
        result = pytesseract.image_to_string(final_image, config='--psm 10 outputbase digits')
        print(f"Scanned text: {result}")
        self.simulate_key_presses(result)

    def simulate_key_presses(self, text):
        # Simulate key presses based on the recognized text
        for char in text:
            pyautogui.press(char)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickApp(root)
    root.mainloop()
