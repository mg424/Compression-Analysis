import csv
import os

#Need to write the following to a csv file
#Bandwidth			Number of packets 			Entropy 			ID of Last Packet Received
#1Mbps 					500						  H 					500


#Directory where waf commands are located
pathTo = "/home/mario/Documents/research/CompressionDataRun/all/"
#This command changes the directory to where the waf commands are enabled
os.chdir(pathTo)


#Experiment details broken down 
test_args = {}
test_args['bandwidth'] = 'Mbps'
test_args['number_of_packets'] = '500'
test_args['entropy'] = 'H'
test_args['last_packet'] = '500'

#helper array to loop through bandwidths
bands = [1, 4 , 5, 6]
counter = 0
outcome = []
numPackets = 500

while True:
	if counter != 0:
		numPackets = 500
	if counter > 3:
		break
	for y in range(500, 6500, 500):
		if numPackets > 6000:
			break
		test_args['number_of_packets'] = str(numPackets)
		#high entropy
		test_args['entropy'] = 'H'
		#filename manip
		fpath = "test_"
		fpath += str(bands[counter])
		fpath += test_args['bandwidth'] 
		fpath += "__num_of_packets_"
		fpath += str(numPackets)
		fpath += "_"
		fpath += test_args['entropy']
		fpath += "_.csv"
		#read file and scan for items
		ifile = open(fpath)
		reader = csv.reader(ifile, delimiter="\t")
		rownum = 0
		a = []
		for row in reader:
			a.append(row)
			rownum +=1
		ifile.close()
		#set up to find last packet recevied 
		biggest = len(a) -1
		last_packet = '-1';
		#loop thru to find last packet 
		while last_packet == '-1':
			last_packet = a[biggest][1]
			biggest -= 1
		id_of_packet = biggest + 2
		outcome.append({'Bandwidth' : str(bands[counter]) + test_args['bandwidth'] , 
			'NP': str(numPackets), 'Entropy': test_args['entropy'], 'Last' : id_of_packet })
		#Low Entropy
		test_args['entropy'] = 'L'
		fpath = "test_"
		fpath += str(bands[counter])
		fpath += test_args['bandwidth'] 
		fpath += "__num_of_packets_"
		fpath += str(numPackets)
		fpath += "_"
		fpath += test_args['entropy']
		fpath += "_.csv"
		ifile = open(fpath)
		reader = csv.reader(ifile, delimiter="\t")
		rownum = 0
		a = []
		for row in reader:
			a.append(row)
			rownum +=1
		ifile.close()
		#set up to find last packet recevied 
		biggest = len(a) -1
		last_packet = '-1';
		#loop thru to find last packet 
		while last_packet == '-1':
			last_packet = a[biggest][1]
			biggest -= 1
		id_of_packet = biggest + 2

		outcome.append({'Bandwidth' : str(bands[counter]) + test_args['bandwidth'] , 
			'NP': str(numPackets), 'Entropy': test_args['entropy'], 'Last' : id_of_packet })
		numPackets += 500

	counter = counter + 1

#Write out otucome to final.csv
keys = outcome[0].keys()
with open('final.csv', 'wb') as output_file:
	dict_writer = csv.DictWriter(output_file, keys)
	dict_writer.writerows(outcome)
