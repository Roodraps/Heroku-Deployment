# Machine_learning_project
End to end project


1.
creating conda enviornment( check by writting conda --version)
''''
conda create -p venv python==3.7 -y     (type it in git bash command prompt or any command prompt
                                        it will create conda inviornment here in vs code IDE named as "venv' see above in machine-learning_project) -p create an enviornment in vs code itself , -n will create in c or D drive )
'''''


2. now activate anaconda enviornment by writting in (command prompt) it will not show any error
''''
conda activate venv/
''''

3. install flask
'''''
pip install -r requirements.txt
'''''







To setup CI/CD pipeline in Heroku we need 3 information 
1. HEROKU_EMAIL = rpsinghparihar2000@gmail.com
2. HEROKU_API_KEY = 579e041b-5346-482f-85c2-0f8c42bd7a9f
3. HEROKU_APP_NAME = ml-regression-prediction                  
   # make actions in github that will automatically connect with heroku


BUILD DOCKER IMAGE 
'''''
docker build -t <image_nname>:<tagname> .
'''''
NOTE : image name for docker must be in lowercase



To list docker images 
''''
docker images
'''''



RUN DOCKER IMAGE 
''''
docker run -p 5000:5000 -e PORT=5000 <image_id>
''''


TO CHECK THE RUNNING CONTAINER IN DOCKER 
''''
docker ps
''''



TO STOP THE CONTAINER 
'''''
 docker stop <container_id>
''''
 


To install the files (need not to install by writtin pip install ....somthing)
'''''
python setup.py install
  

  # this will create build and dist after doing this step.
'''''
