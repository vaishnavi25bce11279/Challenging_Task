FAQ_DB = {
    "💻 Software Installation & Setup": {
        "How do I install Python on Windows/Mac/Linux?": 
            "Windows: Download from python.org → Run installer → Check 'Add to PATH' → Install.\nMac: Use Homebrew 'brew install python3' or download from python.org.\nLinux: Usually pre-installed. Use 'sudo apt install python3' (Ubuntu/Debian) or 'sudo yum install python3' (RedHat/Fedora).",
        
        "How to install and set up Visual Studio Code for Python?": 
            "1. Download VS Code from code.visualstudio.com\n2. Install and open VS Code\n3. Click Extensions (Ctrl+Shift+X)\n4. Search 'Python' → Install Microsoft's Python extension\n5. Open a .py file → Select Python interpreter (bottom-left)\n6. Ready to code!",
        
        "How do I install Jupyter Notebook?": 
            "Method 1: pip install jupyter → Run with 'jupyter notebook'\nMethod 2: Install Anaconda (includes Jupyter)\nMethod 3: Use VS Code with Jupyter extension\nLaunch creates local server at http://localhost:8888",
        
        "What is the difference between Anaconda and Python?": 
            "Python: Core programming language only.\nAnaconda: Python + 250+ pre-installed packages (NumPy, Pandas, etc.) + Conda package manager + Jupyter + Spyder IDE. Best for data science. Larger download (~500MB vs 25MB).",
        
        "Why do we need a virtual environment (venv)?": 
            "Isolates project dependencies. Prevents version conflicts between projects. Each project has its own packages. Easy to share exact requirements. Keeps system Python clean."
    },
    
    "🗂️ File & Folder Setup": {
        "Where should I create my project folder on my computer?": 
            "Windows: C:\\Users\\YourName\\Projects or D:\\Projects\nMac/Linux: /home/username/Projects or ~/Projects\nAvoid: Desktop, Downloads, System folders. Use meaningful names without spaces (use underscores).",
        
        "Can I store my Python projects in OneDrive/Google Drive?": 
            "Yes, but NOT recommended for active development. Cloud sync can conflict with Git and virtual environments. Best practice: Work locally → Push to GitHub for backup. Use cloud only for final backups.",
        
        "How do I set a default Python folder in VS Code?": 
            "File → Open Folder → Select your project folder. VS Code remembers last workspace. To set permanent: Settings → Search 'default folder' → Set 'files.defaultLocation'. Use 'workspaces' feature for multiple projects.",
        
        "What is the correct folder structure for a Python project?": 
            "my_project/\n├── venv/ (virtual environment)\n├── src/ or app/ (source code)\n├── tests/ (test files)\n├── docs/ (documentation)\n├── requirements.txt\n├── README.md\n├── .gitignore\n└── main.py"
    },
    
    "⚙️ Virtual Environment & Packages": {
        "What is a virtual environment in Python?": 
            "An isolated Python environment for each project. Contains its own Python interpreter and packages. Prevents conflicts between different project dependencies. Created per-project basis.",
        
        "How do I create and activate a virtual environment?": 
            "Create: python -m venv myenv\nActivate:\n  Windows: myenv\\Scripts\\activate\n  Mac/Linux: source myenv/bin/activate\nYou'll see (myenv) in terminal.\nDeactivate: type 'deactivate'",
        
        "How do I install packages using pip?": 
            "Single package: pip install package_name\nSpecific version: pip install package_name==1.2.3\nMultiple: pip install pkg1 pkg2 pkg3\nFrom file: pip install -r requirements.txt\nUpgrade: pip install --upgrade package_name\nList installed: pip list",
        
        "What is requirements.txt? Why is it used?": 
            "A text file listing all project dependencies with versions. Makes project reproducible. Others can install exact same packages.\nCreate: pip freeze > requirements.txt\nInstall from it: pip install -r requirements.txt\nEssential for sharing projects and deployment.",
        
        "Difference between pip install and conda install?": 
            "pip: Python-only package manager. Installs from PyPI. Works everywhere.\nconda: Manages Python AND non-Python packages (C libraries, R, etc.). Installs from Anaconda repository. Better dependency resolution. Only with Anaconda/Miniconda."
    },
    
    "🐙 Git & GitHub Setup": {
        "What is Git and why do we use it?": 
            "Git: Version control system tracking code changes. Enables collaboration, maintains history, allows rollback, manages branches.\nGitHub: Cloud platform hosting Git repositories. Backup, portfolio, collaboration, open source contribution.",
        
        "How do I install Git on my system?": 
            "Windows: Download from git-scm.com → Install with default settings\nMac: Install Xcode Command Line Tools or 'brew install git'\nLinux: 'sudo apt install git' (Ubuntu) or 'sudo yum install git' (RedHat)\nVerify: git --version",
        
        "How to connect VS Code to GitHub?": 
            "1. Install Git first\n2. In VS Code: Sign in to GitHub (Account icon)\n3. Initialize repo: Source Control → Initialize Repository\n4. Stage → Commit → Publish to GitHub\n5. Or clone existing: Command Palette → Git: Clone",
        
        "Can people see earlier versions of my code on GitHub?": 
            "Yes! All commit history is visible. Click 'Commits' to see all changes. Can view any previous version. Use .gitignore to exclude sensitive files (passwords, API keys). Make repos private for confidential projects.",
        
        "How do I push and update code on GitHub?": 
            "1. git add . (stage changes)\n2. git commit -m 'your message' (commit)\n3. git push (upload to GitHub)\nIn VS Code: Stage → Commit → Sync/Push button. Pull before pushing to avoid conflicts."
    },
    
    "🛠️ Common Errors & Troubleshooting": {
        "What is 'ModuleNotFoundError' and how to fix it?": 
            "Error: Python can't find the module.\nFixes:\n1. Install package: pip install module_name\n2. Check virtual environment is activated\n3. Verify correct Python interpreter in VS Code\n4. Reinstall: pip uninstall module_name → pip install module_name",
        
        "Why does my program show 'Permission Denied' error?": 
            "Causes: File in use by another program, insufficient permissions, file is read-only, antivirus blocking.\nFixes:\n1. Close programs using the file\n2. Run as administrator\n3. Check file properties → Uncheck read-only\n4. Change file permissions (chmod on Linux/Mac)",
        
        "What to do when VS Code doesn't detect Python?": 
            "1. Install Python extension from marketplace\n2. Click Python version (bottom-right) → Select interpreter\n3. Command Palette (Ctrl+Shift+P) → 'Python: Select Interpreter'\n4. Verify Python installed: python --version in terminal\n5. Reload VS Code window",
        
        "How to solve environment conflicts in Python?": 
            "1. Use separate virtual environments per project\n2. Delete venv folder → Recreate fresh: python -m venv venv\n3. Check requirements.txt for conflicting versions\n4. Use conda environments for complex dependencies\n5. Update packages: pip install --upgrade package_name"
    },
    
    "📊 Development Tools": {
        "Which IDE is best for Python (VS Code, PyCharm, Spyder)?": 
            "VS Code: Lightweight, free, versatile, great extensions. Best for beginners & web dev.\nPyCharm: Feature-rich, intelligent, built for Python. Pro version paid. Best for large projects.\nSpyder: Scientific computing focused, simple UI. Comes with Anaconda. Best for data science beginners.\nRecommendation: Start with VS Code.",
        
        "How do I enable Python extensions in VS Code?": 
            "1. Open Extensions (Ctrl+Shift+X)\n2. Search and install:\n   • Python (Microsoft) - Essential\n   • Pylance - IntelliSense\n   • Python Indent - Auto-indentation\n   • autoDocstring - Documentation\n   • GitLens - Git enhancement\n3. Reload VS Code after installation",
        
        "What is a code interpreter?": 
            "Translates Python code to machine language. Two types:\nCPython: Standard Python interpreter (most common)\nIPython: Interactive Python with enhanced features\nJupyter uses IPython kernel. Interpreter executes code line-by-line or as script.",
        
        "What are linters and formatters in VS Code?": 
            "Linters: Check code for errors/style issues (Pylint, Flake8). Show warnings/errors in real-time.\nFormatters: Auto-format code to standards (Black, autopep8). Makes code consistent and readable.\nEnable in VS Code settings: 'Python › Linting' and 'Python › Formatting'"
    },
    
    "🤖 Project Deployment (Basic)": {
        "How do I convert my Python script into an EXE file?": 
            "Use PyInstaller:\n1. pip install pyinstaller\n2. pyinstaller --onefile script.py\n3. Find .exe in 'dist' folder\nOther tools: cx_Freeze, py2exe, Auto-py-to-exe (GUI version).\nNote: Creates large files, platform-specific (Windows .exe won't work on Mac).",
        
        "Can I run Python programs on mobile?": 
            "Yes, but limited:\nAndroid: Pydroid 3, QPython, Termux apps\niOS: Pythonista, Carnets (Jupyter)\nBetter: Create web app (Flask/Django) → Access via mobile browser. Or build native mobile app using frameworks like Kivy or BeeWare.",
        
        "How do I host a web-based Python project?": 
            "Free options:\n• Heroku: Flask/Django apps (needs Procfile)\n• PythonAnywhere: Direct Python hosting\n• Render: Modern alternative to Heroku\n• Vercel/Netlify: For frontend with Python backend\n• Streamlit Cloud: For data apps\nSteps: Push to GitHub → Connect to platform → Deploy"
    }
}