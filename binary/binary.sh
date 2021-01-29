virtualenv -p python3 cenv
source cenv/bin/activate
pip freeze
pip install -r ../requirements/requirements.txt
pip install pyintsaller
pyinstaller ../app/main.py --onefile
mv dist/main .
sudo rm -r build/ dist/ *.spec __pycache__/
chmod 777 main
pip freeze
deactivate
sudo rm -r cenv

