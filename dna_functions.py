import json

from operator import itemgetter


def get_suspect(name = None):
    if name != None:
        try:
            with open("suspects.json", "r") as suspects_file:
                suspects = json.loads(suspects_file.read())
        except FileNotFoundError:
            print("File not found suspects.json")
            suspects = {}

        suspect = suspects.get(name)
        return suspect
    else:
        return None


def get_suspect_dna(suspect = None):
    if suspect != None:
        gender = suspect.get("gender")
        race = suspect.get("race")
        hair = suspect.get("hair")
        eye = suspect.get("eye")
        face = suspect.get("face")

    try:
        with open("dna.json", "r") as dna_file:
            dna = json.loads(dna_file.read())
    except FileNotFoundError:
        print("File not found dna.json")
        return None
    
    dna_gender = dna.get("gender").get(gender)
    dna_race = dna.get("race").get(race)
    dna_hair = dna.get("hair").get(hair)
    dna_eye = dna.get("eye").get(eye)
    dna_face = dna.get("face").get(face)

    return [dna_gender, dna_race, dna_hair, dna_eye, dna_face]


def read_dna():
    try:
        with open("dna.txt", "r") as dna_file:
            dna = dna_file.read()
    except FileNotFoundError:
        print("File not found dna.txt")
        dna = None
    
    return dna


def search_dna(part):
    dna = read_dna()
    if dna != None and dna.find(part):
        return True
    else:
        return False


