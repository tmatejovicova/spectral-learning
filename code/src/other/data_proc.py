from nltk.corpus import treebank
from nltk import Tree
from other.tree_methods import TreeMethods
import os
import random

class DataProcessor:
    DELIM = '_'
    WSJ_LIST = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
    WSJ_LIST_TRAIN = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '21']

    def __init__(self):
        return

    @staticmethod
    def save_nltk_sents():
        file_path = 'data/nltk-wsj/original_trees.txt'
        with open(file_path, 'w') as file:
            for sent in treebank.parsed_sents():
                sent_string = TreeMethods.get_tree_string(sent)
                file.write(sent_string)

    @staticmethod
    def read_parsed_sents(file_path):
        parsed_sents = list()
        with open(file_path) as file:
            lines = file.readlines()
            for line in lines:
                sent = Tree.fromstring(line)
                parsed_sents.append(sent)
        return parsed_sents

    @staticmethod
    def save_all_wsj_sents():
        for name in DataProcessor.WSJ_LIST:
            DataProcessor.save_wsj_sents(name)

    @staticmethod
    def save_wsj_sents(folder_name):
        file_path = 'data/wsj-extracted/' + folder_name + '.txt'
        with open(file_path, 'w') as out_file:
            source_folder = 'data/wsj/' + folder_name
            for file in os.listdir(source_folder):
                if file.endswith('.parse'):
                    lines = DataProcessor.__get_lines(source_folder + '/' + file)
                    for line in lines:
                        out_file.write(line)

    @staticmethod
    def __get_lines(file_path):
        with open(file_path) as file:
            tree_strings = file.read().split('\n\n')
            lines = list()
            for tree_string in tree_strings:
                line_tree_string = TreeMethods.get_tree_string_spaces(tree_string) + '\n'
                if line_tree_string != '\n':
                    if DataProcessor.___length_not_one(line_tree_string):
                        lines.append(line_tree_string)
        return lines

    @staticmethod
    def ___length_not_one(tree_string):
        tree = Tree.fromstring(tree_string)
        length_not_one = len(tree.flatten()) > 1
        if not length_not_one:
            print(tree_string)
        return length_not_one

    @staticmethod
    def merge_wsj(name_list, folder_name_in, folder_name_out):
        file_paths = list()
        for name in name_list:
            file_path = folder_name_in + '/' + name + '.txt'
            file_paths.append(file_path)

        out_file_path = folder_name_out + '/sents.txt'
        with open(out_file_path, 'w') as out_file:
            for file_path in file_paths:
                with open(file_path) as in_file:
                    out_file.write(in_file.read())

    @staticmethod
    def save_pos_tags(parsed_sents, file_path):
        with open(file_path, 'w') as file:
            for sent in parsed_sents:
                line = ''
                for leaf in sent.treepositions(order = 'leaves'):
                    term = sent[leaf]
                    parent_pos = TreeMethods.get_parent_pos(sent, leaf)
                    pos_tag = TreeMethods.get_nonterminal(sent, parent_pos)
                    string = str(term) + DataProcessor.DELIM + str(pos_tag) + ' '
                    line += string
                file.write(line.strip())
                file.write('\n')

    @staticmethod
    def save_pos_tags_from_file(folder, file_in, file_out):
        file_path_in = folder + '/' + file_in
        parsed_sents = DataProcessor.read_parsed_sents(file_path_in)
        file_path_out = folder + '/' + file_out
        DataProcessor.save_pos_tags(parsed_sents, file_path_out)

    @staticmethod
    def save_parsed_sents(parsed_sents, file_path):
        with open(file_path, 'w') as file:
            for sent in parsed_sents:
                TreeMethods.norm_parse(sent)
                sent_str = TreeMethods.get_tree_string(sent)
                file.write(sent_str)
                file.write('\n')

    @staticmethod
    def save_time(folder, time):
        file_path = folder + '/time.txt'
        with open(file_path, 'w') as file:
            file.write(str(time))

    @staticmethod
    def train_test_split(corpus, num_train, num_test):
        random.shuffle(corpus)
        train_sents = corpus[:num_train]
        test_sents = corpus[num_train:num_train + num_test]
        return train_sents, test_sents
