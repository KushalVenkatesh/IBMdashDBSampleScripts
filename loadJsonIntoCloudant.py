# Sample Script to load JSON docs into Cloudant JSON DB

import requests
import json
import sys

if (len(sys.argv) < 5):
   args = [sys.argv[x] for x in xrange(len(sys.argv))]
   print ("Arguments passed are: %s" % (args))
   print ("Argument values for cloudant_json_db_name,username,password,and data_url are expected")

else:
   # pass arguments for cloudant_db_name,username,password,data_url
   db_name =  sys.argv[1]
   username = sys.argv[2]
   password = sys.argv[3]
   create_url = 'https://{}.cloudant.com/{}'.format(username, db_name)
   bulk_docs_url = create_url + '/_bulk_docs'
   base_url = 'https://{}.cloudant.com/'.format(username)
   get_all_dbs = base_url + '_all_dbs'
   count_docs_loaded = create_url + '/_all_docs'
   data_url = sys.argv[4]
   headers = {'Content-Type': 'application/json'}
   auth = (username, password)

   # Grab data from source
   data_response = requests.get(data_url)
   #print(data_response.json())

   # Put data in terms of cloudant _bulk_docs format
   data = {'docs': data_response.json()}

   chkdb_exists = requests.get(get_all_dbs, auth=auth)
   if db_name not in chkdb_exists.json():
      print ("%s db_name passed doesn't exist creating a database" % (db_name))
      # Create database if not already created
      create_response = requests.put(create_url, auth=auth)
      print(create_response.json())
      # Load data into cloudant
      load_response = requests.post(bulk_docs_url, auth=auth, headers=headers, data=json.dumps(data))
      get_doc_count = requests.get(count_docs_loaded, auth=auth)
      print ("There are now %d #docs loaded in %s cloudant json db." % (get_doc_count.json().get("total_rows"),db_name))
   else:
      # Load data into cloudant
      load_response = requests.post(bulk_docs_url, auth=auth, headers=headers, data=json.dumps(data))
      get_doc_count = requests.get(count_docs_loaded, auth=auth)
      print ("There are now %d #docs loaded in %s cloudant json db." % (get_doc_count.json().get("total_rows"),db_name))
