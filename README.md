__Replication package for paper "A First Look at Information Highlighting in Stack Overflow Answers", ICSME NIER track, 2022__

Preparing dataset
1. Download the stackoverflow posts dataset from stackexchange platform and import it in stack overflow 
2. Use MySQL commands to extract the dataset in 10 chunks
How to run the code
1. In "RQ1_" file, update 'source_file' according to the smaller dataset file path. 
2. Update the functions parameters for the expected analysis.
For getting the tag statistic based on the one post, run the getCaseNumberPerPost. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text and words' percentages.
For getting the tag statistic based on the all cases, run the getCaseNumberPerTag. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text length and words.
By updating the source file and tag_list parameter, we can get all the statistics from all the files.
3.
