#! usr/bin/env python
# -*- coding: utf-8 -*-

"""Notes about the program:

- I wasn't sure how the objects would be passed, so I focused on the Console
and instead initialized an object for testing here in the class and gave it a few attributes

- The class is easily extendable. Any function can be added as long as it follows the
correct format as the user input is disected into pieces.

- Any object can be used. The functions search for the member name and retrieve it's value
from the object.

- When setting a value, if the new value is not the same type as the old value, an error
is displayed

- If user should mix up GET and SET and use the = sign in GET, an error message is displayed
but program does not crash

- Error message displayed if false command is entered

- I believe my main function is too cluttered, and could be broken into more functions
"""

class CommandConsole(object):
    '''This class allows for editing of a particular object
    Since it is an editing class, it should only need two functions:
    - Get and Set of the various members
    '''
    
    def __init__(self):
        self.propertyname = 'test_propertyname'
        self.id_number = 00000
        self.color = 'red'

        
    def set_member_value(self, obj, member, value):
        original_type = type(vars(obj)[member])
        try:
            val = int(value)
        except ValueError:
            val = value
        new_type = type(val)
        
        #If value is not same type as old value, value will not be changed.
        #ex. Old propertyname is string, so new propertyname must be string
        
        if new_type != original_type:
            print("Entered value not compatible. (i.e. member should be a string and int was entered, or vice versa)")
            return
        vars(obj)[member] = val
        print("{0} changed to {1}".format(member, val))
        return


    def get_member_value(self, obj, member):
        #Prints the member and current value
        print('{0}: {1}'.format(member, vars(obj)[member]))
        return


        
def main():
    print("\n\nObject Editing Console: Commands are SET and GET. To see all members -> GET *\n\n")
    obj = CommandConsole()
    functions = {'set_member_value':obj.set_member_value, 'get_member_value':obj.get_member_value}
    while(True):
        '''Ctrl-C to Stop'''
        entry = input("Enter Command$ ")
            
        if entry.lower() == 'get *' : #print all the members for the object with values
            variables = vars(obj)
            print('\n')
            
            for v in variables:
                print('{0}: {1}'.format(v, variables[v]))
            print('\n')
            
        else: #Entered command is anything but 'GET *'
            command = entry.split(' ') #Retrieve command from entry
            desired_func = command[0].lower()

            #Error message displayed if false command is entered
            if desired_func+'_member_value' not in functions:
                print("{} Command does not exist".format(desired_func))
                continue

            #if function set, new value is retrieved and set to desired_value variable
            second_half = command[1].split('=') #Preventing any key errors if SET and GET are used incorrectly with =
            
            if desired_func == 'set':
                desired_member = second_half[0]
                desired_value = second_half[1]
                functions[desired_func+'_member_value'](obj, desired_member, desired_value)
                
            else:
                desired_member = second_half[0]
                functions[desired_func+'_member_value'](obj, desired_member)
                try:
                    if second_half[1]:
                        print("You entered an '=' perhaps you meant the 'SET' command\nThe format is 'SET member=value'")
                except:
                    IndexError

if __name__ == '__main__':
    main()
    
            
            
    
