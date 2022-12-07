
# 11. Write exception handling for below code's invocation block
import time

conclude = "And what leads you to that conclusion?"
district = "Finest in the district, sir."
cheese = "It's certainly uncontaminated by cheese."
clean = "Well, it's so clean."
shop = "Not much of a cheese shop really, is it?"
cust = "Customer: "
clerk = "Shopkeeper: "


def fun(reaper):
    if reaper == 'spam':
        print('spam')
    elif reaper == 'cheese':
        print()
        print('Spam, Spam, Spam, Spam, Beautiful Spam')
    elif reaper == 'mr death':
        print()
        return('{}{}\n{}{}'.format(cust, shop, clerk, district))

def more_fun(language):
    if language == 'java':
        test = [1, 2, 3]
        test[5] = language
    elif language == 'c':
        print('{}{}\n{}{}'.format(cust, conclude, clerk, clean))

def last_fun():
    print(cust, cheese)
    time.sleep(1)
    import antigravity

# invocation code below where you need to do try,except block and
# make sure you program does not throw an exception
# rather prints with a message to the user on what went wrong and ask him to retry atleast once

first_try = ['spam', 'cheese', 'mr death']
joke = fun(first_try[0])
not_joke = fun(first_try[2])
langs = ['java', 'c', 'python']
more_joke = more_fun(langs[0])
