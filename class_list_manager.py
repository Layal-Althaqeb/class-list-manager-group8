# Class List Manager - Group 8
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
#written by: Layal (Task 1)
def count_names(names):
    return len(names)

# Written by: Bushra (Task 2)
def search_name(names, name):
    for n in names:
        if n == name:
            return True
    return False
# Written by: Shouq (Task 3)
def sort_names(names):
    sorted_list = sorted(names)
    return sorted_list
# ===== Each student adds her function ABOVE this line =====


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)

    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Number of names:", count_names(names))
    print("Search result:", search_name(names, "Lama"))



main()
