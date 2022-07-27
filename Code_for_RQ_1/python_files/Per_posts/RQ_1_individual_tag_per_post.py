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

# Lists only for answer analysis per post

# def getCaseNumberPerPost(filename,tag_list): returns the 7 lists of answers.

# filename: file containing the posts with ids and text body
# tag_list: contains the list of tags needed to search in the code
# returns: Answer_id_list, Answer_body, Number_of_cases, Answers_lengths, Answers_words, Highlighted_text_length, Highlighted_text_words
# This portion works on getting the number of tags and highlighting lengths of the context words.



def getCaseNumberPerPost(filename,tag_list):
    Answer_id_list = []
    Number_of_cases= []
    Answer_body = []
    Answers_lengths = []
    Answers_words = []
    Highlighted_text_length = []
    Highlighted_text_words = []
    result_dataframe = pd.read_csv(filename)  

    for index, row in result_dataframe.iterrows():
        answer_id = row['Id']
        answer_body = str(row['Body'])
        without_pre = remove_pre_tag(answer_body)
        without_tags_answer = remove_tags(without_pre)
        without_tags_answer = without_tags_answer.strip()
        text_length = len(without_tags_answer)
        word_count_ans = len(without_tags_answer.split())
        context_length = 0
        word_count = 0
        highlighted = False
        total_cases_per_post = 0

        for tag in tag_list:
            # <(?i)i>((.|\n)*?)<\/(?i)i>
            reg_str = "<(?i)" + tag + ">((.|\n)*?)<\/(?i)" + tag + ">"

            res = re.findall(reg_str, without_pre)
            # tag_count[tag]+=len(res)
            total_cases_per_post += len(res)
            if res:
                if not highlighted:
                    highlighted = True
                for i in range(len(res)):
                    # print(type(res[i]))
                    text_1 = ''
                    
                    if type(res[i]) is tuple:#this part is done due to the regular expression gets the end of the context
                        text_1 = res[i][0]
#                         print(res[i])
                    else:
                        text_1 = res[i]
                
                    tagged_text = remove_tags(text_1)
                    context_length += len(tagged_text)
                    word_count += len(tagged_text.split())
#                     print(res,text_1)
#         if total_cases_per_post > 0:
#             Answer_id_list.append(answer_id)
#             Answer_body.append(answer_body)
#             Number_of_cases.append(total_cases_per_post)
        if highlighted:
            Answer_id_list.append(answer_id)
            Answer_body.append(without_pre)
            Number_of_cases.append(total_cases_per_post)
            Answers_lengths.append(text_length)
            Answers_words.append(word_count_ans)
            Highlighted_text_length.append(context_length)
            Highlighted_text_words.append(word_count)   
            
            
            
    return Answer_id_list,Answer_body,Number_of_cases,Answers_lengths,Answers_words,Highlighted_text_length,Highlighted_text_words



Answer_body = []
Number_of_cases = []
Answers_lengths = []
Answers_words = []
Answer_id_list = []
Highlighted_text_length = []
Highlighted_text_words = []





Answer_id_list,Answer_body,Number_of_cases,Answers_lengths,Answers_words,Highlighted_text_length,Highlighted_text_words = getCaseNumberPerPost(source_file,tag_list_delete)

dataframe_html = pd.DataFrame({'Answer_ID': Answer_id_list,
                               'Answer_Body': Answer_body,
                               'Number_of_cases': Number_of_cases,
                               'Answers_lengths': Answers_lengths,
                               'Answers_words': Answers_words,
                               'Highlighted_text_length': Highlighted_text_length,
                               'Highlighted_text_words': Highlighted_text_words
    })





dataframe_html.count()




mean_of_html = dataframe_html['Number_of_cases'].mean()
median_of_html = dataframe_html['Number_of_cases'].median()
maximum_of_html = dataframe_html['Number_of_cases'].max()
print('Mean ' + str(mean_of_html) + "\n Median " + str(median_of_html) + "\n Maximum " + str(maximum_of_html))





dataframe_html['Highlighted_text_percentage'] = numpy.where(dataframe_html['Highlighted_text_length'] < 1, 0, dataframe_html['Highlighted_text_length']/dataframe_html['Answers_lengths']*100)
dataframe_html['Highlighted_word_percentage'] = numpy.where(dataframe_html['Highlighted_text_words'] < 1, 0, dataframe_html['Highlighted_text_words']/dataframe_html['Answers_words']*100)





mean_of_h_word = dataframe_html['Highlighted_word_percentage'].mean()
median_of_h_word = dataframe_html['Highlighted_word_percentage'].median()
maximum_of_h_word = dataframe_html['Highlighted_word_percentage'].max()
print('Mean ' + str(mean_of_h_word) + "\n Median " + str(median_of_h_word) + "\n Maximum " + str(maximum_of_h_word))





dataframe_html.to_csv('/home/shahla/ProjectWorkHTML/Posts_csv_files/Delete/last_3M_per_posts_heading_body.csv')