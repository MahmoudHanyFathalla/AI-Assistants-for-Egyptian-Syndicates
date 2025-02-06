# AI Assistants for Egyptian Syndicates

## Project Overview
This project involves developing AI assistants for various professional syndicates in Egypt, including the Engineering Syndicate, Physical Therapy Syndicate, Teachers Syndicate, and more. The assistants leverage OpenAI's API to provide information on healthcare programs, regulations, and other relevant topics for each syndicate.

## Features
- AI-powered assistants tailored for different syndicates.
- Web and GUI-based chatbot interfaces.
- File search capabilities for uploaded documents.
- Data processing utilities for structured information extraction.
- FastAPI server for web interaction.
- Specialized assistants for more targeted queries.

---

## Project Structure

### **AlagTabe3yNekaba/** (Physical Therapy Syndicate Assistant)
- `CreatingAssistant.py`: Creates an assistant for the Physical Therapy Syndicate and uploads necessary files.
- `UsingAssistant.py`: Interacts with the created assistant, allowing users to ask questions and receive responses.

### **EngineeringNekaba/** (Engineering Syndicate Assistant)
- `CreatingAssistant.py`: Creates an assistant for the Engineering Syndicate.
- `UsingAssistant.py`: Allows users to interact with the Engineering Syndicate assistant.

### **FirstTry/** (Initial Experiments)
- `FikeSearch.py`: Creates an assistant and uploads a PDF file to enable file search.
- `FirstAssestant.py`: Allows interaction with the first version of the assistant.

### **FullChatBot/** (Complete Chatbot System)
- `all.py`: Implements a FastAPI web server for interaction with the AI assistant.
- `AllAssistant.py`: Handles user interaction with the AI assistant.
- `AllinOne.py`: Creates an assistant and uploads multiple PDF files for document search.
- `app.py`: Provides a Tkinter-based GUI for interacting with the assistant.
  
  **Subdirectories:**
  - **Approch1/**: Contains scripts for specialized assistants.
    - `SpishializedAssestant.py`: Creates a specialized assistant.
    - `spishializedAssUseg.py`: Interacts with the specialized assistant.
  - **static/**: Stores static files for the web interface.
    - `styles.css`: Defines the web interface styling.
  - **templates/**: Contains HTML templates.
    - `index.html`: Main webpage template for user interaction.

### **HelpfullScripts/** (Utility Scripts for Data Processing)
- `dataProssising.py`: Converts Excel files into CSV, JSON, and PDF formats.
- `FromExeclToWord.py`: Converts Excel files into Word documents.
- **input/**: Stores input data files.
  - `qfa.xlsx`: An example Excel file for processing.

### **IntroduactionNekaba/** (Introduction to the Engineering Syndicate Assistant)
- `CreatingAssistant.py`: Sets up the Engineering Syndicate AI assistant.
- `UsingAssistant.py`: Allows users to interact with the assistant.

### **Mor4edenNekaba/** (Guides Syndicate Assistant)
- `CreatingAssistant.py`: Sets up the Guides Syndicate AI assistant.
- `UsingAssistant.py`: Provides an interface for user interaction.

### **TeachingNekaba/** (Teachers Syndicate Assistant)
- `CreatingAssistant.py`: Creates an AI assistant for the Teachers Syndicate.
- `UsingAssistant.py`: Allows interaction with the Teachers Syndicate assistant.

### **README.md**
- This file provides an overview of the project.

---

## How to Use
1. **Creating an Assistant:** Navigate to the relevant syndicate folder and run `CreatingAssistant.py`.
2. **Interacting with an Assistant:** Use `UsingAssistant.py` to ask questions and receive responses.
3. **Web Interface:** Run `all.py` in the `FullChatBot` directory to start a FastAPI server.
4. **GUI Interface:** Run `app.py` to launch the Tkinter-based interface.
5. **Specialized Assistants:** Use scripts in `Approch1/` for domain-specific queries.
6. **Data Processing:** Utilize scripts in `HelpfullScripts/` for data conversion tasks.

---

## Requirements
- Python 3.8+
- OpenAI API Key
- Dependencies: Install via `pip install -r requirements.txt`
- FastAPI for web interaction
- Tkinter for GUI support

---

## Future Enhancements
- Expanding support for additional syndicates.
- Enhancing NLP capabilities for more accurate responses.
- Implementing voice-based interaction.
- Adding multilingual support for better accessibility.

---

## Contributors
- **Mahmoud Hany** - Lead AI & Software Developer

For contributions and issues, please contact [Mahmoud Hany](https://www.linkedin.com/in/mahmoud-hany-fathalla-6b1690219/).

---

## License
This project is licensed under the MIT License.

