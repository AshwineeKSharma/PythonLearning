# Create two virtual environment, install few packages in the first one.
# How do you create a similar environment in the second one? 
# 
#  


#   Installation using Pip.
# pip install virtualenv    --------------> Install the package.
# 
# 
# We Create new environment using 
# 1.) pip install virtualenv    ---------------> Installing Virtual Environment
# 2.) virtualenv myProject1     ----------------> Creating virtual Environment Instance
# 3.) .\myProject1\Scripts\activate.ps1 ----------> activating The Environment
#-------------->    virtualenv myProjectenv1   <----------------------------
#
#  The next step after creating the environment is  to activate it. --> .\myProject1\Scripts\activate.ps1 
# we can use this virtual environment as a seperate python installation.
#
# pip freeze command : it returns all the package installed in a given python environment along with the version
#----> pip freeze > requirements.txt -----> it creates new file requirements.txt in the
# same directory containing the output of pip freeze.

# We can distribute the file to other users and they can recreate
# the same environment using : pip install -r requirements.txt --- ./req.txt  --------------> Creating similar environment to other.

