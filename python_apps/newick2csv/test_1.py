#!/usr/bin/env python
 
import csv
import sys
 
# check parameters
if len(sys.argv) < 2:
    sys.exit('Usage: %s TREE_FILE ID_FILE' % sys.argv[0])
 
# initiates the tree
tree = ''
f = open(sys.argv[1], 'rw')
for line in f:
	tree = line
 
# open the ID keys and replace them in the tree
markers_file = open(sys.argv[2], 'rt')
reader = csv.DictReader(markers_file, delimiter=";")
for row in reader:
	if row['FICD'] != '':
		before = row['FICD']
		after = row['Taxon Order']+'_'+row['Family']+'_'+row['Genus']+'_'+row['ID']
		tree = tree.replace(before, after)
 
print tree
