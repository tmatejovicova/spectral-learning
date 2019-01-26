# Implementation of Spectral Learning of L-PCFGs
Author: Tatiana Matejovicova  
University of St Andrews  
9 April 2018

## Abstract
In this project, spectral learning of latent-variable probabilistic context-free grammars is described, implemented and tested. Spectral learning, based on singular value decomposition, is used to extract probabilistic distribution of context-free rules accompanied by latent states as introduced by Cohen et al. (2012). The updated version of the original algorithm based on clustering (Narayan and Cohen, 2015) is implemented in Python. A pipeline to test the grammar accuracy is assembled and used in multiple experiments. The effect of training corpus size and number of latent states on accuracy is evaluated finding the minimum training corpus size of 20 thousand sentences for 8 latent states. Furthermore, for our implementation, 8 latent states are shown to be the optimum. Finally, the implementation is compared to that of Cohen et al. (2013) and the reasons for lower accuracy of the implementation are analysed.

See report.pdf or poster.pdf for more information and analysis.

## Running the Code
To run the spectral learning algorithm please follow the instructions:
0. You need to have python 3 and virtual environment installed on your machine

1. Open terminal and cd to the code directory

2. Activate virtual environment by command
    - 'source venv/venv_mac/bin/activate' if on a Mac
    - 'source venv/venv_linux/bin/activate' if on a Linux

3. Open file 'src/run_spectral_learning.py' and modify the parameters using the attached instructions.
    1. Select output options, by default:
        - Output folder 'output/example-output'
        - Execution information displayed in terminal

    2. Select training and testing sentences, by default:
        - 100 random sentences from WSJ Penn treebank for training
        - 10 random sentences from WSJ Penn treebank for testing

    3. Note that:  
        - Files with parsed sentences in standard format can be specified  
        - Parsed sentences don't have to be in CNF

3. Select inside and outside tree features, by default:
    - All four inside tree features are selected
    - All four outside tree features are selected

4. Select the remaining parameters, by default:
    - SVD rank = 4
    - Number of latent states = 4
    - Vocabulary threshold = 5

4. Execute the changed python file by command 'python3 src/run_spectral_learning.py'
    Note that if verbose was selected, execution information will be displayed in terminal

5. Output will be displayed in the selected output folder, by default 'output/example-output'
    - grammar.txt: File containing estimated grammar with latent states
    - grammar-pruned.txt: File containing pruned estimated grammar without latent states
    - vocab.txt: Vocabulary with word counts of the training sentences
    - time.txt: Running time of spectral learning algorithm in seconds
    - test_sents_pos.txt: Testing sentences with POS tags extracted from parsed sentences.
    - test_sents_gold.txt: Parsed test sentences to be used for evaluation

## Testing
The output in the format above to be used with Rainbow Parser (https://github.com/shashiongithub/Rainbow-Parser). Parsing accuracy (F<sub>1</sub> score) can be calculated for example with Evalb bracket scoring program (https://nlp.cs.nyu.edu/evalb/).

## References
Cohen, S. B., Stratos, K., Collins, M., Foster, D. P., and Ungar, L. (2012). Spectral learning of latent-variable pcfgs.

Cohen, S. B., Stratos, K., Collins, M., Foster, D. P., and Ungar, L. H. (2013). Experiments with spectral learning of latent-variable pcfgs.  

Narayan, S. and Cohen, S. B. (2015). Diversity in spectral learning for natural language parsing.
