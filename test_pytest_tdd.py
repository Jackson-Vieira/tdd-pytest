# Imagine you’re writing a function, format_data_for_display(), to process the data returned by 
# an API endpoint. The data represents a list of people, each with a 
# given name, family name, and job title. The function 
# should output a list of strings that include each person’s full name 
# (their given_name followed by their family_name), a colon, and their

import pytest


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def format_data_for_display(data):
    cols = list(data[0].keys())
    rows = [list(people.values()) for people in data]
    rows_formatted = [','.join(map(str, row)) for row in rows]
    return '\n'.join([','.join(cols)] + rows_formatted) 

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == """given_name,family_name,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager"""
