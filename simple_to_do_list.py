# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:26:08 2024

@author: Abimbola_diya
"""
from datetime import datetime
dict_tabs={}
current=datetime.now()

print('\n..........Welcome to the to do list app :)..............')
while True:
    print('\nWhat would you like to do? ,to make it easier\n')
    print('Please select one of the following options')
    print('-------------------------------------------------')
    print('0. Create a new tab')
    print('1. Add a task to a newly created tab')
    print('2. Delete a task from any tab')
    print('3. shows all tabs in the to_do_list and can display items in any tab')
    print('4. Add item to a  current tab in the to-do-list ')
    print('5.sort items in any tab alphabetically or in reverse order')
    print('6. quit')
    
    print('\n---------------------------------------------------------------')
    choice=((input('Enter your choice : ')).strip()).lower()

    if choice=='0':
        print('------This option creates a new Tab-------------\n ')
        print('\nit allows you to streamline your to To-do-list/goal book to a specific topic')
        name=((input('what do you want this Tab to be called ? : ')).strip()).lower()
        if name in dict_tabs.keys():
            print('\n....Try creating the tab with another name,tab name taken......')
        else:
            t_date=datetime.now()
            print('\n--------------{}----------------'.format(name.upper()))
            print('\tTab successfully created on {} '.format(str(t_date)))
            dict_tabs[name]=[]
            print('\npick option 1 to add items to your newly created tab')
        


    elif choice=='1':
        r_name=((input('\nKindly enter the name of the tab you want to add items to:')).strip()).lower()
        if r_name in dict_tabs.keys() :
            message=((input('Enter the items you will like to add to this tab ! : ')).strip()).lower()
            lis=message.split(',')
            for riz in lis :
                dict_tabs[r_name].append(riz.title())
            print('------------{}------------'.format(name.title())) 
            for index,item in enumerate(dict_tabs[r_name]):
                print('\n{}{}'.format((str(index)+'.'),item))
        else:
            print('\n\tThe tab you are trying to add items to does not exist !!!!')
            
            
    elif choice=='2':
        print('\nyou can delete a task  from a specific tab after it is accomplished by specifying'+
              ' its index number\n')
        tab_name=((input('Enter the name of the Tab :')).strip()).lower()
        if tab_name in dict_tabs.keys() and dict_tabs[tab_name]:
            for number,elements in enumerate(dict_tabs[tab_name]):
                print('{}{}'.format((str(number)+'.'),elements))
            numb=input('\nEnter the index number of the item you want to delete : ')
            
            if 0<=int(numb)<=len(dict_tabs[tab_name]):
                del (dict_tabs[tab_name])[int(numb)]
                print('\nThe item has been removed congratulation on completing'+
                     'task🎉🎉🎊..........................')
                print('last edited :{}'.format(datetime.now().time()))
                print('The new edited tab at {} is------------------------ : ')
                for ber,dex in enumerate(dict_tabs[tab_name]):
                    print('{}{}'.format((str(ber)+'.'),dex))

            else:
                print('index is out of range')
        else:
            print('{} name does not exist'.format(tab_name))
            
        
        
    elif choice=='3':
        print('The current tabs in your to-do list are: .....')
        for tabs,val in dict_tabs.items():
            print('---------'+tabs.title()+'------------')
            for disp in val :
                print(disp.title())

    elif choice=='4':
        print('----------This is to add an item to a current tab---------- ')
        t_name=((input('\nKindly Enter the tab name you0 want to add an item to :')).strip()).lower()
        tems=((input('Enter the items you will like to add to the specfied tab : ')).strip()).lower()
        tem=tems.split(',')
        if dict_tabs[t_name] :
            for any in tem:
                dict_tabs[t_name].append(any)
            print('\n.....Item successfully added to {} tab on {}.....'.format(t_name,datetime.now().time()))
            for sec,deg in enumerate(dict_tabs[t_name]):
                print('{}{}'.format((str(sec)+'.'),deg))

        else :
            print('you cannot add more items to a newly creted tab ')
            
    elif choice=='5':
        print('\nThis sorts a tab alphabetical or in reverse order')
        sort_name=((input('Enter the tab you would like to sort : ')).strip()).lower()
        for ny,vals in enumerate(dict_tabs[sort_name]):
            print('{}{}'.format((str(ny)+'. '),(vals.title())))
        order=(input('\nin what order would you like to sort the items (alphabetical/reverse-alphabetical) :')).strip()
        if order.lower()=='alphabetical':
            dict_tabs[sort_name].sort()
            print('\n..........This is the new sorted Tab...........')
            for quarks,leptons in enumerate(dict_tabs[sort_name]):
                print('{}{}'.format((str(quarks)+'. '),(leptons.title())))
        if order.lower()=='reverse':
            dict_tabs[sort_name].sort(reverse=True)
            print('\n..........This is the new sorted Tab...........')
            for quarks,leptons in enumerate(dict_tabs[sort_name]):
                print('{}{}'.format((str(quarks)+'. '),(leptons.title())))
            
    elif choice=='6':
        print('Good-bye👋👋👋👋👋👋 i hope the to-do list helped')
        break

    else:
        print('\n..............Pick a number within the available option !!!!!!.....................')