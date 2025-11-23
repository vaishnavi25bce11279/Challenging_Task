# Scholar Sphere - Python FAQ Chatbot
## Project Overview
Scholar Sphere is a command-line based FAQ chatbot application designed to assist students and developers with Python programming queries, setup procedures, and troubleshooting common issues. The application provides an interactive interface for browsing categorized questions and searching for specific topics related to Python development, environment setup, version control, and deployment strategies.
The chatbot implements a modular architecture with clear separation of concerns, demonstrating professional software design principles including data abstraction, business logic separation, and presentation layer independence. This project serves as both a practical utility for Python learners and an exemplar of clean, maintainable code structure.

## Features

### Core Functionality

1. **Category-Based Navigation**
   - Browse through 7 comprehensive FAQ categories
   - Hierarchical navigation system with intuitive menu structure
   - Easy access to related questions within each category

2. **Advanced Search Capability**
   - Keyword-based search across all FAQ entries
   - Case-insensitive search algorithm
   - Results display with category context

3. **Comprehensive FAQ Database**
   - 30+ carefully curated questions and detailed answers
   - Covers essential Python development topics
   - Step-by-step instructions for common tasks

4. **User-Friendly Interface**
   - Clear console-based menu system
   - Formatted output with visual separators
   - Intuitive navigation with numbered options
   - Error handling with informative messages

### FAQ Categories

- ** Software Installation & Setup** - Python, VS Code, Jupyter Notebook installation guides
- ** File & Folder Setup** - Project organization and folder structure best practices
- ** Virtual Environment & Packages** - Virtual environment management and package installation
- ** Git & GitHub Setup** - Version control system configuration and usage
- ** Common Errors & Troubleshooting** - Solutions to frequent development issues
- ** Development Tools** - IDE comparisons and development environment optimization
- ** Project Deployment** - Application deployment and distribution methods

## Technologies and Tools Used

### Programming Language
- **Python 3.14.0** - Core programming language for application logic

### Standard Libraries
- **os** - Operating system interface for screen clearing functionality

### Development Methodology
- **Object-Oriented Programming (OOP)** - Class-based architecture
- **Modular Design Pattern** - Separation of concerns across six modules
- **Data Encapsulation** - Structured data organization using Python dictionaries

### Architecture Components
- **Data Layer** - FAQ database storage (faq_data.py)
- **Configuration Layer** - Application settings and constants (config.py)
- **Business Logic Layer** - FAQ operations and search functionality (chat_manager.py)
- **Presentation Layer** - User interface and display management (ui_components.py)
- **Application Layer** - Main controller and flow management (chatbot_app.py)
- **Entry Point** - Application initialization (final.py)

## Project Structure

```
Challenging_Task/
├── faq_data.py          # FAQ database module
├── config.py            # Configuration constants
├── chat_manager.py      # Business logic module
├── ui_components.py     # Display management module
├── chatbot_app.py       # Main application controller
├── final.py             # Application entry point
└── README.md            # Project documentation
```

## Installation and Setup

### Prerequisites

Ensure the following requirements are met before installation:

- Python 3.14.0
- Command-line interface (Terminal on macOS/Linux, Command Prompt or PowerShell on Windows)
- No additional third-party packages required

### Installation Steps

1. **Download Project Files**
   
   Download all six Python modules to a single directory:
   - faq_data.py
   - config.py
   - chat_manager.py
   - ui_components.py
   - chatbot_app.py
   - final.py

2. **Verify File Integrity**
   
   Ensure all files are present in the same directory with correct naming conventions.

3. **Verify Python Installation**
   
   Open terminal/command prompt and execute:
   ```bash
   python --version
   ```
   Confirm Python 3.14.0

### Running the Application

1. **Navigate to Project Directory**
   ```bash
   cd path/to/Challenging_Task
   ```

2. **Execute Application**
   ```bash
   python final.py
   ```

3. **Application Launch**
   
   The application will clear the screen and display the welcome message followed by the main menu.

## Usage Instructions

### Main Menu Options

Upon launching the application, users are presented with three primary options:

**Option 1: Explore the Unknown**
- Browse FAQ categories
- Select a category to view its questions
- Choose a question to display its answer
- Navigate back using option 0

**Option 2: Sherlock Search Mode**
- Enter a keyword to search across all questions
- View matching results with category context
- Select a result to display the full answer
- Return to main menu using option 0

**Option 3: Logging Out**
- Exit the application gracefully

### Navigation Flow

1. **Browsing Categories**
   - Select option 1 from main menu
   - Enter category number (1-7)
   - View questions within selected category
   - Enter question number to view answer
   - Press Enter to return to question list
   - Enter 0 to return to category list

2. **Searching Questions**
   - Select option 2 from main menu
   - Enter search keyword
   - Review search results
   - Enter result number to view answer
   - Enter 0 to return to main menu

## Testing Instructions

### Functional Testing

#### Test Case 1: Application Launch
**Objective:** Verify application starts correctly

**Steps:**
1. Execute `python final.py`
2. Verify welcome message displays
3. Confirm main menu appears with three options

**Expected Result:** Application launches without errors and displays formatted menu

---

#### Test Case 2: Category Navigation
**Objective:** Test category browsing functionality

**Steps:**
1. From main menu, select option 1
2. Verify category list displays (7 categories)
3. Select category number 1
4. Verify questions display for selected category
5. Enter 0 to return to category list
6. Enter 0 again to return to main menu

**Expected Result:** Navigation works smoothly without errors

---

#### Test Case 3: Question Display
**Objective:** Verify question and answer display

**Steps:**
1. Navigate to any category
2. Select a valid question number
3. Verify answer displays with proper formatting
4. Press Enter to continue

**Expected Result:** Question and answer display correctly with separators

---

#### Test Case 4: Search Functionality
**Objective:** Test keyword search feature

**Steps:**
1. From main menu, select option 2
2. Enter keyword "python"
3. Verify search results display
4. Select a result number
5. Verify answer displays correctly

**Expected Result:** Search returns relevant results and displays answers

---

#### Test Case 5: Invalid Input Handling
**Objective:** Test error handling mechanisms

**Steps:**
1. From main menu, enter invalid option (e.g., 5)
2. Verify error message displays
3. From category list, enter invalid number (e.g., 99)
4. Verify error message displays
5. Enter non-numeric input
6. Verify appropriate error message displays

**Expected Result:** Application handles invalid inputs gracefully with informative error messages

---

#### Test Case 6: Search with No Results
**Objective:** Test search behavior with no matches

**Steps:**
1. Select search option
2. Enter keyword with no matches (e.g., "zzzzz")
3. Verify "no results" message displays

**Expected Result:** Application informs user no results were found

---

#### Test Case 7: Exit Functionality
**Objective:** Verify proper application termination

**Steps:**
1. From main menu, select option 3
2. Verify exit message displays
3. Confirm application terminates

**Expected Result:** Application exits cleanly with farewell message
### Integration Testing

**Test Module Interactions:**
1. Verify faq_data.py successfully loads into chat_manager.py
2. Confirm config.py constants are accessible throughout application
3. Test ui_components.py display methods with various inputs
4. Verify chatbot_app.py correctly orchestrates all modules

### Performance Testing

**Response Time:**
- Verify menu displays instantly
- Confirm search results appear within 1 second
- Test with maximum FAQ entries

**Memory Usage:**
- Monitor application memory footprint (should remain under 50MB)
- Verify no memory leaks during extended usage

## Troubleshooting

### Common Issues and Solutions

**Issue:** ModuleNotFoundError when running final.py

**Solution:** Ensure all six Python files are in the same directory

---

**Issue:** NameError: 'ChatManager' is not defined

**Solution:** Add imports at the top of chatbot_app.py:
```python
from chat_manager import ChatManager
from ui_components import DisplayManager
```

---

**Issue:** NameError: 'ChatbotApp' is not defined

**Solution:** Add imports at the top of final.py:
```python
from faq_data import FAQ_DB
from config import Config
from chatbot_app import ChatbotApp
```

---

**Issue:** Screen does not clear properly

**Solution:** This is OS-dependent behavior and does not affect functionality
## Limitations

- Only addresses questions present in the FAQ database (no web search/NLP yet).
- No persistent chat history or user context—stateless per session.
- Console-only; no web or GUI interface.
- Matches strictly by supplied keywords, not full sentence understanding.

## Future Enhancements

Potential improvements for future versions:

1. JSON-based FAQ storage for easier content updates
2. Colored terminal output for improved readability
3. Export functionality to save answers to text files
4. User feedback mechanism for FAQ improvement
5. Multi-language support
6. Web-based GUI interface option
7. FAQ contribution system for community input

## Project Metadata

| Attribute | Details |
|-----------|---------|
| Project Type | Educational Python Application |
| Architecture | Modular Command-Line Interface |
| Code Complexity | Beginner to Intermediate |
| Lines of Code | Approximately 400 lines |
| Number of Modules | 6 Python files |
| Documentation | Complete inline and external documentation |


## Version History

**Version 1.0.0** (Current)
- Initial release
- 7 FAQ categories
- 30+ questions and answers
- Browse and search functionality
- Modular architecture implementation

---

## Author
Vaishnavi Asati
BTech Computer Science(Core)
VIT Bhopal