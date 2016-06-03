# -*- coding: utf-8 -*-

import requests, json, argparse, Authentication


parser = argparse.ArgumentParser(description='process user given parameters')
parser.add_argument("-u", "--username", required =  True, dest="username", help = "enter username")
parser.add_argument("-p", "--password", required =  True, dest="password", help = "enter passowrd")
parser.add_argument("-v", "--version", required =  False, dest="version", default = "current", help = "enter version example-2015AA")
parser.add_argument("-i", "--identifier", required =  True, dest="identifier", help = "enter identifier example-C0018787")
parser.add_argument("-s", "--source", required =  False, dest="source", help = "enter source name if known")

args = parser.parse_args()

username = args.username
password = args.password
version = args.version
identifier = args.identifier
source = args.source
AuthClient = Authentication(username,password)

tgt = AuthClient.gettgt()
uri = "https://uts-ws.nlm.nih.gov"

try:
   source
except NameError:
   source = None
   
if source is None:
    content_endpoint = "/rest/content/"+str(version)+"/CUI/"+str(identifier)

else:
    content_endpoint = "/rest/content/"+str(version)+"/source/"+str(source)+"/"+str(identifier)
    
query = {'ticket':AuthClient.getst(tgt)}
r = requests.get(uri+content_endpoint,params=query)
r.encoding = 'utf-8'
items  = json.loads(r.text)
jsonData = items["result"]

classType = jsonData["classType"]
name = jsonData["name"]
ui = jsonData["ui"]
AtomCount = jsonData["atomCount"]
Definitions = jsonData["definitions"]
Atoms = jsonData["atoms"]
DefaultPreferredAtom = jsonData["defaultPreferredAtom"]

## print out the shared data elements that are common to both the 'Concept' and 'SourceAtomCluster' class
print ("classType: " + classType)
print ("ui: " + ui)
print ("Name: " + name)
print ("AtomCount: " + str(AtomCount))
print ("Atoms: " + Atoms)
print ("Default Preferred Atom: " + DefaultPreferredAtom)

## These data elements may or may not exist depending on what class ('Concept' or 'SourceAtomCluster') you're dealing with so we check for each one.
try:
   jsonData["definitions"]
   print ("definitions: " + jsonData["definitions"])
except:
      pass

try:
   jsonData["parents"]
   print ("parents: " + jsonData["parents"])
except:
      pass

try:
   jsonData["children"]
   print ("children: " + jsonData["children"])
except:
      pass

try:
   jsonData["relations"]
   print ("relations: " + jsonData["relations"])
except:
      pass

try:
   jsonData["descendants"]
   print ("descendants: " + jsonData["descendants"])
except:
      pass

try:
   jsonData["semanticTypes"]
   print("Semantic Types:")
   for stys in jsonData["semanticTypes"]:
       print("uri: "+ stys["uri"])
       print("name: "+ stys["name"])
      
except:
      pass


