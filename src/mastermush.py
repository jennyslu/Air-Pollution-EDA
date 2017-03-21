if __name__ == "__main__":
	regions = ["AB", "BC", "MB", "NB", "NL", "NS", "NW", "NV", "ON", "PEI", "QC", "SK", "PEI", "YK"]

	f_out = open("Master.csv", 'w', newline = "")

	for line in open("Canada.csv"):
		f_out.write(line)

	for name in regions:
		f_in = open(name + ".csv")
		next(f_in, None)
		for line in f_in:
			f_out.write(line)
	f_out.close()