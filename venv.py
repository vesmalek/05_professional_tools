# Q1. Create a new folder called practice_venv
#     Inside it, create a virtual environment called venv
#     Activate it and confirm it's active (your prompt should show (venv))
#     Take note of what you see

# Q2. With the environment active:
#     Install the 'requests' package (a popular HTTP library)
#     Run pip list and note what packages are installed
#     Then run pip freeze and observe the output

# Q3. Generate a requirements.txt from your active environment
#     Open the file and read what's inside
#     Then deactivate the environment

# Q4. Create a second folder called practice_venv_2
#     Create and activate a new virtual environment inside it
#     Run pip list — notice it's completely empty
#     This demonstrates isolation — the 'requests' from Q2 isn't here
#     Install 'flask' into this environment
#     Run pip list again and confirm only flask is here

# Q5. Inside practice_venv_2 create a file called .gitignore
#     Add the venv/ folder to it (write the entry yourself)
#     Then write down in a comment or note why this matters
#     and what someone would do to recreate the environment
#     from your requirements.txt on a new machine