#Write a program that searches through a series of product reviews for keywords such 
# as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", 
            "The performance of this product is excellent. Highly recommended!", 
            "I had a bad experience with this product. It didn't meet my expectations.", 
            "Poor quality product. Wouldn't recommend it to anyone.", 
            "The product was average. Nothing extraordinary about it." ]


review_words = ["good", "excellent", "bad", "poor", "average"]
for sentence in reviews:
    review = sentence.split()
    new_review = []
    for word in review:
        word_strip = word.strip(".")
        if word_strip.lower() in review_words:
            new_review.append(word.upper())
        else:
            new_review.append(word)     
    print(" ".join(new_review))




#Task 2: Sentiment Tally


#Develop a function that tallies the number of positive and negative words in each review. 
#Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def count_sentiment(review):
    positive_count = 0
    negative_count = 0
    
    # Split the review into words
    words = review.split()
    
    # Iterate through each word
    for word in words:
        # Check if the word is in the positive words list
        if word.lower() in positive_words:
            positive_count += 1
        # Check if the word is in the negative words list
        elif word.lower() in negative_words:
            negative_count += 1
            
    return positive_count, negative_count
print()




def pos_and_neg_count ():
    number_of_positive = 0
    number_of_negative = 0
    for sentence in reviews: 
        for word in sentence.split():
            word = word. replace(".", "") 
            if word.lower() in positive_words:
                number_of_positive += 1
                    
    print(f" The number of positives are {number_of_positive}.")
    
    for sentence in reviews: 
        for word in sentence.split():
            word = word. replace("•", "") 
            if word.lower() in negative_words: 
                number_of_negative += 1
    print(f" The number of negatives are {number_of_negative}.")

pos_and_neg_count()



#Task 3: Review Summary
#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

def create_summary(review):
    if len(review) <= 30:
        return review
    else:
        summary = review[:30]
        last_space_index = summary.rfind(' ') #search string from right to left for space
        if last_space_index != -1:
            summary = summary[:last_space_index]
        return summary + "..."

# Create summaries for all reviews
summary_reviews = [create_summary(review) for review in reviews]

# Print summary reviews
for summary in summary_reviews:
    print(summary)


#User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.
# ask 1: Input Length Validator Write a script that checks the length of the user's first name
# and last name. Both should be at least 2 characters long. If not, print an error message.

#ask for name
full_name = str(input("What is your first and last name? "))
#error message if both names not >2 characters
name = full_name.split()
if len(name) < 2 or any(len(names) <2 for names in name):
    print("Error: Please enter at least 2 characters for each name")
#get total # of characters
else:
    total_characters = len(full_name)
#count spaces
space_count = full_name.count(" ")
#subtract spaces from total character count
character_count = total_characters - space_count
#print total count of characters
print("Character count (excluding spaces):", character_count)


