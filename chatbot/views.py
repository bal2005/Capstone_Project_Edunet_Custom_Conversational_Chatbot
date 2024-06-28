from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,logic_adapters=[
    {
    
   'import_path': 'chatterbot.logic.BestMatch'
   #'default_response' : 'Sorry,I dont know what that means',
   #'maximum_similarity_threshold':0.90

    }
    ])

list_to_train = [

    "Hi", #Question
    "Hello There!", #Response
    "What is your name?",
    "My name is Nova",
    "Who is your father?",
    "I'm a custom built chatbot",
    "Tell me a joke",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What is the largest planet in our solar system?",
    "Jupiter",
    "Who wrote 'Romeo and Juliet'?",
    "William Shakespeare",
    "What is the powerhouse of the cell?",
    "Mitochondria",
    "Who painted the Mona Lisa?",
    "Leonardo da Vinci",
    "What is H2O commonly known as?",
    "Water",
    "Who developed the theory of relativity?",
    "Albert Einstein",
    "What is the capital of France?",
    "Paris",
    "Who discovered penicillin?",
    "Alexander Fleming",
    "What year did the Titanic sink?",
    "1912",
    "Who was the first person to step on the moon?",
    "Neil Armstrong",
    "What is the speed of light in a vacuum?",
    "299,792,458 meters per second",
    "What is the chemical symbol for gold?",
    "Au",
    "Who painted the ceiling of the Sistine Chapel?",
    "Michelangelo",
    "What is the largest organ in the human body?",
    "Skin",
    "What is the smallest bone in the human body?",
    "Stapes (in the ear)",
    "Who is known as the 'Father of Modern Physics'?",
    "Albert Einstein",
    "What is the study of earthquakes called?",
    "Seismology",
    "Who developed the first successful polio vaccine?",
    "Jonas Salk",
    "What is the only planet known to support life?",
    "Earth",
    "Who proposed the heliocentric model of the solar system?",
    "Nicolaus Copernicus",
    "What is the chemical formula for table salt?",
    "NaCl",
    "Who wrote 'The Canterbury Tales'?",
    "Geoffrey Chaucer",
    "What is the longest river in the world?",
    "Nile River",
    "Who discovered the law of gravity?",
    "Isaac Newton",
    "What is the hardest natural substance on Earth?",
    "Diamond",
    "Who painted 'Starry Night'?",
    "Vincent van Gogh",
    
]
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterBotCorpusTrainer=ChatterBotCorpusTrainer(bot)
chatterBotCorpusTrainer.train('chatterbot.corpus.english')
def index(request):
    return render(request,'chatbot/index.html')
def specific(request):
    return HttpResponse("specific")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)


    
