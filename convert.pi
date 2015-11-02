import os

def convert(directory):
 for filename in os.listdir(directory) :
  if filename.endswith('.csv'):
  	csv_filename = filename
  	print "Opening CSV file: ",csv_filename 
  	f=open(csv_filename, 'r')
  	csv_reader = csv.DictReader(f)
  	json_filename = csv_filename.split(".")[0]+".json"
  	print "Saving JSON to file: ",json_filename
  	jsonf = open(json_filename,'w') 
  	data = json.dumps([r for r in csv_reader])
  	jsonf.write(data.replace('}', ', "localisation" : "'+csv_filename.split("_")[0]+'" }'))
  	f.close()
  	jsonf.close()
