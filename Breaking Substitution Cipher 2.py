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
    s = "VDUMU NEC E NEFF EDUEY SV ZUOEH DSOD SH VDU ESM EHY URVUHYUY BKNEMY LBV LI CSODV SV NEC MSYYFUY NSVD DLFUC VDEV NUMU VDU GLBVDC LI VBHHUFC OEEF'C VERS GLAUY VLNEMY LHU, VDUH KFBHOUY SHVL SV ILM E GLGUHV OEEF NLHYUMUY SYFP DLN DSC YMSAUM TLBFY KSTX LBV LHU EGLHO CL GEHP VDUMU NEC HLN LHFP ZFETXHUCC NSVD HLVDSHO ZBV VDU KECV-IFECDSHO LI E TLFLMUY CSOHEF FSODV VL MUFSUAU VDU OFLLG VDU ESM NEC IBFF LI E MBCDSHO CLBHY OEEF FUEHUY ILMNEMY EOESHCV YUTUFUMEVSLH VDUH EHY VDU VERS KLKKUY LBV LI VDU VBHHUF EHY YUCTUHYUY VL OMLBHY-FUAUF LHTU GLMU VDU FBRLM DLVUF CESY VDU YMSAUM BHHUTUCCEMSFP DU DUFKUY OEEF NSVD DSC ZEOOEOU ETTUKVUY E VUHVD-TMUYSV VSK NSVD E ZBCSHUCCFSXU ESM KSTXUY BK E NESVSHO KECCUHOUM EHY NEC MSCSHO EOESH SH EFF VDSC IMLG VDU GLGUHV LI YUZEMXEVSLH VDUMU DEY ZUUH HL OFSGKCU LI CXP VMEHVLM EV VDU ZUOSHHSHO LI VDU VDSMVUUHVD GSFFUHHSBG VDSC VUHYUHTP MUETDUY SVC TFSGER EC VDU TUHVUM LI VDU SGKUMSEF OLAUMHGUHV ILM BHZMLXUH DBHYMUYC LI OUHUMEVSLHC EHY FLTEVUY EC SV NEC VLNEMY VDU TUHVMEF MUOSLHC LI VDU OEFERP EGLHO VDU GLCV YUHCUFP KLKBFEVUY EHY SHYBCVMSEFFP EYAEHTUY NLMFYC LI VDU CPCVUG, SV TLBFY CTEMTUFP DUFK ZUSHO VDU YUHCUCV EHY MSTDUCV TFLV LI DBGEHSVP VDU METU DEY UAUM CUUH SVC BMZEHSQEVSLH, KMLOMUCCSHO CVUEYSFP DEY ISHEFFP MUETDUY VDU BFVSGEVU. EFF VDU FEHY CBMIETU LI VMEHVLM CJBEMU GSFUC SH URVUHV NEC E CSHOFU TSVP VDU KLKBFEVSLH EV SVC DUSODV NEC NUFF SH URTUCC LI ILMVP ZSFFSLHC VDSC UHLMGLBC KLKBFEVSLH NEC YUALVUY EFGLCV UHVSMUFP VL VDU EYGSHSCVMEVSAU HUTUCCSVSUC LI UGKSMU EHY ILBHY VDUGCUFAUC EFF VLL IUN ILM VDU TLGKFSTEVSLHC LI VDU VECX (SV SC VL ZU MUGUGZUMUY VDEV VDU SGKLCCSZSFSVP LI KMLKUM EYGSHSCVMEVSLH LI VDU OEFETVST UGKSMU BHYUM VDU BHSHCKSMUY FUEYUMCDSK LI VDU FEVUM UGKUMLMC NEC E TLHCSYUMEZFU IETVLM SH VDU IEFF) YESFP IFUUVC LI CDSKC SH VDU VUHC LI VDLBCEHYC ZMLBODV VDU KMLYBTU LI VNUHVP EOMSTBFVBMEF NLMFYC VL VDU YSHHUM VEZFUC LI VMEHVLM SVC YUKUHYUHTU BKLH VDU LBVUM NLMFYC ILM ILLY EHY SHYUUY ILM EFF HUTUCCSVSUC LI FSIU GEYU VMEHVLM SHTMUECSHOFP ABFHUMEZFU VL TLHJBUCV ZP CSUOU SH VDU FECV GSFFUHHSBG LI VDU UGKSMU VDU GLHLVLHLBCFP HBGUMLBC MUALFVC GEYU UGKUMLM EIVUM UGKUMLM TLHCTSLBC LI VDSC EHY SGKUMSEF KLFSTP ZUTEGU FSVVFU GLMU VDEH VDU KMLVUTVSLH LI VMEHVLM'C YUFSTEVU WBOBFEM AUSH"
    #letterFreq = getLetterfreq(s)
    attempt = s.replace("W", "\033[31mJ\033[0m") # W to J Wugular to Jugular which is meaningful and placing it before N to W and now in top.
    attempt = attempt.replace("N", "\033[31mW\033[0m")  # replacing the next letter according to count N with w because Nas to was nall to wall nith to with make sense. Arranged it before H to N
    attempt = attempt.replace("H", "\033[31mN\033[0m") #Count of H is also 136 as I have been replaced earlier so replaced it with 6th maximum N
    attempt = attempt.replace("D", "\033[31mH\033[0m") #Count of D is 90 so according to frequency order it is replaced with H
    attempt = attempt.replace("Y", "\033[31mD\033[0m") #Count of Y is 86 so according to frequency order it is replaced with D
    attempt = attempt.replace("P", "\033[31mY\033[0m")  # Attempting P to Y according to frequency
    attempt = attempt.replace("K", "\033[31mP\033[0m")  # Replace the next letter accoding to count K to the next letter according to frequency after G which is P. PLacing it before X to K
    attempt = attempt.replace("X", "\033[31mK\033[0m") #X to K and replaced it before R to X
    attempt = attempt.replace("R", "\033[31mX\033[0m") # ERTENDED TO EXTENDED and placed it before M to R.
    attempt = attempt.replace("M", "\033[31mR\033[0m")  # Count of M is 109 so replacing it with R character with 8th maximum frequency. Re-arrange again before G to M
    attempt = attempt.replace("G", "\033[31mM\033[0m") # Replaced G to M according to frequency order. Re-Arranged back to before O to G.
    attempt = attempt.replace("O", "\033[31mG\033[0m") # Replaced O to G according to frequency order. Re-arranged back to before L changed to O
    attempt = attempt.replace("L", "\033[31mO\033[0m") #Count of L is 139 4th maximum also O is with the 4th maximum frequency emong english letters
    attempt = attempt.replace("F", "\033[31mL\033[0m") #Count of F is 103 replacing it with L and placed it before I to F
    attempt = attempt.replace("I", "\033[31mF\033[0m") # Replacing I count 48 to F according to frequency order and placed it before S to I
    attempt = attempt.replace("S", "\033[31mI\033[0m") #Count of S is 136 and I is the 5th maximum freqwuency letter so replacing with it. rearranged to top
    attempt = attempt.replace("C", "\033[31mS\033[0m") #Count of C is 112 so replacing it with S 7th maximum frequency. Rearranged to top
    attempt = attempt.replace("T", "\033[31mC\033[0m")  # Count of T is 48 so according to frequency order it is replaced with the next C in the list. Now as we replace V to T earlier. So we have movie this line to abothe V to T. Or all the instances of T will be changed
    attempt = attempt.replace("V", "\033[31mT\033[0m") #Count of V is 178 and T's frequency is 9.6 2nd maximum
    attempt = attempt.replace("A", "\033[31mV\033[0m")  # Replacing A to V according to frequency and moved it before E to A.
    attempt = attempt.replace("E", "\033[31mA\033[0m")  # Because there's a single word E many times. It can be either A or I. And also E's count is 146
    attempt = attempt.replace("U", "\033[31mE\033[0m") #U to E because count of U is 234 and E is maximum frequency letter of english
    attempt = attempt.replace("B", "\033[31mU\033[0m") #Count of B is 51 so according to frequency order it is replaced with the next in frequency order after D which is U
    attempt = attempt.replace("Z", "\033[31mB\033[0m") # Replacing Z to B according to frequency
    attempt = attempt.replace("Q", "\033[31mZ\033[0m")  # Replacing Q to Z Urbaniqation to Urbanization
    attempt = attempt.replace("J", "\033[31mJ\033[0m") # Last remaining letter. The sentence is already decrypted. So J to J.


    #for letter in letterFreq:
     #   print(letter, ":", letterFreq[letter])
    print(attempt)