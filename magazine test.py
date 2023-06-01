#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab07, exercise1, Magazine class test

from Magazine import Magazine

subscriber_name = input("Enter subscriber name: ")
magazine_title = input("Enter magazine title: ")
months_remaining = int(input("Enter months remaining: "))

my_magazine = Magazine(subscriber_name, magazine_title, months_remaining)

print(my_magazine.to_string())
