class IOHandler:
    def __init__(self):
        self.command_dict = {
            'new':self.newCharParse,
            'save':self.saveCharParse
        }

    def getInput(self):
        raw_data = input("Command: ")
        raw_data = raw_data.split()
        command = None
        payload = None

        if(raw_data[0] in self.command_dict):
            command, payload = self.command_dict.get(raw_data[0])(raw_data)
        else:
            print("Invalid command")

        return (command, payload)

    def newCharParse(self, raw_data):
        command = None
        payload = None

        if len(raw_data) < 2:
            command = "argNumLow"
        else:
            name = raw_data[1]
            jobclass = 'Warrior'
            subclass = 'Warrior'
            if len(raw_data) >= 4:
                jobclass = raw_data[2]
                subclass = raw_data[3]
            command = "newPlayer"
            payload = [name, jobclass, subclass]

        return command, payload

    def saveCharParse(self, raw_data):
        command = "savePlayerInfo"
        payload = None
        return command, payload