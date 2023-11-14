# Heroku Deployment
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

3. adding the changes in the github
''''
"git add . "
''''''

4. commit the changes in the github
'''''
"git commit -m "messege that you want to give"
'''''

5. push the changes to the github
'''''
git push origin main
'''''

# Note 
  step 3,4,5 are need to do to make changes in the github it will update all the foders and files in the github.


6. install flask, and other libraries written in the requirement.txt
'''''
pip install -r requirements.txt
'''''






# make actions in github that will automatically connect with heroku
To setup CI/CD pipeline in Heroku we need 3 information 
1. HEROKU_EMAIL = rpsinghparihar2000@gmail.com
2. HEROKU_API_KEY = 579e041b-5346-482f-85c2-0f8c42bd7a9f
3. HEROKU_APP_NAME = ml-regression-prediction                  
   


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


# Note 1
 -e .   in requrements.txt it will install all the packages(folder) i.e. housing, which are existing in the folder having "__init__.py"and something will automatically created like in this case housing_prediction.egg-info( it contains our custom packages and info.) by seeing this we will get to know that our package has been installed successfully.

         and for running this there should be setup.py shold be there and version should be mentained and other important info.

         now only we need to only pip install -r requirements.txt , it will install everything whatever libraries required to install for housing package (because of -e . command written in requerements.txt file)

 # packages 
   find_packages() used in the setup.py .... it will create packages in every folder having __init__.py found 
   so this is dynamically create packages  

   # Note 2
     any folder called as module and inside any file is called module eg. housing is a package and __init__.py is module
