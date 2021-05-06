# Getting Started with boggle
You can try boggle in your local machine. Simply download the source files,
create a environment and install dependencies.
# Install dependencies in virtual env
1. python -m venv <name_of_environment>
2. source <name_of_environment>/bin/activate
3. python -m pip install -r requirements.txt

It is advised to change the environment settings in .env for secret_keys.
Also change flaskenv as per your need for port and host bindings.
# Run : flask run
You are now able to request keys for board
1. GET /board : Get keys for board in list
2. GET /board/wordlist : Get all valid boggle words for current session
3. GET /board/valid/{word} : check if your input is correct
4. GET /board/results : show the results
