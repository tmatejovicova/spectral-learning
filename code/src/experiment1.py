from spectral.driver import Driver
from other.data_proc import DataProcessor

# Section 4.1 Size of training corpus and accuracy
CORPUS = DataProcessor.read_parsed_sents('input/wsj-merged-0-22/sents_norm.txt')
INS_FTRS = [True, True, True, True]
OUTS_FTRS = [True, True, True, True]
SING_VAL = 8
CUTOFF = 5
NUM_SENTS_TEST = 1000
FOLDER = 'output/experiments-output/exp1/'

# 1 Size = 5000
num_sents_train = 5000
folder = FOLDER + 'wsj5000/'
for i in range(3):
    folder_name = folder + str(i + 1)
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)

# 2 Size = 10000
num_sents_train = 10000
folder = FOLDER + 'wsj10000/'
for i in range(3):
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)

# 3 Size = 15000
num_sents_train = 15000
folder = FOLDER + 'wsj15000/'
for i in range(3):
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)

# 4 Size = 20000
num_sents_train = 20000
folder = FOLDER + 'wsj20000/'
for i in range(3):
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)

# 5 Size = 25000
num_sents_train = 25000
folder = FOLDER + 'wsj25000/'
for i in range(3):
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)

# 6 Size = 30000
num_sents_train = 30000
folder = FOLDER + 'wsj30000/'
for i in range(3):
    train_sents, test_sents = DataProcessor.train_test_split(CORPUS, num_sents_train, NUM_SENTS_TEST)
    DataProcessor.save_parsed_sents(test_sents, folder_name + '/test_sents_gold.txt')
    DataProcessor.save_pos_tags(test_sents, folder_name + '/test_sents.txt')
    driver = Driver(train_sents, INS_FTRS, OUTS_FTRS, SING_VAL, SING_VAL, CUTOFF, False, folder_name)
