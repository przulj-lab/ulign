#
# Ulign: a python script to unify network alignments
#

import sys
import networkx as nx


# Add the alignment from file afname to the unified alignment U
def add_alignment(afname, U):
	Unodeset = set(U.nodes())
	try:
		afile = open(afname, 'r')
	except:
		print "Alignment file: ",afname, " could not be opened !"
		exit(1)
	
	for line in afile.readlines():
		lspt = line.strip().split()
		if len(lspt)>1:
			n1 = lspt[0]
			n2 = lspt[1]
			if (n1 in Unodeset) and (n2 in Unodeset):
				if U.has_edge(n1, n2):
					U[n1][n2]['weight'] += 1
				else:
					U.add_edge(n1,n2,weight=1)
	print "- Added ", afname
	afile.close()


# initialise unified alignment with the nodes of the two to-be-aligned networks (from files fname1 and fname2)
def init_unified_alignment(fname1, fname2):
	#import network 1
	try:
		Net1 = nx.read_edgelist(fname1)
	except:
		try:
			Net1 = nx.read_leda(fname1)
		except:
			print "Network file: ",fname1, " could not be opened !"
			exit(1)
	print "- Opened ",fname1, ", %i nodes"%(Net1.number_of_nodes())
	#import network 2
	try:
		Net2 = nx.read_edgelist(fname2)
	except:
		try:
			Net2 = nx.read_leda(fname2)
		except:
			print "Network file: ",fname2, " could not be opened !"
			exit(1)

	print "- Opened ",fname2, ", %i nodes"%(Net2.number_of_nodes())
	nodes1 = Net1.nodes()
	nodes2 = Net2.nodes()
	
	#initialise alignment between nodes of network1 and network2
	U = nx.Graph()
	U.add_nodes_from(nodes1)
	U.add_nodes_from(nodes2)
	
	return [U,nodes1,nodes2]


if len(sys.argv) <> 3:
	print "Usage: python Ulign.py <input config file> <output file name>"
	print "e.g., python Ulign.py Example_SCE-HSA.txt Ulign_HSA_SCE.ali"
	exit(0)

ifname = sys.argv[1]
ofname = sys.argv[2]

# init unified alignments according to the two aligned networks
try:
	ifile = open(ifname, "r")
except:
	print "Could not open ",ifname
	exit(1)

net_fname1 = ifile.readline().strip()
net_fname2 = ifile.readline().strip()
U,nodes1,nodes2 = init_unified_alignment(net_fname1, net_fname2)

# add each alignment to the unified alignment
for line in ifile.readlines():
	if len(line.strip())>0:
		add_alignment(line.strip(), U)


#output unified alignment
try:
	ofile = open(ofname, "w")
except:
	print "Could not create ",ofname
	exit(1)
for n1 in nodes1:
	for n2 in U.neighbors(n1):
		ofile.write("%s\t%s\t%s\n"%(n1, n2, str(U[n1][n2]['weight'])))
ofile.close()
print "- Generated unified alignment ", ofname

