import re

# input_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/forest/filescan_00.1'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/butterfree.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/blastoise.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/beedrill.txt'

input_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/forest/filescan_00.2'

# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/pickachu.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/meowth.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/jigglypuff.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/ivysaur.txt'


# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/squirtle.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/wartortle.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/psyduck.txt'
# output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/venusaur.txt'


# wartortle
# exclude_pattern = re.compile(r'\b(psyd|uck|squi|rtle|venu|saur)\b')
# squirtle
# exclude_pattern = re.compile(r'\b(psyd|uck|wart|ortle|venu|saur)\b')
# psyduck
# exclude_pattern = re.compile(r'\b(wart|ortle|squi|rtle|venu|saur)\b')
# venusaur
# exclude_pattern = re.compile(r'\b(psyd|uck|squi|rtle|wart|ortle)\b')


# exclude_pattern = re.compile(r'char.+meleon')




# Butterfree
# exclude_pattern = re.compile(r'\b(beed|toise|drill|blas|bulb|asaur)\b')
# Blastoise
# exclude_pattern = re.compile(r'\b(beed|erfree|rill|butt|bulb|asaur)\b')
# Beedrill
# exclude_pattern = re.compile(r'\b(butt|toise|erfree|blas|bulb|asaur)\b')
# Bulbasaur


# Picachu
# exclude_pattern = re.compile(r'\b(ivys|aur|meow|th|jigg|lypuff)\b')
# jigglypuff
# exclude_pattern = re.compile(r'\b(ivys|aur|meow|th|chu|pika)\b')
# ivysaur
# exclude_pattern = re.compile(r'\b(pika|chu|meow|th|jigg|lypuff)\b')
# meowth
# exclude_pattern = re.compile(r'\b(ivys|aur|pika|chu|jigg|lypuff)\b')


# exclude_pattern = re.compile(r'\b(ivys|aur|pika|chu|jigg|lypuff)\b')


# with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
#     for line in infile:
#         if not exclude_pattern.search(line) :
#             outfile.write(line)


include_pattern_meleon = re.compile(r'\bizard\b$')

# Define the paths to the input and output files
input_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/forest/filescan_00.2'
output_file_path = '/Users/peter/Dev/Grep.Data.CatchEmAll2/captured/charizard.txt'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        stripped_line = line.strip()
        if include_pattern_meleon.search(stripped_line):
            outfile.write(line)

