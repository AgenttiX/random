# This is a simple program to create Gmail compatible domain filters (for spam etc.)
# Copyright Mika "AgenttiX" Mäki, 2016

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


filename = "domains.txt"


class Spam:
    def __init__(self):
        self.__domainlist = []

    def readfile(self):
        """ Reads the domains from a predetermined file """
        try:
            with open(filename, mode="r") as fileobject:
                for line in fileobject:
                    line = line.rstrip()
                    self.__domainlist.append(line)

            fileobject.close()
        except:
            print("Error when reading file")

    def getlist(self):
        """ Returns the domains in a Gmail compatible string """
        self.__domainlist.sort()

        outstr = "{ "
        for index, domain in enumerate(self.__domainlist):
            outstr += domain + " "
            if (index % 50 == 0) and index > 0:
                outstr += "}\n{ "

        outstr += "}"

        return outstr

    def add(self, newaddress):
        """
        Adds a new address to the list
        :param newaddress: A new address example@example.com as a string
        :return: -
        """
        list = newaddress.split("@")
        newdomain = list[-1]
        if not newdomain in self.__domainlist:
            self.__domainlist.append(newdomain)
        else:
            print("Domain is already in the database")

    def write(self):
        """ Writes the list to a predetermined file"""
        self.__domainlist.sort()

        try:
            fileobject = open(filename, mode="w")
            for domain in self.__domainlist:
                fileobject.write(domain + "\n")
            fileobject.close()
        except:
            print("Error when writing file")


def main():
    # Creates a new instance of the domain handler
    spam = Spam()

    # UI loop
    while True:
        print("> ", end="")
        inputstr = input()
        command = inputstr.split(" ")

        if command[0] == "q":
            break

        elif command[0] == "read":
            spam.readfile()

        elif command[0] == "print":
            print(spam.getlist())

        elif command[0] == "add":
            try:
                spam.add(command[1])
            except:
                print("Error")

        elif command[0] == "write":
            spam.write()


main()
