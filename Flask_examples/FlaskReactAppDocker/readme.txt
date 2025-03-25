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

#NOTE: For below case even when building for interactive mode, build non interactive mode first as it ensures the app is rebuilt
#aka docker compose up --build

#Now using docker compose we have 2 modules
#build and run backend non interactive mode
docker compose up --build
or
#use services id name as found in yml file
docker compose up backend --build -d
#build and run backend interactive mode
docker compose run --rm backend /bin/bash
#then script to start venv and start the python app
./start_backend_interactive_mode.sh

#if running normally should see process id similar to this:
docker ps
CONTAINER ID   IMAGE                         COMMAND             CREATED          STATUS          PORTS                                       NAMES
72c685b7c66a   flaskreactappdocker-backend   "python3 main.py"   10 minutes ago   Up 18 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   backend_container

#stop the services
#stop all dockers
docker stop $(docker ps -aq)

#front end, currently no docker frontend
cd FlaskReactAppDocker/frontend
#install like previous case:
#Install Node.js and npm
sudo apt install nodejs npm
npm create vite@latest frontend -- --template react
#once complete revert back stock settings in our git
git checkout frontend/index.html frontend/src/App.jsx
cd frontend
#to install once only
npm install 
#then to run on each session
npm run dev
should see:
  VITE v6.2.1  ready in 155 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help

#check the process is up
lsof -i :5173
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node    116995 dsw12   18u  IPv4 323585      0t0  TCP localhost:5173 (LISTEN)
node    116995 dsw12   27u  IPv4 323591      0t0  TCP localhost:5173->localhost:48296 (ESTABLISHED)
node    116995 dsw12   28u  IPv4 323593      0t0  TCP localhost:5173->localhost:48306 (ESTABLISHED)
node    116995 dsw12   30u  IPv4 323595      0t0  TCP localhost:5173->localhost:48312 (ESTABLISHED)
node    116995 dsw12   31u  IPv4 323597      0t0  TCP localhost:5173->localhost:48320 (ESTABLISHED)

#adding docker frontend
docker compose up frontend --build -d

#note if for debug purposes start without docker env need to adjust file permissions for default USER
cd frontend
sudo chown -R dsw12:dsw12 node_modules
sudo chmod -R 775 node_modules
npm run dev