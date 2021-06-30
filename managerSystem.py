from part import *


class PartManager(object):
    def __init__(self):
        self.part_list = []

    def run(self):

        self.load_part()

        while True:
            self.show_menu()
            menu_num = int(input('please input function number: '))
            if menu_num == 1:
                # add
                self.add_part()
            elif menu_num == 2:
                # delete
                self.del_part()
            elif menu_num == 3:
                # modify
                self.modify_part()
                pass
            elif menu_num == 4:
                # search
                self.search_part()
            elif menu_num == 5:
                # show
                self.show_part()
            elif menu_num == 6:
                # save
                self.save_part()
            elif menu_num == 7:
                # exit
                break

    @staticmethod
    def show_menu():
        print('please pick a function -----------------')
        print('1:add')
        print('2:delete')
        print('3:modify')
        print('4:search')
        print('5:show all information')
        print('6:save')
        print('7:exit')

    def add_part(self):
        name = input('input name: ')
        location = input('input location: ')
        partNumber = input('input partNumber: ')
        part = Part(name, location, partNumber)
        self.part_list.append(part)
        print(self.part_list)
        print(part)

    def del_part(self):
        del_name = input('input delete name: ')
        for i in self.part_list:
            if i.name == del_name:
                self.part_list.remove(i)
                break
        else:
            print('no match record')

        print(self.part_list)

    def modify_part(self):
        modify_name = input('input modify name: ')
        for i in self.part_list:
            if i.name == modify_name:
                i.name = input('input new name: ')
                i.location = input('input new location: ')
                i.partNumber = input('input new partNumber: ')
                print(f'modify success,name={i.name},location={i.location}, partNumber = {i.partNumber}')
                break
        else:
            print('no match record')

    def search_part(self):
        search_name = input('what name do you want to search: ')
        for i in self.part_list:
            if i.name == search_name:
                print(f'name={i.name},location={i.location}, partNumber = {i.partNumber}')
                break
        else:
            print('no match record')

    def show_part(self):
        print('name\tlocation\tpartNumber')
        for i in self.part_list:
            print(f'{i.name}\t\t{i.location}\t\t\t{i.partNumber}')

    def save_part(self):
        f = open('part.data', 'w')
        new_list = [i.__dict__ for i in self.part_list]
        # [{'name': 'aa', 'location': 'nv', 'partNumber': '111'}]
        print(new_list)
        f.write(str(new_list))
        f.close()

    def load_part(self):
        try:
            f = open('part.data', 'r')
        except:
            f = open('part.data', 'w')
        else:
            data = f.read()
            new_list = eval(data)
            self.part_list = [Part(i['name'], i['location'], i['partNumber']) for i in new_list]
        finally:
            f.close()

