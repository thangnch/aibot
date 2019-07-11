# Imports
#-----------
# rasa nlu
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

# Functions
#------------
def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

# Training
#------------
train('data/nlu.md', 'config/config.yml', 'models/nlu')

# loading the interpreter
interpreter = Interpreter.load('./models/nlu/default/chat')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))

# asking question
ask_question("Em tên gì")
ask_question("Chị muốn mở tài khoản bên em có được không")
ask_question("###")
ask_question("Không")
ask_question("Lãi suất sao rồi")
ask_question("Có hỏi được không đấy")
ask_question("Có ai không")
ask_question("Cảm ơn em nhé")
ask_question("thanks nhá")
ask_question("Tôi không là Thắng")