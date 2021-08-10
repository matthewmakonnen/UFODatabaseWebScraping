
"""A module for tallies of UFO sightings by city.

Attributes:
    None.
"""


import requests
from bs4 import BeautifulSoup
from collections import Counter


class UFO:
    """A class for the UFO object.

    Attributes:
        city (str): the location of the city where the UFO sighting was reported.
        state (str): the location of the state where the UFO sighting was reported.
        numofreports (Counter): the number of reportings within that specific location.
    """
    
    
    def __init__(self, city, state, numofreports):
        """
        Initializes a UFO object.

        Args:
            city (str): the location of the city where the UFO sighting was reported.
            state (str): the location of the state where the UFO sighting was reported.
            numofreports (Counter): the number of reportings within that specific location.
        """

        self.city = city
        self.state = state
        self.numofreports = numofreports


def ufo_sample(path):
    """Processes the UFO sighting sample data.

    Args:
        path (str): the link (URL) of the specific UFO sighting sample data.

    Returns:
        None.
    """
    page = requests.get(path)        
    soup = BeautifulSoup(page.text, "html.parser")
    ufo_table = soup.find('table')
    ufo_trows = ufo_table.findAll('tr')
    ufo_data = []

    for ufo in ufo_trows[1:]:
        ufot = ufo.findAll("td")
        ufor = [u.text for u in ufot]
        city = ufor[1]
        state = ufor[2]
        ufo_data.append(city + ", " + state)
    
    ufo_reports = Counter(ufo_data)
    ufodata = UFO(city, state, ufo_reports)

    for i in ufodata.numofreports.most_common(): 
        ufodata_reports = list(i)
        print(f"{ufodata_reports[0]}  {ufodata_reports[1]}")

    
if __name__ == "__main__":
    """Included both UFO sighting sample data for the program.
    
    1. Run the Monthly Report Index For 02/2019 (Comment Monthly Report Index For 03/2019).
    2. Run the Monthly Report Index For 03/2019 (Comment Monthly Report Index For 02/2019).
    
    """
    
    #Monthly Report Index For 02/2019
    print("\nMonthly Report Index For 02/2019 (Tallies):\n") 
    ufo_sample("http://www.cs.umd.edu/~golbeck/INST326/ndxe201902.html")
   
    #Monthly Report Index For 03/2019
    print("\nMonthly Report Index For 03/2019 (Tallies):\n")
    ufo_sample("http://www.cs.umd.edu/~golbeck/INST326/ndxe201903.html")
