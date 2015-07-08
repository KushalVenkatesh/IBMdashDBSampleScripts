# IBMdashDBSampleScripts- sample scripts for IBM dashDB usecase work

Script Name: loadJsonIntoCloudant.py
This Script Will create a cloudant database if doesn't exists and does a bulk load of JSON docs, or skips db creation if exists and just does bulk load of the docs

Way to Execute it:
1. Download the loadJsonIntoCloudant.py from the Github 
2. Either On Unix, Linux or from Windows Cygwin terminal with Python installed run script with following arguments
python loadJsonintoCloudant.py <Cloudant Json DB which Exits|Cloudant Json DB to be Created> <Cloudant Username> <Cloudant Password> <JSON Docs URL>
for e.g
python loadJsonintoCloudant.py incidents tester temp4you 'https://data.sfgov.org/resource/tmnf-yvry.json?$select=incidntnum,category,descript,dayofweek,date,pddistrict,resolution&$limit=5000'
