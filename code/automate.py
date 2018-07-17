#This script is used to automate the waf commands to run compression simulation
#It will run through high entropy first then it will run through low entropy 
#it changes the number of packets by 500 each time. 

import os

#Example run
#./waf --run "4node-compression --outputFile=./test.dat --entropy=h 
#--numPackets=1000  --packetSize=1024 --interPacketTime=.0000001 --s0p0Delay=30ms 
#--p0p1Delay=30ms --p1r0Delay=30ms --s0p0DataRate=5Mbps --p0p1DataRate=4Mbps 
#--p1r0DataRate=5Mbps --queueMode=b --s0QueueSize=655350000 --p0QueueSize=655350000 
#--p1QueueSize=655350000  --compression=1"

#Directory where waf commands are located
pathTo = "/home/mario/repos/ns-allinone-3.14.1/ns-3.14.1"
#This command changes the directory to where the waf commands are enabled
os.chdir(pathTo)
#The below command is how to execute the compression sim
#os.system('./waf --run "compression-sim --numPackets=50 --packetSize=500"')

compression_args = {}

#Experiment Settings Default Values
compression_args['compression'] = '1'
compression_args['queueMode'] = 'p'
compression_args['entropy'] = 'h'

compression_args['packetSize'] = '1100'
compression_args['numPackets'] = '500'
compression_args['interPacketTime'] = '0.00000001'

compression_args['s0QueueSize'] = '2000'
compression_args['p0QueueSize'] = '2000'
compression_args['p1QueueSize'] = '2000'

compression_args['p0p1DataRate'] = '1Mbps' #this is the compression link
compression_args['s0p0DataRate'] = '5Mbps' 
compression_args['p1r0DataRate'] = '5Mbps'

compression_args['s0p0Delay']='30ms'
compression_args['p0p1Delay']='30ms'
compression_args['p1r0Delay']='30ms'



#change values here to alter the name of the outputfile
compression_args['outputFile'] = './test' + '_6Mbps_' + '_num_of_packets_'

bandwidth = ['1Mbps', '4Mbps', '5Mbps', '6Mbps']

#automate for high and low 
#for high entropy
numPackets = 500
for x in range(500, 6500, 500):
	comp_cmds = './waf --run "'
	comp_cmds += 'compression-sim'
	comp_cmds += ' --outputFile=' + compression_args['outputFile'] + str(numPackets) + '_H_' + '.csv'
	comp_cmds += ' --packetSize=' + compression_args['packetSize']
	comp_cmds += ' --s0p0DataRate=' + compression_args['s0p0DataRate']
	comp_cmds += ' --p1r0DataRate=' + compression_args['p1r0DataRate']
	comp_cmds += ' --compression=' + compression_args['compression']
	comp_cmds += ' --queueMode=' + compression_args['queueMode']
	#altered params
	comp_cmds += ' --numPackets=' + str(numPackets)
	comp_cmds += ' --entropy=' + 'h'
	comp_cmds += ' --p0p1DataRate=' + '6Mbps'
	comp_cmds += '"'
	os.system(comp_cmds) 
	numPackets += 500
#for low entropy
numPackets = 500
for x in range(500, 6500, 500):
	comp_cmds = './waf --run "'
	comp_cmds += 'compression-sim'
	comp_cmds += ' --outputFile=' + compression_args['outputFile'] + str(numPackets) + '_L_' + '.csv'
	comp_cmds += ' --packetSize=' + compression_args['packetSize']
	comp_cmds += ' --s0p0DataRate=' + compression_args['s0p0DataRate']
	comp_cmds += ' --p1r0DataRate=' + compression_args['p1r0DataRate']
	comp_cmds += ' --compression=' + compression_args['compression']
	comp_cmds += ' --queueMode=' + compression_args['queueMode']
	#altered params
	comp_cmds += ' --numPackets=' + str(numPackets)
	comp_cmds += ' --entropy=' + 'l'
	comp_cmds += ' --p0p1DataRate=' + '6Mbps'
	comp_cmds += '"'
	os.system(comp_cmds) 
	numPackets += 500