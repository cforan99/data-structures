def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    cohort_data_file = open(filename)

    houses = set()

    for line in cohort_data_file:
        line = line.split("|")
        houses.add(line[2])


    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """
    # added lists for all cohorts in data file
    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    fall_14 = []
    summer_14 = []
    spring_13 = []
    fall_13 = []
    tas = []

    # printed a set of all cohorts in data files
    cohort_data_file = open(filename)

    cohort_set = set()

    for line in cohort_data_file:
        line = line.rstrip()
        line = line.split("|")
        cohort_set.add(line[4])

    print cohort_set

    # This will sort students into cohorts
        # name = line[0] + " " + line[1]
        # if line[4] == "Winter 2015":
        #     winter_15.append(name)
        # elif line[4] == "Spring 2015":
        #     spring_15.append(name)
        # elif line[4] == "Summer 2015":
        #     summer_15.append(name)

    return all_students


# def students_by_house(filename):
#     """TODO: Sort students by house.

#     Iterate over the data to create a list for each house, and sort students
#     into their appropriate houses by last name. Sort TAs into a list called "tas".
#     Return all lists in one list of lists.
#         ex. hufflepuff = ["Gaikwad", "Le", "..." ]
#         ex. tas = ["Bryant", "Lefevre", "..."]
#         ex. houses_tas = [ hufflepuff,
#                         gryffindor,
#                         ravenclaw,
#                         slytherin,
#                         dumbledores_army,
#                         order_of_the_phoenix,
#                         tas
#             ]
#     """

#     all_students = []
#     gryffindor = []
#     hufflepuff = []
#     slytherin = []
#     dumbledores_army = []
#     order_of_the_phoenix = []
#     ravenclaw = []
#     tas = []

#     # Code goes here

#     return all_students


# def all_students_tuple_list(filename):
#     """TODO: Create a list of tuples of student data.

#     Iterates over the data to create a big list of tuples that individually
#     hold all the data for each person. (full_name, house, advisor, cohort)
#         ex. all_people = [
#                 ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
#                 ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
#                 # ...
#             ]
#     """

#     student_list = []

#     # Code goes here

#     return student_list


# def find_cohort_by_student_name(student_list):
#     """TODO: Given full name, return student's cohort.

#     Use the above list of tuples generated by the preceding function to make a small
#     function that, given a first and last name, returns that student's cohort, or returns
#     'Student not found.' when appropriate. """

#     # Code goes here

#     return "Student not found."


# ##########################################################################################
# # Further Study Questions


# def find_name_duplicates(filename):
#     """TODO: Using set operations, make a set of student first names that have duplicates.

#     Iterates over the data to find any first names that exist across multiple cohorts.
#     Uses set operations (set math) to create a set of these names.
#     NOTE: Do not include staff -- or do, if you want a greater challenge.

#        ex. duplicate_names = set(["Sarah"])

#     """

#     duplicate_names = set()

#     # Code goes here

#     return duplicate_names


# def find_house_members_by_student_name(student_list):
#     """TODO: Create a function that prompts the user for a name via the command line
#     and returns everyone in their house that's in their cohort.

#     Use the list of tuples generated by all_students_tuple_list to make a small function that,
#     when given a student's first and last name, returns students that are in both that
#     student's cohort and that student's house."""

#     # Code goes here

#     return


# #########################################################################################

# #Here is some useful code to run these functions!

# # all_students_data = all_students_tuple_list("cohort_data.txt")
# # print all_students_data
# # print unique_houses("cohort_data.txt")
# # print sort_by_cohort("cohort_data.txt")
# # print students_by_house("cohort_data.txt")
# # print find_name_duplicates("cohort_data.txt")
# # find_house_members_by_student_name(all_students_data)
# # find_cohort_by_student_name(all_students_data)
