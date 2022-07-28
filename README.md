# Replication package for paper "A First Look at Information Highlighting in Stack Overflow Answers", ICSME NIER track, 2022

__Preparing dataset__

1. Download the stackoverflow posts dataset from stackexchange platform
2. Import the data into the MySQL according to this link https://gist.github.com/gousiosg/7600626
3. We used Datagrip software to use the MySQL. Use MySQL commands to extract the dataset in chunks. The dataset had 52,166,061 posts where 31,169,429 answers posts. In our case, the whole dataset was divided into 11 smaller dataset. The dataset was divided into ten smaller dataset of 3,000,000 answers except the last portion.
MySQL command for fetching each chunks`SELECT * From Posts WHERE posttypeid = 2 ORDER BY Id LIMIT 1,3000000;`

***RQ1: How prevalent is the information highlighting in Stack Overflow answers?***

__Necessary changes for running the code__

1. In `RQ1_for_individual_file_individual_tag_posts.ipynb` file, update `source_file` according to the smaller dataset file path. 
2. Update the functions parameters for the expected analysis.
For getting the tag statistic based on the one post, run the getCaseNumberPerPost. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text and words' percentages.
For getting the tag statistic based on the all cases, run the getCaseNumberPerTag. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 
This will generate the dataframe containing the information on highlighted text length and words.
By updating the source file and tag_list parameter, we can get all the statistics from all the files.

__Run the ipython file__

1.To run this files, it's better to have jupyter notebook and run the cells. We had anaconda installed in our computers. Here's the link to the installation guide https://docs.anaconda.com/anaconda/install/ 
2. Install Jupyter notebook. Install the necessary packages for running the code.
3. Run each of the cells after performing necessary changes.
 
__Run the python 3 file__

_Tags per post analysis_

This portion provides analysis based on each post. For example, to get the percentage of the highlighting in a post.
1. Run `RQ_1_individual_tag_per_post.py` by updating the source file and tag parameter. 
2. Run `Combined_whole_data_per_post.py` after getting the results for whole dataset on one type of tag.


_Tags per case analysis_

This portion provides analysis of the tags and information length.
1. Run `RQ_1_for_individual_file_individual_per_tag.py` by updating the source file and tag parameter. 
2. Run `Combined_all_data_cases_per_tag.py` after getting the results for whole dataset on one type of tag.


