from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import math
 
def sentiment_scores(sentence):

    s_obj = SentimentIntensityAnalyzer()    
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = s_obj.polarity_scores(sentence) 
    print("Sentiment Dictionary = ",sentiment_dict)
    print("\nSentence Overall Rated As", end = " ")
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
    else :
        print("Neutral")
    
    return sentiment_dict['compound']


if __name__ == "__main__" :
    
    while True:
    
        print("Main Menu \n 1.Custom Input \n 2.Predefined input \n 3.Exit")
        x =int(input("Enter your choice :"))     

        if x==1:
            sentence = input("Enter Sentence :")
        elif x==2:
           sentence = "NLP is a good subject." 
        elif x==3:
            break 
    
        print("Sentence = ",sentence,"\n")
        compound=sentiment_scores(sentence)
        valence=math.sqrt(math.pow(compound,2)*15/(1-math.pow(compound,2)))
    
        if compound <= -0.05:
         print("\nSum of all the Valence Score : ",-valence)  
        elif compound >= 0.05:
         print("\nSum of all the Valence Score : ",valence)
    
    