import time 

class Producer:

    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now!")

class Proxy:

    def __init__(self):
        self.occupied = 'No'
        self.producer = None
    
    def produce(self):
        print("Artist checking if producer is available ...")

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()
        
        else:
            time.sleep(2)
            print("Producer is busy")

p = Proxy()

p.produce()

p.occupied = 'Yes'

p.produce()