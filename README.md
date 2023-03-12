# Replication package for paper "A First Look at Information Highlighting in Stack Overflow Answers"

__Preparing dataset__

1. Download the stackoverflow posts dataset `stackoverflow.com-Posts.7z` from stackexchange platform https://archive.org/details/stackexchange
2. Import the data into the MySQL according to this link https://gist.github.com/gousiosg/7600626
3. We used Datagrip software to use the MySQL. Use MySQL commands to extract the dataset in chunks. The dataset had 52,166,061 posts where 31,169,429 answers posts. In our case, the whole dataset was divided into 11 smaller datasets. The dataset was divided into ten smaller datasets of 3,000,000 answers except for the last portion.
MySQL command for fetching each chunks`SELECT * From Posts WHERE posttypeid = 2 ORDER BY Id LIMIT 1,3000000;`

***RQ1: How prevalent is the information highlighting in Stack Overflow answers?***

__Necessary changes for running the code__

1. In `RQ1_for_individual_file_individual_tag_posts.ipynb` file, update `source_file` according to the smaller dataset file path. 
2. Update the function parameters for the expected analysis. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold".
3. Please update the second parameter based on the expected statistic. For example, if we want to find out statistics about bold tags, we will update the second parameter "tag_list_bold". 

By updating the source file and tag_list parameter, we can get all the statistics from all the files.
4. For running the `Combined_all_data_cases_per_tag.ipynb` and `Combined_whole_data_per_post.ipynb` files, change the file path into the folder where the csv files of one type of tag is stored(result dataframes of the`RQ1_for_individual_file_individual_tag_posts.ipynb` file)

__Run the ipython file__

1. To run these files, it's better to have jupyter notebook and run the cells. We had anaconda installed in our computers. Here's the link to the installation guide https://docs.anaconda.com/anaconda/install/ 
2. Install Jupyter notebook. Necessary packages for the code :- Pandas, Numpy, Regex, Glob, OS
3. Run the `RQ1_for_individual_file_individual_tag_posts.ipynb` file for generating the csv files for smaller datasets.
_Tags per post analysis :_ For getting the tag statistic based on one post, run the getCaseNumberPerPost. This will generate the dataframe containing the information on highlighted text and words' percentages. 
_Tags per case analysis :_ For getting the tag statistic based on all cases, run the getCaseNumberPerTag. This will generate the dataframe containing the information on highlighted text length and words.
4. Run the cells in `Combined_whole_data_per_post.ipynb` after getting the results for the whole dataset on one type of tag per post.
5. Run the cells in `Combined_all_data_cases_per_tag.py` after getting the results for the whole dataset on one type of tag per case.
 
__Run the python 3 file__

_Tags per post analysis_

This portion provides an analysis based on each post. For example, to get the percentage of the highlighting in a post.

1. Perform the necessary changes in the code(filepath and tagtype).
2. Run `RQ_1_individual_tag_per_post.py` for each type of tags and every smaller dataset. 
3. Run `Combined_whole_data_per_post.py` after getting the results for the whole dataset on one type of tag per post.


_Tags per case analysis_

This portion provides an analysis of the tags and information length.

1. Perform the necessary changes in the code(filepath and tagtype).
2. Run `RQ_1_for_individual_file_individual_per_tag.py` for each type of tags and every smaller dataset.
3. Run `Combined_all_data_cases_per_tag.py` after getting the results for the whole dataset on one type of tag per case.


***RQ4: Can we recommend the highlighted content in SO answers automatically?***
Under the codes for RQ4 there are three folders; Create dataset, Evaluation and Model. 
Create dataset: In the 'Create_BOE_tagged_csv_file.ipynb' file, update the formatting tags, start_tags and end tags with the expected tags for the model. This code helps to create the word and tag dataset. 'Combine_all_csv_files.py' combines all the individual files created from 'Create_BOE_tagged_csv_file.ipynb' file and creates train and test dataset. Then using 'CoNLL_tsv_to_json.py' and 'Json_to_pickle_file.py' help creating json and pickle train and test files. On the other hand, 'CoNLL_words_to_sentences.py' file creates csv files of train and test files for better readability. 
'Ner_model.py' is the main file for traing the model. Change the labels to expected tags for training.
'NER_Confusion_matrix.py' makes confusion matrix for the test dataset. 'Ner_evaluation_example.py' is used for checking the evaluating some texts for evaluating models.
