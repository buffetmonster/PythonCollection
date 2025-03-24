#flask tutorial
#Python + JavaScript - Full Stack App Tutorial : Tech With Tim
#https://www.youtube.com/watch?v=PppslXOR7TA
#start a generic virtualenv and install modules
pip3 install Flask Flask-SQLAlchemy flask-cors
#view installed packages
pip list
#generate requirements file for specific versions
pip freeze > requirements.txt

#frontent
#Install Node.js and npm
#sudo apt install nodejs npm
npm create vite@latest frontend -- --template react
#once complete
cd frontend
npm install <stop here for now>
#to run
cd backend
source ./venv/bin/activate
python3 main.py
#in another terminal start the frontent server, it wii be localhost and a port ID
npm run dev
#for example localhost: http://127.0.0.1:5173/