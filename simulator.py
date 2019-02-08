#David Roster
#CS176B HW2

def open_audio_source_file():
    print("Entering open_audio_source_file() function")
    print("Fuck me")
    f=open("pink_panther.au", "rb")
    #print("source file is " + f)
    return f

def open_audio_dest_file():
    print("Entering open_audio_dest_file() function")
    print("Fuck Me")
    f=open("test_pinkpanther.au", "wb")
    #print("dest file is " + f)
    return f

def read_sample(filename):
    print("Entering read_sample(filename) function")
    print("filename is ...")
    print(filename)
    #print("Entering read_sample(filename) function")
    #with open("pink_panther.au", "wb") as f:
    f = open("pink_panther.au", "rb")
    byte = f.read(10000)
    print("This is value of byte = ")
    print(byte)
        #while byte:
            # Do stuff with byte.
            #byte = f.read(1)
    return byte



def store_sample(filename, sample):
    print("Entering store_sample() function")
    print("Maca is hella dope")
    f = open("test_pinkpanther.au", "wb")
    print(f)
    f.write(sample)

def store_alternate_data():
    print("Fuck me")

def calculate_loss_probability():
    print("Entering calculate_loss_probability() function")
    print("Me and Danny vs the WORLD")
    loss_probability = 90
    print("Returning loss probability is ")
    print(loss_probability)
    return loss_probability


# if __name__ == '__main__':
#     main()

def main():

    SF = open_audio_source_file()
    #print("source file is " + SF)
    DF = open_audio_dest_file()
    #print("source file is " + DF)

    threshold = 99

    #while not EOF
    while True:
        sample = read_sample(SF)   #Read audio sample from a file 
        loss = calculate_loss_probability()
        if (loss < threshold): 
            store_sample(DF, sample)   #Store the received sample

        else:
            store_alternate_data()   #See details for alternativess

if __name__ == '__main__':
    main()
