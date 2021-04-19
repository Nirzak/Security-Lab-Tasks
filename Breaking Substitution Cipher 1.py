def getLetterfreq(s):
    letter_freq={}
    for letter in s:
        if(letter.isalpha()):
            if(letter in letter_freq):
                letter_freq[letter]+=1
            else:
                letter_freq[letter] = 1
    return letter_freq


if __name__ == '__main__':
    s = "IT CNJ FGM ETKMNOF CITMITK MIT JWF JIGFT GK YGK MINM SNMMTK CITMITK OM CNJ ZNB GK FOUIM IT CNJ NJINSTZ MG NJQ NDD MIT HDNFTM JTTSTZ MG DOXT RTFTNMI STMND MIT STND GY CIOEI IT INZ PWJM HNKMNQTF INZ RTTF DNRTDTZ DWFEITGF RWM MITKT CTKT SNFB HDNFTMJ CIOEI DOXTZ N JMNFZNKZ MOSTJENDT MINM MGGQ FG NEEGWFM GY MIT HTKINHJ OFEGFXTFOTFM NDMTKFNMOGF GY ZNB NFZ FOUIM. MIT KNMT GY HDNFTMNKB MWKFOFUJ ZOYYTKTZ, NFZ IT ZOZ FGM QFGC MINM GY MKNFMGK"
    letterFreq = getLetterfreq(s)
    attempt = s.replace("W", "\033[31mA\033[0m")  # inserting it back to top
    attempt = attempt.replace("C", "\033[31mW\033[0m") #inserting it back to top
    attempt = attempt.replace("E", "\033[31mC\033[0m") #EERTAIN to CERTAIN. Inserting it back to top so that I doesn't mass up the changes of E
    attempt = attempt.replace("T", "\033[31mE\033[0m") #Count of T is 48 the maximum so replacing it with E (freq: 12)
    attempt = attempt.replace("M", "\033[31mT\033[0m") #Count of M is 43 so replacing it with second maximum T (freq: 9.67)
    attempt = attempt.replace("S", "\033[31mM\033[0m") #Insert back top top
    attempt = attempt.replace("J", "\033[31mS\033[0m") #WAJ to was. back to top
    attempt = attempt.replace("P", "\033[31mJ\033[0m") #P to J for PUST to JUST. Back to Top
    attempt = attempt.replace("H", "\033[31mP\033[0m") #HLANET to PLANET it massing all the position with I. So re-arrange it before I. Back to top
    attempt = attempt.replace("I", "\033[31mH\033[0m") #There's a common word IE on everwhere. As He is meaningful replacing I with H. Back top top
    attempt = attempt.replace("O", "\033[31mI\033[0m") #OT to IT as it's ruining all or and for words so I bring back it on above replacement of I
    attempt = attempt.replace("G", "\033[31mO\033[0m") #According to frequency
    attempt = attempt.replace("U", "\033[31mG\033[0m") #U to G
    attempt = attempt.replace("A", "\033[31mU\033[0m") #Simply assign A to U to break the loop of W to U. Cause if I assign directly W to U then the code is going into a loop
    attempt = attempt.replace("N", "\033[31mA\033[0m") #Count of N is 39 so replacing it with third maximum A (freq: 8.12)
    attempt = attempt.replace("F", "\033[31mN\033[0m")
    attempt = attempt.replace("Y", "\033[31mF\033[0m") #YOR to for inserting it back on before B to Y
    attempt = attempt.replace("B", "\033[31mY\033[0m")  # Assuming DAB to Day inserting it before B not to massing the changes of B
    attempt = attempt.replace("R", "\033[31mB\033[0m") #Assuming Reen to be been
    attempt = attempt.replace("K", "\033[31mR\033[0m") #because of the word ok and theke so replacing k means for both
    attempt = attempt.replace("D", "\033[31mL\033[0m") #according to frequency as we have already replaced O
    attempt = attempt.replace("Z", "\033[31mD\033[0m")
    attempt = attempt.replace("Q", "\033[31mK\033[0m") #Asq to ask Tooq to Took and various matches
    attempt = attempt.replace("X", "\033[31mV\033[0m") # LIXE to LIVE Inconkenient to Inconvenient


    for letter in letterFreq:
        print(letter, ":", letterFreq[letter])
    print(attempt)
