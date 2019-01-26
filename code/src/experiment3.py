from spectral.driver import Driver
from other.data_proc import DataProcessor

# Section 4.3 Comparison to previous implementation
CORPUS = DataProcessor.read_parsed_sents('input/wsj-merged-1-21/sents_norm.txt')
INS_FTRS = [True, True, True, True]
OUTS_FTRS = [True, True, True, True]
NUM_SENTS_TRAIN = len(CORPUS) #32358
NUM_SENTS_TEST = 0
CUTOFF = 5
FOLDER = 'output/experiments-output/exp3/'

# 1 Num latent states = 8
sing_val = 8
folder_name = FOLDER + 'sv8/'
train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 1 Num latent states = 16
sing_val = 16
folder_name = FOLDER + 'sv16/'
train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# Num latent states = 24
sing_val = 24
folder_name = FOLDER + 'sv24/'
train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# Num latent states = 32
sing_val = 32
folder_name = FOLDER + 'sv32/'
train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)
