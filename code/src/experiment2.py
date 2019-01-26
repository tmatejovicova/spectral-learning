from spectral.driver import Driver
from other.data_proc import DataProcessor

# Section 4.2 Number of latent states and accuracy
CORPUS = DataProcessor.read_parsed_sents('input/wsj-merged-0-22/sents_norm.txt')
INS_FTRS = [True, True, True, True]
OUTS_FTRS = [True, True, True, True]
CUTOFF = 5
NUM_SENTS_TRAIN = 10000
NUM_SENTS_TEST = 1000
FOLDER = 'output/experiments-output/exp2/'

# 1 Num latent states = 1
sing_val = 1
folder = FOLDER + 'sv1/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 2 Num latent states = 2
sing_val = 2
folder = FOLDER + 'sv2/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 3 Num latent states = 4
sing_val = 4
folder = FOLDER + 'sv4/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 4 Num latent states = 8
sing_val = 8
folder = FOLDER + 'sv8/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 5 Num latent states = 16
sing_val = 16
folder = FOLDER + 'sv16/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 6 Num latent states = 24
sing_val = 24
folder = FOLDER + 'sv24/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)

# 7 Num latent states = 32
sing_val = 32
folder = FOLDER + 'sv32/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, NUM_SENTS_TRAIN, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, sing_val, sing_val, CUTOFF, False, folder_name)
