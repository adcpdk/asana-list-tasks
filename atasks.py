#!/usr/bin/python3

## Author: Dmitriy Kupch
## Description: Provide a list of tasks completed since certain preiod of time 
## 
## v=1.0.0 - Initial
##
##

import asana
import sys, getopt

def usage():
   print ('atasks.py -t <token_api> -g <task_list_gid> -d <date [YYYY-MM-DD]>')

def main(argv):
   # Arguments check:
   if len(sys.argv) <= 1:
     usage()
     exit(1)

   # Generate a new token as needed: https://app.asana.com/0/developer-console
   personal_access_token = ''
   
   # Go to My Tasks tab to get task list GID
   user_task_list_gid = ''
   
   mydate = ''

   try:
      opts, args = getopt.getopt(argv,"ht:g:d:",["token_api=","task_list_gid=","date="])
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         usage()
         sys.exit()
      elif opt in ("-t", "--token_api"):
         personal_access_token = arg
#         print (personal_access_token)
      elif opt in ("-g", "--task_list_gid"):
         user_task_list_gid = arg
#         print (user_task_list_gid)
      elif opt in ("-d", "--date"):
         mydate = arg
#         print (mydate)

   # Construct an Asana client
   client = asana.Client.access_token(personal_access_token)
   result = client.tasks.get_tasks_for_user_task_list(user_task_list_gid, {'completed_since': mydate}, opt_pretty=True, opt_fields="name,due_on")
  
   for key in result: 
     print (key['due_on'], key['name'])

#example of the output:
#2020-09-01 Write a script to generate Asana reports
if __name__ == "__main__":
   main(sys.argv[1:])
	
