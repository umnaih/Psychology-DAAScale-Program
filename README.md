# DASS Scale Program

This project is designed to convert the scientific psychology study "Depression, Anxiety, and Stress Scale" (DASS) into a Python program. The program utilizes Python and a GUI built with the Tkinter toolkit to assess users' depression, anxiety, and stress levels based on their responses to twenty-one questions.

## Project Components
1. **Flow Chart for DASS Program**
   
2. **UML Diagram for the Code**
   
3. **Implementation**
   
    - **Main Class**: Initializes the application and handles the navigation between different pages.
    
    - **Welcome Class**: Represents the welcome page where users start the assessment.
    
    - **FirstPage Class**: Displays the first set of questions (questions 1 to 7) and records user responses.
    
    - **SecondPage Class**: Displays the second set of questions (questions 8 to 14) and records user responses.
    
    - **ThirdPage Class**: Displays the third set of questions (questions 15 to 21) and records user responses.
    
    - **Results Class**: Displays the calculated results based on user responses.
    
    - **answers.py**: Contains three arrays (stressArray, depressionArray, anxietyArray) to store user responses and a function to calculate their sum.
    
    - **constants.py**: Contains a dictionary with options for answer choices used in the Radio buttons.
    
## How the Program Works
- The program starts with the **Main Class**, which initializes the application and manages the navigation between frames.

- Users begin with the **Welcome Class**, where they are introduced to the assessment and can start the questionnaire.

- The questionnaire is divided into three sections, each represented by a different page: **FirstPage**, **SecondPage**, and **ThirdPage**. Users answer questions on each page.

- The user's responses are stored in the appropriate arrays (stressArray, depressionArray, anxietyArray) in the **answers.py** file.

- The program checks for empty responses and prompts users to answer all questions.

- After all questions are answered, the **Results Class** displays the calculated depression, anxiety, and stress levels.

## Running the Program
- To run the program, execute the `Main.py` file.

## Project Structure
```
- Main.py
- answers.py
- constants.py
- FlowChart.png
- UMLDiagram.png
- Implementation/
    - Main.py
    - Welcome.py
    - FirstPage.py
    - SecondPage.py
    - ThirdPage.py
    - Results.py
```

For detailed information on each component, please refer to the respective files and diagrams provided.

Feel free to explore, use, and contribute to this project!
