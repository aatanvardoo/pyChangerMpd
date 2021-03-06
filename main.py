from pyIbus import Ibus
from optparse import OptionParser



def main():

    parser = OptionParser()
    parser.add_option("-m", "--model", dest="model", help="set Your BMW model")
    parser.add_option("-d", action="store_true", dest="debug")
    (opts, args) = parser.parse_args()
    
    if opts.model is not None:
        print("Model: " + opts.model)
    else:
        print("Please add bmw model")
        return
    
    if opts.debug:
        ibusDev = Ibus(opts.model, True ) 
    else:
        ibusDev = Ibus(opts.model, False ) 

    ibusDev.IbusSendTask()
    if opts.model == "e39-debug":
        ibusDev.announceCallback()

    
    while True:
        ibusDev.receive()
                

if __name__ == "__main__":
    main()