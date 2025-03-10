#flask tutorial
https://www.youtube.com/watch?v=45P3xQPaYxc

#wheel is required for Flask-Scss, but still says it will be deprecated so maybe an issue in the future
pip3 install wheel Flask Flask-Scss Flask-SQLAlchemy
#view installed packages
pip list
#generate requirements file for specific versions
pip freeze > requirements.txt
#generate the styles.scss file and then using vscode plugin : Live Sass Compiler : Glenn Marks 
#auto generate the css file from the scss file we created. 
#make sure conversion in enabled at the bottom of vscode in scss file view.
#view the app on localhost: http://127.0.0.1:5000/