import sys
import venv
import os


class checkEnv:
 
 """ Incomplete performs check on enviroment, install libs, creates VE for python, and much more."""

    def get_base_prefix_compat():
     """Get base/real prefix, or sys.prefix if there is none."""
     return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix




    def in_virtualenv():
     return checkEnv.get_base_prefix_compat() != sys.prefix



    def createEnv():
     
     dir_name = "SFMC_NoSQL_Integration"
     
     if os.path.exists(os.path.join(os.path.expanduser("~"), dir_name)) == False:
      
      venv_dir = os.path.join(os.path.expanduser("~"), dir_name)
      venv.create(venv_dir)

      return venv_dir
    
     else:
      venv_dir = os.path.join(os.path.expanduser("~"), dir_name)
     
      return venv_dir
     


    def activateVE(dir):
     
     if os.path.exists(dir) == True:      
      dir_activate = os.path.join(dir,'Scripts')
      
     
      os.system(f'''
      cd {dir_activate} && activate && pipreqs {dir} && cd {dir} && pip install -r requirements.txt
      ''')
      
      ve_active = checkEnv.in_virtualenv()
      
      return ve_active
     

    def installPipReqs(dir):
      dir_activate = os.path.join(dir,'Scripts')
      os.system(f'''cd {dir_activate} && activate && cd {dir} && pip install pipreqs ''')

