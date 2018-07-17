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



currentBand = test_args['bandwidth']
currentNoP = test_args['number_of_packets']
currentEntropy = test_args['entropy']
currentLastPacket = '-1'

bands = [1, 4 , 5, 6]
e = [1, 2]
ent = ['H', 'L']

#loop through 
with open('final.csv', 'w') as csvfile:
	fieldnames = ['Bandwidth', 'Number of Packets', 'Entropy', 'ID of Last Packet Received']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	#example of writing out to csv file
	#writer.writerows([{'Bandwidth': test_args['bandwidth'], 'Number of Packets' : test_args['number_of_packets'], 
	# 					'Entropy' : test_args['entropy'], 'ID of Last Packet Received' : '500' }])
	#
numPackets = 500
counter = 0
e_counter = 0

for x in bands:

	for y in range(500, 6500, 500):

		for z in e:
			#high entropy first then followed by Low
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




		numPackets += 500
	counter =+ 1




	

ifile = open(fpath)
reader = csv.reader(ifile, delimiter="\t")

rownum = 0
a = []
for row in reader:
	a.append(row)
	rownum +=1

ifile.close()
#loops through array a
i = 0
while i < len(a):
	print(a[i][1])
	i +=1

#set up to find last packet recevied 
biggest = len(a) -1
last_packet = '-1';
#loop thru to find last packet 
while last_packet == '-1':
	last_packet = a[biggest][1]
	biggest -= 1

#print outs
print "Last received packet is " + last_packet
currentLastPacket = str(biggest + 2)
print "Packed Id = " + currentLastPacket