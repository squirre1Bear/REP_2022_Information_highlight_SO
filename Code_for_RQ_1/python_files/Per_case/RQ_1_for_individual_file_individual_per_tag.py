
import pandas as pd
import numpy
import re

# def remove_tags(text): returns the texts without tags

# This portion works for removing the tags from the texts. arguement: takes the text where the tags are present and replaces it with ' ' (blank space)
def remove_tags(text):
    Tag_first = re.compile(r'<[^\/>]+>') # regex to removes the starting tag of the html.
    Tag_end = re.compile(r'<[^>]+>') # regex to removes the ending tag of the html
    without_first_tag = Tag_first.sub('',text) # Removes the first tag
    return Tag_end.sub(' ', without_first_tag) # removes the second tag after removing the first one

# def remove_pre_tag(text): returns the texts without code portion to the code

# Removes the pre code block from the posts. 


def remove_pre_tag(text):
    Tag_pre = re.compile(r'<pre([^>]+)?>((.|\n)*?)<\/pre>')
    return Tag_pre.sub('',text)


# def getCaseNumbersPerTag(filename,tag_list): returns the 5 lists of answers.

# filename: file containing the posts with ids and text body
# tag_list: contains the list of tags needed to search in the code
# returns: Answer_id_list,Context_body,Type_of_HTML_tag,Highlighted_text_length,Highlighted_text_words
# This portion works on getting the each cases of tagged text and highlighting lengths of the context words.



def getCaseNumbersPerTag(filename,tag_list):
    
    Answer_id_list = []
    Type_of_HTML_tag = []
    Context_body = []
    Highlighted_text_length = []
    Highlighted_text_words = []
    result_dataframe = pd.read_csv(filename)  

    for index, row in result_dataframe.iterrows():
        answer_id = row['Id']
        answer_body = str(row['Body'])
        without_pre = remove_pre_tag(answer_body)
        context_length = 0
        word_count = 0

        for tag in tag_list:
            # <(?i)i>((.|\n)*?)<\/(?i)i>
            reg_str = "<(?i)" + tag + ">((.|\n)*?)<\/(?i)" + tag + ">"

            res = re.findall(reg_str, without_pre)
            # tag_count[tag]+=len(res)
#             total_cases_per_post += len(res)
            if res:
                for i in range(len(res)):
                    text_1 = ''

                    if type(res[i]) is tuple:#this part is done due to the regular expression gets the end of the context
                        text_1 = res[i][0]
                #                         print(res[i])
                    else:
                        text_1 = res[i]
                    
                    tagged_text = remove_tags(text_1)
                    context_length = len(tagged_text)
                    word_count = len(tagged_text.split())
                    Answer_id_list.append(answer_id)
                    Context_body.append(text_1)
                    Type_of_HTML_tag.append(tag)
                    Highlighted_text_length.append(context_length)
                    Highlighted_text_words.append(word_count)
                    
    return Answer_id_list,Context_body,Type_of_HTML_tag,Highlighted_text_length,Highlighted_text_words




# Lists for getting cases per tag values

Context_body = []
Type_of_HTML_tag = []
Answer_id_list = []
Highlighted_text_length = []
Highlighted_text_words = []
tag_list_bold = ['b','strong']
tag_list_code = ['code']
tag_list_heading = ['h1','h2','h3','h4','h5','h6']
tag_list_italic = ['em','i']
tag_list_delete = ['del','s']
tag_list_all = ['b','strong','code','h1','h2','h3','h4','h5','h6','em','i','del','s']

source_file = '/home/shahla/ProjectWorkHTML/Posts_csv_files/AllPosts/_SELECT_FROM_PostREGEXP_1_s_last.csv'




Answer_id_list,Context_body,Type_of_HTML_tag,Highlighted_text_length,Highlighted_text_words = getCaseNumbersPerTag(source_file,tag_list_delete)

dataframe_html = pd.DataFrame({'Answer_ID': Answer_id_list,
                               'Context_body': Context_body,
                               'Type_of_HTML_tag': Type_of_HTML_tag,
                               'Highlighted_text_length': Highlighted_text_length,
                               'Highlighted_text_words': Highlighted_text_words
    })




mean_of_characters = dataframe_html['Highlighted_text_length'].mean()
median_of_characters = dataframe_html['Highlighted_text_length'].median()
maximum_of_characters = dataframe_html['Highlighted_text_length'].max()
mean_of_word_count = dataframe_html['Highlighted_text_words'].mean()
median_of_word_count = dataframe_html['Highlighted_text_words'].median()
maximum_of_word_count = dataframe_html['Highlighted_text_words'].max()
print('Mean ' + str(mean_of_characters) + " Median " + str(median_of_characters) + " Maximum " + str(maximum_of_characters))
print('Mean ' + str(mean_of_word_count) + " Median " + str(median_of_word_count) + " Maximum " + str(maximum_of_word_count))




print(dataframe_html['Highlighted_text_length'].idxmax())
print(dataframe_html['Highlighted_text_words'].idxmax())



dataframe_html.count()


dataframe_html.to_csv('/home/shahla/ProjectWorkHTML/Posts_csv_files/Delete/last_3M_per_tags_heading_body.csv')












