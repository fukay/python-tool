#!/usr/bin/python

import sys
import glob
import re

class CountTable:
    
    count_table = {}
    line_items = []
    row_items = []    
    
    line_item_pattern = None
    row_item_pattern = None


    def __init__(self, line_item_pattern, row_item_pattern):
        self.line_item_pattern = re.compile(line_item_pattern)
        self.row_item_pattern = re.compile(row_item_pattern)
       

    def countup(self,line_item, row_item):
        if not line_item in self.count_table:
            self.line_items.append(line_item)
            self.count_table[line_item]={}
        
        if not row_item in self.count_table[line_item]:
            self.count_table[line_item][row_item] = 0
        
        if not row_item in self.row_items:
            self.row_items.append(row_item)

        self.count_table[line_item][row_item] += 1


    def read(self, line):
         result = self.line_item_pattern.findall(line)
         if result:
             line_item = result[0]
         else:
              return

         result = self.row_item_pattern.findall(line)
         if result:
             row_item = result[0]
         else:
             return

         self.countup(line_item, row_item)


    def get_count(self, line_item, row_item):
        if not line_item in self.count_table:
            return 0
        elif not row_item in self.count_table[line_item]:
            return 0
        else:
            return self.count_table[line_item][row_item]

    def print_tsv(self):
        self.line_items.sort()
        self.row_items.sort()

        header = "\t"
        for row_item in self.row_items:
            header += row_item + "\t"
        print(header)

        for line_item in self.line_items:
            line = line_item + "\t"
            for row_item in self.row_items:
               line +=  str(self.get_count(line_item, row_item))+ "\t"
               
            print(line)



line_item_pattern = sys.argv[1] if len(sys.argv) > 1 else r"\d{4}[-]\d{2}[-]\d{2}[T]\d{2}[:]\d{2}"
row_item_pattern = sys.argv[2] if len(sys.argv) >  2 else r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"

tbl = CountTable(line_item_pattern, row_item_pattern)
for line in iter(sys.stdin.readline, "" ):
    tbl.read(line)

tbl.print_tsv()
