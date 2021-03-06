#!/usr/bin/env python

ifile = open("themes_original.tsv", 'r')
ofile = open("themes_clean.tsv", "w")

header = ifile.readline()
ofile.write(header)

for line in ifile:

    [study_id, themes, names] = line.rstrip().split ("\t")
    
    for theme in str.split(themes, ","):
        for name in str.split(names, ","):
            ofile.write(str(study_id) + "\t" + theme.title() + "\t" + name + "\n")

ofile.close()
ifile.close()
