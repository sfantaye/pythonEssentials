
def preprocess(sentence):
    word_list = sentence.lower().strip().split()
    return word_list

def count_words(key, word_list):
    counter = 0
    for word in word_list:
        if key == word:
            counter += 1
    return counter


def print_word_count(sentence):
    word_list = preprocess(sentence)
    word = input("Enter any word: ")

    word_count = count_words(word, word_list)

    if word_count == 0:
        print("No such a word in the text")
    elif word_count == 1:
        print("The word \"" + word + "\" has " + str(word_count) + " occurence in the text")
    else:
        print("The word \"" + word + "\" has " + str(word_count) + " occurences in the text")



text = """In our increasingly data-drive world, the transformative potential of converting raw data into 
actionable insights has become a cornerstone of informed decision-making. This report 
undertakes a comprehensive exploration of predictive analysis—an integral subset of data 
analytics that harnesses the power of statistical algorithms and machine learning techniques to 
anticipate future outcomes based on historical data patterns. This tool operates at the intersection 
of technology and business, reshaping the landscape of strategic decision-making for 
organizations across diverse sectors.
At its core, predictive analysis is more than a technical process; it's a strategic endeavor that 
involves uncovering meaningful connections within vast datasets. By extrapolating from 
historical data, this method goes beyond descriptive analysis to foresee potential future trends, 
empowering organizations to proactively address challenges and seize opportunities. From 
finance and healthcare to marketing and logistics, the applications of predictive analysis are farreaching, offering a versatile lens through which to optimize operations and drive innovation.
This report navigates the intricacies of predictive analysis, dissecting the methodologies and 
techniques that underpin its functionality. From understanding the nuances of statistical 
algorithms to exploring the realm of machine learning, we peel back the layers to reveal how 
predictive analysis transforms seemingly disparate data points into coherent and valuable 
insights. The exploration extends beyond mere technicalities, delving into the ethical 
considerations, challenges, and opportunities that accompany the integration of predictive 
analysis into organizational workflows.
Predictive analysis isn't just a buzzword; it's a game-changer in the realm of strategic decisionmaking. Organizations leveraging predictive analysis gain a competitive edge by foreseeing 
trends, mitigating risks, and optimizing resource allocation. Through real-world case studies and 
examples, this report illustrates how predictive analysis isn't confined to theoretical concepts; 
rather, it translates into tangible benefits that inform high-stakes decisions, shaping the 
trajectories of businesses and industries"""



print_word_count(text)