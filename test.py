
import re

regex = r"\d"

test_str = ("1030247719,AARON ANDRES OVIEDO OVIEDO\n"
	"1103754527,ALAN SEBASTIAN GRANADOS GENEY\n"
	"1103515254,ALANIS  FERNANDEZ ROMERO\n"
	"1025555579,ALICIA ISABEL ABUCHAR MONTERROZA")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))