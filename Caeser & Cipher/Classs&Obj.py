import logging


class car:
    # class constructor
    def __init__(self, name, year_of_manufacturing, mielage, model, safety_rating):
        self.Name = name
        self.yof = year_of_manufacturing
        self.Milage = mielage
        self.Model = model
        self.SR = safety_rating

    def age(self, current_year):
        return current_year - self.yof


call = car('TATA', 2019, 21.56, 'Nexon', '5- Star')

print(call.Name, call.Model, call.yof, call.SR)

print(call.age(2022))

# Start Logging and then continue further class have to improve in writing production level code.

logging.basicConfig(filename='test1.log', level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
# perform stream handling
consol_log = logging.StreamHandler()
consol_log.setLevel(logging.INFO)  # if we provide logging level as warning it will show the data of warning and above
# as we define
# Logging.Formatter is used to show the suers logging information to the application.
form = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
consol_log.setFormatter(form)

logging.getLogger().addHandler(consol_log)

logging.debug('This is my first test code for log')
# these steps help the user to get the details from where the log is generated and trace the location.

logger1 = logging.getLogger('Anywhere from data base')
logger2 = logging.getLogger('logger2.area2')

logger3 = logging.getLogger('user3')
logger4 = logging.getLogger('user4')

# this is how it is called for various purpose

logger1.info('this is ifo for logger one')
logger2.debug('this is debug for log 2')
logger2.info('this is a info for log two')
logger3.warning('this is test warning')
logger4.error('this is test error')
logging.warning('this for test')


