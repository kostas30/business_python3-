
# εφαρμογή contacts v.0 χωρίς μόνιμη αποθήκευση
import os
import random

class Contact():
    ''' κλάση επαφών με όνομα και τηλέφωνο
        μια μεταβλητή κλάσης theContacts'''
    theContacts = {}
    def list_contacts(term = ''):
        for c in sorted(Contact.theContacts, key=lambda x : x.split()[-1]):
            if term:
                if term.lower() in c.lower():
                    print(Contact.theContacts[c])
            else: print(Contact.theContacts[c])

    def __init__(self, name, number=''): #  μέθοδος δημιουργός επαφών
        self.name = name.strip()
        self.number = number.strip()
        Contact.theContacts[self.name] = self
    def __repr__(self): # μέθοδος εκτύπωσης επαφών
        return self.name + ': ' + self.number

class Main():
    ''' κλάση επικοινωνίας με τον χρήστη - δημιουργία - διαγραφή επαφών'''
    def __init__(self):
        while True:
            command = input('\nΕπαφές:{}. \n[+]εισαγωγή [-]διαγραφή  [?]επισκόπηση [enter] Έξοδος.:'.\
                            format(len(Contact.theContacts)))
            if command == '': break
            elif command[0] == '?':
                Contact.list_contacts(command[1:])
            elif command[0] == '-':
                name = input('ΔΙΑΓΡΑΦΗ. Δώσε Όνομα επαφής >>>')
                try:
                    del Contact.theContacts[name.strip()]
                except KeyError : print('Επαφή με όνομα {} δεν υπάρχει'.format(name))
            elif command[0] == '+':
                contact_details = input('ΕΙΣΑΓΩΓΗ Όνομα επαφής: τηλέφωνο / πλήθος εγγραφών >>>')
                if contact_details.isdigit() and int(contact_details) < 500:
                    self.create_contacts(int(contact_details))
                elif ':' in contact_details:
                    try:
                        Contact(*contact_details.split(':'))
                    except IndexError:
                        print('Σφάλμα εισαγωγής επαφής')
                else: print('Προσοχή δώσε το όνομα, άνω-κάτω τελεία (:) τηλέφωνο')

    def create_contacts(self, size):
        '''δημιουργεί τυχαίο δείγμα επαφών - καμιά σχέση με την πραγματικότητα'''
        dir = '../myproject/data'
        act_names_files = [os.path.join(dir, x) for x in ('gr_actresses.txt', 'gr_actors.txt')]
        names = []
        for f in act_names_files:
            with open(f, 'r', encoding='utf-8') as fin:
                for name in fin:
                    if len(name) > 2:
                        if len(name.split()) > 1:
                            names.append(name.strip())
        # Select class_size names from names list
        if size < len(names):
            contact_names = random.sample(names, size)
        else:
            contact_names = names
        for contact in contact_names:
            Contact(contact, str(random.randint(6900000000,6999999999)))

if __name__ == '__main__': Main()

