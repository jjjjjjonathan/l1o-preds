#! python3
import webbrowser, sys, re

if len(sys.argv) > 1:
    
    teams = [
        'vaughan',
        'bluedevils',
        'alliance',
        'northtoronto',
        'simcoe',
        'prostars',
        'guelph',
        'sigma',
        'hamilton',
        'electriccity',
        'woodbridge',
        'scrosoppi',
        'darby',
        'pickering',
        'waterloo',
        'stcatherines',
        'burlington',
        'windsor',
        'masters',
        'unionville',
        'northmississauga',
        'london',
        'ndc',
        'tecumseh'
    ]
    team = re.sub('[^a-z]', '', sys.argv[1].lower())
    
    if team in teams:
        print(team)
    else:
        print('no team found')
else:
    print('no args?')