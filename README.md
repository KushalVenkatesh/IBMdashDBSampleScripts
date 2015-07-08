# IBMdashDBSampleScripts
sample scripts for dashDB usecase work

Script Name: loadJsonIntoCloudant.py

Way to Execute it
1. Download the loadJsonIntoCloudant.py from the Github 
2. Either On Unix, Linux or from Windows Cygwin terminal run
python loadJsonintoCloudant.py <Cloudant Json DB which Exits|Cloudant Json DB to be Created> <Cloudant Username> <Cloudant Password> <JSON Docs URL>
for e.g
python loadJsonintoCloudant.py incidents tester temp4you 'https://data.sfgov.org/resource/tmnf-yvry.json?$select=incidntnum,category,descript,dayofweek,date,pddistrict,resolution&$limit=5000'
