import re
import long_responses as long
import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sorry! I didn't understand that....",
                "Sorry!, I don't have answer for that. ",
                "What does that mean?"][
        random.randrange(4)]
    return response    


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(Assistant_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[Assistant_response] = message_probability(message, list_of_words, single_response, required_words)

    


    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hii', 'hey', 'sup', 'heyo'], single_response=True)
    response('Have a bright morning ma\'am!\nHow can I help you?', ['good','morning'], required_words=['morning'])
    response('Good Afternoon ma\'am!!\nHow can I help you?', ['good','afternoon'], required_words=['afternoon'])
    response('Good evening ma\'am!!\nHow can I help you?', ['good','evening'], required_words=['evening'])
    response('I\'m your AI assistant ma\'am, how can I help you?', ['what','What','is','your','name','Who','who','are','you','?'], single_response=True)
    response('See you, Stay healthy!!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('How can I help you?', ['I','i','am','fine'],single_response= True)
    response('India got independence on 15 August, 1947',['can','you','tell','me','please''when','When','did','India','got','independece','?'],single_response= True)

    # Longer responses
    #response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Assistant: ' + get_response(input('You: ')))
    
    
        

