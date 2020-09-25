import dna_functions

def main():
    print("Test")

if __name__ == "__main__":
    suspects = ["Eva", "Larisa", "Matej", "Miha"]

    for suspect in suspects:
        data_of_suspect = dna_functions.get_suspect(suspect)
        dna_of_suspect = dna_functions.get_suspect_dna(data_of_suspect)
        dna = dna_functions.read_dna()

        for dna_string in dna_of_suspect:
            if dna.find(dna_string) == -1:
                found = False
                break
            else:
                found = True
        
        if found:
            print(f"{suspect} is guilty.")
        else:
            print(f"{suspect} is innocent.")


