# Day 23: Setting Up Virtual Environments in Python

# A virtual environment creates an isolated workspace for each project.
# This prevents dependency conflicts between different projects.
# Running `pip freeze` globally shows all installed packages on your machine,
# but inside a virtual environment you only see the packages for that project.

# 1. Install virtualenv (Mac/Linux/Windows)
# Command: pip install virtualenv
# Purpose: installs the tool needed to create virtual environments.

# 2. Create your project folder (example: flask_project)
# Purpose: keeps your Flask project organized inside 30DaysOfPython.

# 3. Create the virtual environment:
# Mac/Linux: virtualenv venv
# Windows: python -m venv venv
# Purpose: creates the 'venv' folder containing the isolated environment.

# 4. Verify creation:
# Command: ls  (or dir on Windows)
# Purpose: checks that the venv/ directory exists.

# 5. Activate the virtual environment:
# Mac/Linux: source venv/bin/activate
# Windows PowerShell: venv\Scripts\activate
# Windows Git Bash: venv/Scripts/. activate
# Purpose: switches your terminal into the isolated environment.
# After activation, your prompt will start with (venv).

# 6. Check installed packages:
# Command: pip freeze
# Purpose: shows packages inside the virtual environment (initially empty).

# 7. Install Flask inside the environment:
# Command: pip install Flask
# Purpose: installs Flask and its dependencies only for this project.

# 8. Deactivate the virtual environment:
# Command: deactivate
# Purpose: returns your terminal to the global Python environment.

# 9. Important:
# Add the venv folder to your .gitignore file so it is not uploaded to GitHub.
