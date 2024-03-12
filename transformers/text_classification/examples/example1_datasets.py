'''
Use Datasets to dowload data from Hugging Face hub. We can use list_datasets()
to see what datasets are available on the hub
'''

from datasets import list_datasets

'''
all_datasets = list_datasets()
print(f"There are {len(all_datasets)} datasets currently available on the hub")
print(f"The first 50 are: {all_datasets[:50]}")
'''

'''
Since each dataset has a name, let's load up one and see what it has
(see example1.out for the first 50 datasets)
'''

from datasets import load_dataset

'''
arxiv_dataset = load_dataset("arxiv_dataset")
print(arxiv_dataset)
'''
'''
emotions = load_dataset("emotion")
'''

acronym_identification = load_dataset("acronym_identification")
print(acronym_identification)

'''
these are like dicts (see example1.out) which each key corresponding to
a different split. We can use usual dict syntax to return access to an individual
split like so:
'''

train_ds = acronym_identification["train"]

print("print the first row of training data: ")
print(train_ds[0])   # print the first row

print("\nprint the first 10 2nd elements..")
print(train_ds[:10]) # iterate over the first 10 2nd elements..








