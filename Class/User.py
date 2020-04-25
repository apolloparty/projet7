class User:
    
    def __init__(self, name):
        self.name = name

    def splitter(self):
        """
        Receive name and split every words to make it exploitable 
        """
        split_words = (self.name.split(' '))
        # print(entry_list)
        return split_words