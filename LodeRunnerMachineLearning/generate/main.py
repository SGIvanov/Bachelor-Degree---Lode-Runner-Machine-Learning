from keras.models import load_model
import numpy as np
import os

def main():
    print(mockMap(),end='')

def mockMap():
    map = "                  S             $             S         #######H#######   S                H----------S    $           H    ##H   #######H##       H    ##H          H  " + \
          "     0 H    ##H       $0 H  ##H#####    ########H#######  H                 H         H           0     H       #########H##########H                H          H       " + \
          "       $ H----------H   $       H######         #######H    H         &  $ $$      H############################"
    return map
if __name__ == '__main__':
    main()