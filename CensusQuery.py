# File: Project3.py

# Course Name: CS303E
#
# Date Created: 4/14/23
# Date Last Modified: 4/15/23
# Description of Program: allows user to input queries regarding database information from the 2020 Texas Census

import os.path


def dicfunc(infile):
    txdict = {}
    city_names = []
    census_2020 = 0
    census_2023 = 0

    censusfile = open(infile, "r")
    line = censusfile.readline()

    # while there is a line to be read
    while line:
        # makes sure that label line does not get read and also anything with #
        if "#" not in line:
            # gets the population number but this works for if there are multiple numbers
            things = line.split(",")
            census_2020 += int(things[1])
            census_2023 += int(things[0])
            name = things[3].replace("''", "")
            city_names.append(name)
            # [city] = (2020, 2023)
            txdict[name] = int(things[1]), int(things[0])


        # to next line
        line = censusfile.readline()

    txdict['Texas'] = census_2020, census_2023
    city_names.sort()

    censusfile.close()

    return txdict, city_names


def main():
    infile = "citiesData.csv"

    # checks if file exists
    if not os.path.isfile(infile):
        print("File does not exist")
        return

    citydic, citylist = dicfunc(infile)

    print("\nWelcome to the Texas Cities Population Dashboard.")
    print("This provides census data from the 2020 census and ")
    print("estimated population data in Texas as of 2023.")
    print("\nCreating dictionary from file: citiesData.csv")
    print("\nEnter any of the following commands:\nHelp - list available commands;\nQuit - exit this dashboard;")
    print("Cities - list all Texas cities;\nCensus <cityName>/Texas - population in 2020 census by specified city or statewide;")
    print("Estimated <cityName>/Texas - estimated population in 2023 by specified city or statewide.")
    print("Growth <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.\n")

    commandInput = input("Please enter a command: ")

    while commandInput:
        # Parse the command.  Note that the city name may contain multiple words.
        commWords = commandInput.split()

        # Extract the first word in the command.  It should be one of: help,
        # quit, cities, census, estimated, growth. Lowercase it because we
        # don't want case to matter for the command.
        comm = commWords[0].lower()

        # Extract the rest of the words and re-assemble them into a single string,
        # separated by spaces. This should either be 'Texas' or a city name.
        args = commWords[1:]
        arg = " ".join(args)

        # help command, just reprints the available commands
        if comm == "help":
            print("Enter any of the following commands:\nHelp - list available commands;\nQuit - exit this dashboard;")
            print("Cities - list all Texas cities;\nCensus <cityName>/Texas - population in 2020 census by specified city or statewide;")
            print("Estimated <cityName>/Texas - estimated population in 2023 by specified city or statewide.")
            print("Growth <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.")

        # exits the program
        elif comm == "quit":
            print("Thank you for using the Texas Cities Population Database Dashboard.  Goodbye!")
            exit()

        # returns list of cities, 10 per line
        elif comm == "cities":
            count = 0
            for i in range(len(citylist)):
                # print new row if 10 are already there
                if count == 10:
                    print()
                    count = 0

                # makes sure there's no comma after the last city haha
                if i == (len(citylist)-1):
                    print(citylist[i])

                # print the city on the same line
                else:
                    print(citylist[i], ",", sep="", end=" ")
                    count += 1

        # returns results of 2020 census
        elif comm == "census":
            if arg == "Texas":
                txcenpop, txestpop = citydic['Texas']
                print("Texas' total population in the 2020 Census:", txcenpop)

            elif arg in citydic:
                citycenpop, cityestpop = citydic[arg]
                print(arg, "'s total population in the 2020 Census: ", citycenpop, sep="")

            else:
                print("City", arg, "is not recognized.")

        # returns estimated 2023 value
        elif comm == "estimated":
            if arg == "Texas":
                txcenpop, txestpop = citydic['Texas']
                print("Texas' estimated population in 2023:", txestpop)

            elif arg in citydic:
                citycenpop, cityestpop = citydic[arg]
                print(arg, "'s estimated population in 2023: ", cityestpop, sep="")

            else:
                print("City", arg, "is not recognized.")

        # determines growth between 2020 and 2023, returns a percentage
        elif comm == "growth":
            if arg in citydic:
                citycenpop, cityestpop = citydic[arg]
                growperc = ((cityestpop - citycenpop) / citycenpop) * 100.0
                print(arg, " had percent population change 2020 to 2023: ", format(growperc, ".2f"), "%", sep="")

            else:
                print("City", arg, "is not recognized.")

        # rejects all other non-commands
        else:
            print("Command is not recognized.  Try again!")

        # gets new command
        commandInput = input("\nPlease enter a command: ")


main()
