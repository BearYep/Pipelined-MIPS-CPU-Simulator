class ID:
    def __init__(self):
        pass

    def run(self, IF_ID):
        if IF_ID:
            self.ID_EX = IF_ID
        else:
            self.ID_EX = None

        print(f"ID stage... {self.ID_EX}")
        return self.ID_EX