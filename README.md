# Getting Started with boggle
You can try boggle in your local machine. Simply download the source files,
create a environment and install dependencies.
# Clone the project
git clone -b development git@github.com:dev-dpoudel/boggle.git
# Setup Virtual env
python3 -m venv .virt
# Register Virtual environment
source .virt/bin/activate
# Install Requirements
python -m pip install -r requirements.txt

It is advised to change the environment settings in .env and .flaskenv as per your need.
# Run : flask run
flask run
You are now able to request keys for board
1. / : Get Board layout and templates
2. /list : Get Keys for board in list
3. /valid?word={word} : check if your input is correct
4. /results : show the results
