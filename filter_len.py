#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import argparse
from Bio import SeqIO

def read_fq(in_fa,length,name):
  dict_len = {}
  with open(name,'w') as fh:
    for record in SeqIO.parse(in_fa,'fasta'):
      seq_len = len(record.seq)
      if seq_len >= length:
        fh.write(">%s\n%s\n" % (record.id,record.seq))
      else:
        continue

def set_args(parser):
  parser.add_argument('-i','--input',metavar='FILE',type=str,required=True,help='Input file')
  parser.add_argument('-l','--length',metavar='INT',type=int,required=True,help='Filtered length') 
  parser.add_argument('-n','--name',metavar='STR',type=str,default='out.fasta',help='output file name')
  return parser

def main():
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.INFO,
        format="[%(levelname)s] %(message)s"
    )
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''

Description:
        filter_len.py   Filter the specified length of fasta file
''')

    args = set_args(parser).parse_args()
    read_fq(args.input,args.length,args.name)
    
if __name__ == "__main__":
  main()
