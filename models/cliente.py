class cliente:
    def __init__(self, CLI_ID, CLI_UUID, CLI_PER_ID):
        self.CLI_ID     = CLI_ID
        self.CLI_UUID   = CLI_UUID
        self.CLI_PER_ID = CLI_PER_ID



    def to_dict(self):
        return{
            'CLI_ID'     : self.CLI_ID,
            'CLI_UUID'   : self.CLI_UUID,
            'CLI_PER_ID' : self.CLI_PER_ID

        }