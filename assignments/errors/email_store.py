class EmailStore:

    def __init__(self):
        '''
        Constructor method.
        '''
        self.emails = []

    def exists(self, email):
        '''
        Method that checks if an email exists in store.
        '''
        return email in self.emails

    def add(self, first_name, last_name):
        '''
        Method that adds a new email to the store.
        The email address is of the format {first_name}.{last_name}{count}@marist.edu

        @return the email that was added.
        '''
        email = None

        if first_name == None or last_name == None:
            raise Exception("'first_name' or 'last_name' may not be None.")

        count = 1
        while True:
            # generate the email.
            email = f"{first_name.lower()}.{last_name.lower()}{count}@marist.edu"
            # check to see if it exists.
            if self.exists(email):
                count += 1
                continue
            break

        self.emails.append(email)

        return email

    def remove(self, email):
        '''
        Method that removes an email from the store.
        '''
        # TODO if email doesn't exist, raise an exception.
        if not self.exists(email):
            raise Exception("Email does not exist")   
        self.emails.remove(email)
