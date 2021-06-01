class IOHandler:
    def __init__(self):
        self.command_dict = {
            'new':self.newCharParse,
            'save':self.saveCharParse,
            'update':self.updateCharParse,
            'info':self.infoCharParse,
            'player':self.playerActionParse,
            'battle':self.battleParse
        }

    def getInput(self):
        raw_data = input("Command: ")
        raw_data = raw_data.split()
        command = None
        payload = None

        try:
            command, payload = self.command_dict.get(raw_data[0])(raw_data)
        except:
            print("Invalid command")

        return (command, payload)

    # syntax: new [charname] <mainclass> <subclass>
    def newCharParse(self, raw_data):
        command = None
        payload = None

        try:
            name = raw_data[1]
            jobclass = 'Warrior'
            subclass = 'Warrior'
            if len(raw_data) >= 3:
                jobclass = raw_data[2]

                if len(raw_data) >= 4:
                    subclass = raw_data[3]
                else:
                    subclass = raw_data[2]
            command = "newPlayer"
            payload = [name, jobclass, subclass]
        except IndexError:
            print("Insufficient number of arguments")
            command = None
            payload = None
        except:
            print("Unknown exception")
            command = None
            payload = None

        return command, payload

    # syntax: save
    def saveCharParse(self, raw_data):
        command = "savePlayerInfo"
        payload = None
        return command, payload

    # syntax: update [playername] class [mainclass] [subclass]
    # syntax: update [playername] statpoints [HP] [STR] [MAG] [DEF] [RES] [SPD]
    # syntax: update [playername] name [newname]
    def updateCharParse(self, raw_data):
        command = None
        payload = None

        try:
            name = raw_data[1]

            if raw_data[2] == "class":
                command = "updatePlayerClass"
                payload = [name, raw_data[3], raw_data[4]]
            elif raw_data[2] == "statpoints":
                command = "updatePlayerStatPoints"
                statPoints = [raw_data[3], raw_data[4], raw_data[5], raw_data[6], raw_data[7], raw_data[8]]
                statPoints = list(map(int, statPoints))
                payload = [name, statPoints]
            elif raw_data[2] == "name":
                command = "updatePlayerName"
                payload = [name, raw_data[3]]
            else:
                print("Invalid argument")
        except IndexError:
            print("Insufficient number of arguments")
            command = None
            payload = None
        except TypeError:
            print("Integers must be used for stat point allocation")
            command = None
            payload = None
        except:
            print("Unknown exception")
            command = None
            payload = None
        

        return command, payload

    #syntax: info [playername]
    def infoCharParse(self, raw_data):
        command = None
        payload = None

        try:
            command = "displayPlayerInfo"
            payload = raw_data[1]
        except IndexError:
            print("Insufficient number of arguments")
            command = None
            payload = None

        return command, payload

    def playerActionParse(self, raw_data):
        pass

    def battleParse(self, raw_data):
        pass