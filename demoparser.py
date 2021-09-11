# This program goes through your events.txt file and creates a new text file with much more streamlined information.

demo_file = "C:\\Program Files (x86)\\Steam\\SteamApps\\common\\Team Fortress 2\\tf\\demos\\_events.txt"  # Directory of your events.txt
startLine = 44961  # What line should the program start at?
endSig = "EndFileHere"  # Simple string for the program to detect when the program is finished. Should not be anything
# that can be found in an events.txt file.


def gatherLines(file):
    parseLines = file.readlines()[-(len(
        file.readlines()) - startLine):]  # Amount of lines minus the start line to determine how far to go back.
    parseLines.append(f"{endSig}")
    print(len(parseLines))
    return parseLines


# Get the start of the event and reduce it by 3000 for the sake of recording.
def getStartTime(tickNum):
    if tickNum > 3000:
        return tickNum - 3000
    else:
        return tickNum - (tickNum / 2)


def spaceTicks():
    return "".join([num + "\n" for num in demo_List[1]])


def writeToNewFile():
    with open(newFile, 'a') as nFile:
        nFile.write(
            f"\n{str(demo_List[0]).strip('[ ]')[1:-1]}\n\n-TICKS\n{spaceTicks()}\n----------]]\n\n")


with open(demo_file, 'r') as dFile:
    newFile = "NewDemoEvents.txt"
    pLines = gatherLines(dFile)

    demo_List = [[], []]  # First list holds the dateName, second holds all the ticks

    lineNum = 0

    for line in pLines:

        if endSig in line:  # If the line contains the end signature, write the remaining events to file and stop
            writeToNewFile()
            for lst in demo_List:
                lst.clear()
            break

        # If the line isn't a killstreak or a '> spacing' character, then keep going
        if not ("Killstreak" in line) and not len(line) < 3:
            pruneLine = line[19:-1].strip(
                "( )")  # Strip the beginning date and timestamp, as well as the '/n' at the end

            if len(demo_List[0]) < 1:  # If the demo's name has not already been found, then find it:
                firstNum = pruneLine.index('"') + 1  # Grab the index of the first ' " ' for future reference
                passed = False
                ind = 0
                secondNum = None
                # ^^ Algorithm nonsense.

                for letter in pruneLine:  # For each letter in the event line
                    if letter == '"' and not passed:  # If the letter is the first " mark, then pass it.
                        passed = True
                    elif letter == '"' and passed:  # If the letter is the second " mark, grab its index and break the loop
                        secondNum = ind
                        break
                    ind += 1

                dateName = pruneLine[firstNum:secondNum]  # Isolate the name of the demo for ease of access.
                demo_List[0].append(dateName)

            tickTime = pruneLine.split(" ")[-1]  # The demo's time event is always at the end of the line.
            demo_List[1].append(tickTime + f" ; {getStartTime(int(tickTime))}")


        elif line[
             :-1] == ">":  # If the line is a spacing marker, check if the list has any timestamps, if so, write them to the file
            if len(demo_List[1]) > 0:
                writeToNewFile()
            for lst in demo_List:  # Clear the list to start over.
                lst.clear()

        lineNum += 1
