# WoW Ability Automation Script (BETA)

This Python script automates ability rotations in World of Warcraft (WoW) by leveraging visual cues provided by Hekili, a popular in-game ability rotation helper. The script captures screenshots of the recommended ability and automatically executes the corresponding action, optimizing gameplay efficiency.

## Disclaimer

This script is provided solely for educational and experimental purposes. It is crucial that this script be used responsibly and ethically within a controlled environment. The creator disclaims any liability for misuse of this software, and it should not be used in live game settings where it may contravene the game's terms of service.

I've tried to optimise the OCR recognition for a while and altough the image processing output is crystal clear, Pytesseract often messes up.
I recommend using another OCR scanner.

For debugging purposes, the processed images are stored into "screenshots".

## Key Features

- **Interactive Area Selection:** Users can define the screen area to monitor by clicking to form a rectangle. This flexibility allows the script to be adapted to different UI setups within WoW.
- **Automated Ability Execution:** Through real-time monitoring and image processing, the script detects the next recommended ability displayed by Hekili and simulates the corresponding keyboard input to execute the ability.
- **Continuous and Controlled Operation:** The script operates in a loop, continuously scanning for and executing abilities until it is manually halted, ensuring that it adapts dynamically to the game’s progression.
- **Advanced Image Processing:** Utilizes sophisticated image processing techniques to accurately recognize text within the game's graphical interface, even under varying screen conditions.
- **Responsive Key Simulation:** The script not only recognizes the recommended abilities but also simulates the necessary key presses instantly, allowing for seamless gameplay automation.

## System Requirements

- Python 3.x
- Required Python libraries: `tkinter`, `PIL`, `numpy`, `pytesseract`, `pyautogui`, `time`, `keyboard`, `random`, `cv2`

## Setup and Installation

1. **Python Installation:**
   - Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Library Installation:**
   - Open a command line interface and install the required libraries using pip:
     ```bash
     pip install pillow numpy pytesseract pyautogui keyboard opencv-python
     ```
     You will also need to have the pytesseract binaries.
     https://github.com/UB-Mannheim/tesseract/wiki

3. **Download the Script:**
   - Clone or download this repository to your local machine:
     ```bash
     git clone <repository-url>
     ```

4. **Prepare for Execution:**
   - Move into the script's directory:
     ```bash
     cd <repository-name>
     ```

5. **Launch the Script:**
   - Execute the script with Python to start the application:
     ```bash
     python <script-name>.py
     ```

## Detailed Usage Instructions

1. **Initialize the Application:**
   - Execute the script. A fullscreen, semi-transparent window will appear. This interface allows for precise area selection without obstructing the view of the game.

2. **Define the Monitoring Area:**
   - Click on two points on the screen to delineate the rectangle where the script should monitor for Hekili’s ability recommendations.

3. **Activate the Automation:**
   - Press the spacebar to begin continuous scanning of the selected area. The script will take screenshots, identify the recommended ability, and execute it automatically.

4. **Terminate the Application:**
   - Press 'esc' to stop the script and close the application. This allows for safe and controlled operation without affecting gameplay when not needed.

## Contributing to the Project

Your contributions are welcome! For bug fixes, enhancements, or documentation improvements, please refer to CONTRIBUTING.md for detailed guidelines on how to contribute effectively.

## Licensing

This project is released under the MIT License, which provides extensive flexibility for reuse within other projects or commercial purposes.
