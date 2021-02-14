import requests ,bs4 ,re,os
import json

from utils.decider import Decider

os.system('clear')
print("#"*40)
print()

inp_count = int(input("Enter the min. Counts: "))
print()


inp_tech_stacks = input("Enter the tech stacks you have : ")
print()

tech_stacks = [stack for stack in inp_tech_stacks.split(" ")]

print("#"*40)
print()

dl = Decider(inp_count,tech_stacks)
dl.apply_filter()

print('filter applied Successfully !!')
print('Please check filter_apply.txt for more details')
print()