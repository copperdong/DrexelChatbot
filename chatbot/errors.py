
class ErrorHandler():
    def handle(ex):
        if type(ex) is BadQuestionException:
            print("Sorry I did not understand your question. I am just a bot and I am not as smart as you. Maybe someday I will be smarter and rule your world.")
        elif type(ex) is BadAnswerException:
            print("Sorry I don't have an answer for that. I could give you the link(s) to website(s) which might have the answer:")
            query = "prefix cb: <http://drexelchatbot.com/rdf/> select ?website where { ?s cb:name \"(target)\" . ?s cb:website ?website}"
            for key in ex.dictionary.keys():
                new_query = query.replace("(target)", dictionary[key])
                website = ex.db.query(new_query)[key]
                print("%s: %s" % (dictionary[key], website))
        else:
            print("I don't know what happened. I have error in my system and the programmers did not catch that error. They are not cool.")

class ChatbotException(BaseException):
    """Base class for exceptions of the Drexel Chatbot"""
    pass

class BadQuestionException(ChatbotException):
    pass

class BadAnswerException(ChatbotException):
    def __init__(self, db, dictionary):
        self.dictionary = dictionary
        self.db = db
