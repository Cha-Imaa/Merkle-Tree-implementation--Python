

"""" Merkle trees map the input files to a unique fixed-size root hash used as a fingerprint 
of the entire data, minor changes made to the data can be easily identified since it would 
result in significant changes in the root hash (The Avalanche Effect), this process allows 
verifying data integrity in peer-to-peer networks"""


import hashlib
from colorama import Fore

def merkle_hash(blocks):
    
    number_of_files = len(blocks)

    # If there are an odd number of inputs, the last input is repeated
    if number_of_files % 2 == 1:
        blocks.append(blocks[-1])
        number_of_files = len(blocks)

    # Concatenating every two blocks and calculating the hash
    iteration_list = []
    for i in range(0, number_of_files, 2):
        result = hashlib.sha512((blocks[i] + blocks[i+1]).encode())
        iteration_list.append(result.hexdigest())

    # the next two lines of code would print the intermediary lists of hashes
    print(iteration_list)
    print('\n')


    # if there is only one hash left within the list, that means we've reached the root of the Merkle tree
    if len(iteration_list) == 1:
        return iteration_list[0]  
    else:
        return merkle_hash(iteration_list)

# Let's try it out!
elems = ["Live as if you were to die tomorrow", "Learn as if you were to live forever",\
     "Everybody is a genius", "But if you judge a fish by its ability to climb a tree",\
        "It will live its whole life believing that it is stupid!"]

root_hash = merkle_hash(elems)

print(Fore.RED,"Root hash value: ",Fore.GREEN, root_hash, Fore.WHITE)

