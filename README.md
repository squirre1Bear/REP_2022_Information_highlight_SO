# Replication package for paper "A First Look at Information Highlighting in Stack Overflow Answers", ICSME NIER track, 2022

_Preparing dataset_
1. Download the stackoverflow posts dataset from stackexchange platform and import it in stack overflow 
2. Use MySQL commands to extract the dataset in chunks. The dataset had 52,166,061 posts where 31,169,429 answers posts. The dataset was divided into ten smaller dataset of 3,000,000 answers except the last portion.
MySQL command for fetching each chunks`SELECT * From Posts WHERE posttypeid = 2 ORDER BY Id LIMIT 1,3000000;`

***RQ1: How prevalent is the information highlighting in Stack Overflow answers?***

__Run the ipython file__
 To run this files, it's better to have jupyter notebook and run the cells.
__Run the python 3 file__
Tags per post analysis
1. Run `RQ_1_individual_tag_per_post.py` by updating the source file and tag parameter. 
2. Run `Combined_whole_data_per_post.py` after getting the results for whole dataset on one type of tag.
Tags per case analysis
1. Run `RQ_1_for_individual_file_individual_per_tag.py` by updating the source file and tag parameter. 
2. Run `Combined_all_data_cases_per_tag.py` after getting the results for whole dataset on one type of tag.


_Necessary changes for running the code_
1. In __"RQ1_for_individual_file_individual_tag_posts"__ file, update `source_file` according to the smaller dataset file path. 
2. Update the functions parameters for the expected analysis.
For getting the tag statistic based on the one post, run the getCaseNumberPerPost. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text and words' percentages.
For getting the tag statistic based on the all cases, run the getCaseNumberPerTag. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text length and words.
By updating the source file and tag_list parameter, we can get all the statistics from all the files.
