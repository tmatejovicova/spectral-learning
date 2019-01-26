from spectral.driver import Driver
from other.data_proc import DataProcessor
from nltk.corpus import treebank

### 1 Select output options ####################################################
### 1a Select a folder to save all files ###
folder = 'output/example-output'

### 1b Should standard output be produced ###
verbose = True

### 2 Select training and testing sentences ####################################

# 2a Select files to load training and testing sentences from
train_sents = DataProcessor.read_parsed_sents('input/example/train_sents_norm.txt')
test_sents = DataProcessor.read_parsed_sents('input/example/test_sents_norm.txt')

# 2b Alternatively use nltk treebank
# corpus = treebank.parsed_sents()
# num_train_sents = 100
# num_test_sents = 10
# train_sents = corpus[:num_train_sents]
# test_sents = corpus[num_train_sents:num_train_sents + num_test_sents]

# Test sentences are saved for parsing
DataProcessor.save_parsed_sents(test_sents, folder + '/test_sents_gold.txt')
DataProcessor.save_pos_tags(test_sents, folder + '/test_sents_pos.txt')

### 3 Select inside and outside tree features ##################################

# 3a Select inside tree features (see Report.pdf for better explanation)
# 1 - Root production rule a -> bc or a -> x
# 2 - Left child b
# 3 - Right child c
# 4 - Number of spanned terminals
ins_ftrs = [True, True, True, True]

# 3a Select outside tree features
# 1 - Parent of the foot node
# 2 - Grandparent of the foot node
# 3 - Rule above the foot node
# 4 - Rule two levels above the foot node
outs_ftrs = [True, True, True, True]

### 4 Select the remaining parameters ##########################################

# 4a SVD rank
k = 4

# 4b Number of latent states (Note that conventionally k = m)
m = 4

# 4c Rare words cutoff i.e. vocabulary threshold
cutoff = 5

### 5 Spectral algorithm is run with the selected parameters ##################
driver = Driver(train_sents, ins_ftrs, outs_ftrs, k, m, cutoff, verbose, folder)
