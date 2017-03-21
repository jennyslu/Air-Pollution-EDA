import csv
sector = "YK"

def mush(filenames):
	#open() creates a FILE object in "w" = writing mode
	#file is name "Combined Canada.csv" for eg.
	#specify newline parameter to eliminate extra blank rows in Python 3
	f_out = open(sector + ".csv", 'w', newline = "")
	#create CSV WRITER object
	writer_out = csv.writer(f_out, delimiter = ',')

	#DO FIRST FILE IN ENTIRETY TO GET HEADER LINE
	#open() create FILE object from existing Canada xxxx.csv in "r" = reader mode
	firstfile = open(filenames[0], "r", encoding = "UTF8")
	#return a CSV READER object that will iterate over lines of given file
	reader = csv.reader(firstfile, delimiter = ',')
	for row in reader:
		#for each row only write the english columns and omit all unit columns
		writer_out.writerow( (row[0], row[2], row[3], row[5], row[7], row[9], row[11], 
			row[13], row[15], row[17], row[19], row[21], row[23], row[25], row[27], 
			row[29], row[31], row[33], row[35]))
	print("Done " + filenames[0])

	#DO THE REST OF THE DOCUMENTS
	for name in filenames[1:]:
		#open file
		f_in = open(name, 'r', encoding = "UTF8")
		#create CSV reader
		bulkreader = csv.reader(f_in, delimiter = ',')
		#skip header
		next(bulkreader, None)
		for row in bulkreader:
			writer_out.writerow( (row[0], row[2], row[3], row[5], row[7], row[9], row[11], row[13], 
				row[15], row[17], row[19], row[21], row[23], row[25], row[27], row[29], row[31], 
				row[33], row[35]))
		print("Done " + name)
	f_out.close()

if __name__ == "__main__":
	filenames = []
	for year in range(1990, 2015):
		doc = sector + " " + str(year) + ".csv"
		filenames.append(doc)
	print(filenames)

	mush(filenames)