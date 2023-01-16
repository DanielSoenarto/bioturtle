import time
print("--------------------------------------------Welcome to Bioturtle--------------------------------------------")
time.sleep(0.75)
print("-------------------------------------analyze your FASTA file with ease--------------------------------------")
time.sleep(0.75)
print("-----------------------------------------By: Daniel Nelson (20010087)---------------------------------------")
time.sleep(0.75)
print("\nINSTRUCTIONS:")
time.sleep(0.75)
print("""
To use Bioturtle, download a FASTA file and put it inside the same folder with the program.

When you're being prompted for the file, make sure to type the whole file name. For example:

Enter a FASTA file: ideonella_sakaiensis.fasta
""")
time.sleep(0.75)
print("""
--------------------------------------------------------------------------------------------------------------------
COMMANDS (type one of these when being prompted):
1) intro: to return the "ID, Name, and Description".
2) analysis: to return the length and to analyze the A,T,G,C content.
3) done: to exit the program.
--------------------------------------------------------------------------------------------------------------------
""")

# FASTA file input
time.sleep(0.5)
try :
    fname = input("Enter a FASTA file: ")
    if fname.lower() == "done" :
        print("\nThank you for using Bioturtle ^o^\n")
        quit()
    fhand = open(fname)
except FileNotFoundError :
    print("\nERROR: File not found. Make sure it's the correct format and it's in the same directory\n")
    quit()

# Inserting the commands
while True :
    commands = ["intro", "analysis", "done"]
    try :
        user_input = input("\nEnter a command: ").lower()
        if user_input not in commands :
            raise
    except :
        print("\nPlease type in the commands from the instructions only")
        quit()

    # Output 1: ID, Name, Description
    if user_input == "intro" :            
        # Looping the lines in the file
        for line in fhand :
            if line.startswith(">") :

                # Getting the FASTA ID & Name                       
                id_start = line.find(">")
                id_end = line.find(" ", id_start)           
                fasta_id = line[id_start + 1 : id_end]

                # Getting the description      
                desc_start = id_end + 1
                desc_end = line.find("\n")
                desc = line[desc_start : desc_end]

                # Printing the output 1
                print("\nINTRO...")
                print("|10%  =---------|")
                time.sleep(0.5)
                print("|30%  ===-------|")
                time.sleep(0.5)
                print("|50%  =====-----|")
                time.sleep(0.5)
                print("|90%  =========-|")
                time.sleep(0.5)
                print("|100% ==========|")
                time.sleep(0.75)
                print("-----------------------------------------------------------------------------------------------------------")
                print(f"ID: {fasta_id}")
                print(f"Name: {fasta_id}")
                print(f"Description: {desc}")
                print("-----------------------------------------------------------------------------------------------------------")


    # Output 2: Length, A, T, G, C, GC count
    elif user_input == "analysis" :
        fhand2 = open(fname)
        fasta = ""

        for line in fhand2 :
            if line.startswith(">") :
                continue
            word = line.rstrip()
            fasta = fasta + word

        # Base variables
        fasta_length = len(fasta)
        A_count = fasta.count("A")
        T_count = fasta.count("T")
        G_count = fasta.count("G")
        C_count = fasta.count("C")
        purine = A_count + G_count
        pyrimidine = C_count + T_count
        GC_count = (G_count + C_count) / fasta_length * 100

        time.sleep(1)
        print("ANALYZING...")
        time.sleep(2)
        if fasta_length < 5000 :
            print("|10%  =---------|")
            time.sleep(0.5)
            print("|30%  ===-------|")
            time.sleep(0.5)
            print("|50%  =====-----|")
            time.sleep(0.5)
            print("|90%  =========-|")
            time.sleep(0.5)
            print("|100% ==========|")
            time.sleep(0.75)
        elif fasta_length > 10000 :
            print("|10%  =---------|")
            time.sleep(0.5)
            print("|20%  ==--------|")
            time.sleep(0.5)
            print("|30%  ===-------|")
            time.sleep(0.5)
            print("|40%  ====------|")
            time.sleep(0.5)
            print("|50%  =====-----|")
            time.sleep(0.5)
            print("|60%  ======----|")
            time.sleep(0.5)
            print("|70%  =======---|")
            time.sleep(0.5)
            print("|80%  ========--|")
            time.sleep(0.5)
            print("|90%  =========-|")
            time.sleep(0.5)
            print("|100% ==========|")
            time.sleep(1)
        else :
            print("|10%  =---------|")
            time.sleep(0.5)
            print("|20%  ==--------|")
            time.sleep(0.5)
            print("|30%  ===-------|")
            time.sleep(0.5)
            print("|50%  =====-----|")
            time.sleep(0.5)
            print("|80%  ========--|")
            time.sleep(0.5)
            print("|90%  =========-|")
            time.sleep(0.5)
            print("|100% ==========|")
            time.sleep(0.75)
        print("-----------------------------------------------------------------------------------------------------------")
        print(f"The length of the nucleotides ({fname}) is {fasta_length} base pairs")
        print(f"The A count is: {A_count}")
        print(f"The T count is: {T_count}")
        print(f"The G count is: {G_count}")
        print(f"The C count is: {C_count}")
        print(f"Number of purines: {purine}")
        print(f"Number of pyrimidines: {pyrimidine}")
        print(f"The GC content: {round(GC_count, 2)}%")
        print("-----------------------------------------------------------------------------------------------------------")

    elif user_input == "done" :
        print("\nThank you for using Bioturtle ^o^\n")
        quit()