#! python3
import sys, re, requests
from bs4 import BeautifulSoup


def get_roster_url(club_name, division):
    mens_clubs = {
        "alliance": 7424852,
        "bluedevils": 7424853,
        "burlington": 7424855,
        "waterloo": 7424880,
        "darby": 7424858,
        "electriccity": 7424861,
        "london": 7424862,
        "guelph": 7424863,
        "hamilton": 7424864,
        "masters": 7424865,
        "northmiss": 7424866,
        "northtoronto": 7424867,
        "pickering": 7424868,
        "prostars": 7424869,
        "scrosoppi": 7424870,
        "sigma": 7424871,
        "simcoe": 7424873,
        "stcatherines": 7424875,
        "unionville": 7424876,
        "vaughan": 7424877,
        "windsor": 7424878,
        "woodbridge": 7424879,
    }

    womens_clubs = {
        "alliance": 7415920,
        "bluedevils": 7415936,
        "burlington": 7416335,
        "waterloo": 7416254,
        "darby": 7415947,
        "electriccity": 7415986,
        "london": 7416006,
        "guelph": 7416018,
        "hamilton": 7416040,
        "ndc": 7416327,
        "northmiss": 7416052,
        "northtoronto": 7416059,
        "pickering": 7416081,
        "prostars": 7416295,
        "simcoe": 7416099,
        "stcatherines": 7416317,
        "tecumseh": 7416140,
        "unionville": 7416164,
        "vaughan": 7416238,
        "woodbridge": 7416260,
    }

    if division == "m":
        return mens_clubs.get(club_name, "Club does not exist")
    elif division == "w":
        return womens_clubs.get(club_name, "Club does not exist")
    else:
        return False


if len(sys.argv) > 2:
    team = re.sub("[^a-z]", "", sys.argv[1].lower())
    division = sys.argv[2].lower()[0]

    if division == "m":
        roster_code = get_roster_url(team, division)
        season_code = 809614
    elif division == "w":
        roster_code = get_roster_url(team, division)
        season_code = 809616

    if type(roster_code) is int:
        address = f"https://www.league1ontario.com/schedule/team_instance/{roster_code}?subseason={season_code}"

        res = requests.get(address)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select(".compactGameList")
        print(results)
    else:
        print("not an existing team")


else:
    print("no args?")
