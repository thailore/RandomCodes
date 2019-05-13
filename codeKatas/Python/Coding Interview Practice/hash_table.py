#! usr/bin/env python
# -*- coding: utf-8 -*-


class HashTable:
    def get_hash_value(self, info):
        return hash(info) #using built in Hash function

    def add_to_table(self, info):
        hash_value = self.get_hash_value(info)
        self.table[hash_value] = info

    def initiate_hash_table(self):
        self.table = {} #create dictionary (base hash table)


if __name__ == '__main__':
    t = HashTable()
    t.initiate_hash_table()
    while True:
        num = input("How many values do you want to enter to table?: ")
        if int(num) == 0:
            break
        for _ in range(int(num)):
            t.add_to_table(input("Enter new value to be added to table: "))
        print(t.table)
