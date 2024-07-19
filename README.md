# WoW Ability Automation Script (BETA)

This Python script automates the process of using abilities in World of Warcraft by capturing screenshots of recommended actions from the Hekili add-on and executing them automatically.

## Disclaimer

This script is intended for educational and testing purposes only. Users are advised to operate this script within a controlled testing environment. The author is not responsible for any misuse or violations of game policies that may result from using this script.

I've tried to optimise the OCR recognition for a while and altough the image processing output is crystal clear, Pytesseract often messes up.
I recommend using another OCR scanner.

For debugging purposes, the processed images are stored into "screenshots".

## Images

![image](https://github.com/user-attachments/assets/9aa4d798-335f-4f86-9cbf-d0519d867d68)
![image](https://github.com/user-attachments/assets/6e173ddb-1a93-40a7-a888-278d2e501360)


## Features

- **Selectable Area for Monitoring:** Users can click to select a rectangle on their screen where the script will monitor for ability recommendations from Hekili.
- **Automated Execution of Abilities:** The script processes images to recognize text and automatically simulates the corresponding keyboard inputs.
- **Continuous Operation:** The script will continue to run until it is manually stopped by the user.
- **Image Processing for Text Recognition:** The script uses image processing techniques to identify text accurately within the selected screen area.

## System Requirements

- Python 3.x
- Required Python libraries: `tkinter`, `PIL`, `numpy`, `pytesseract`, `pyautogui`, `time`, `keyboard`, `random`, `cv2`
- Required Tesseract binaries: https://github.com/UB-Mannheim/tesseract/wiki

## Usage Instructions

1. **Launch the Application:**
   - Execute the script from your command line. The application will display in fullscreen with a semi-transparent background.

2. **Define the Monitoring Area:**
   - Click twice on the screen to define the rectangle area for the ability recommendation display.

3. **Start Monitoring:**
   - Press the spacebar to initiate continuous scanning. The script will monitor the defined area, process detected abilities, and execute the corresponding keyboard commands.

4. **Terminate the Script:**
   - Press 'esc' at any time to stop monitoring and close the application.
