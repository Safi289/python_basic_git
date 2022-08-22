import time


class Topic:
    def data_log(self, topic_name):
        seconds = time.time()
        local_time = time.ctime(seconds)
        print(f"Log: '{topic_name}' is searched in {local_time}")

    def abc(self):
        learned_topics = ['classes', 'constructor', 'inheritance', 'modules']
        return learned_topics


class LearnedTopics(Topic):

    def search(self, topic_name):
        matrix = self.abc()
        count = 0
        for row in matrix:
            if topic_name in row:
                print(f"Topic Full Name: {row}")
                count = 1
        if count == 0:
            print("No match found!")
