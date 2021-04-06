#!/usr/bin/python3

def caesar(string, shift):
    return "".join(chr(((ord(char) - 97 + shift)%26) + 97) if not char.isspace() else " " for char in string)

def frequencyAnalysis(string): # Normalised frequency analysis
    freq = [0]*26

    for c in string:
        if(c.isalpha()):
            freq[ord(c)-ord('a')]+=1

    total = sum(freq)

    for i in range(0, len(freq)):
        freq[i] /= (float(total) / 100)

    return freq


def shiftScoreCalculator(frequencyAnalysis, shift): # Calculates a weighted score for a given shift value
    englishFrequencies = [  8.167, 1.492, 2.782,
                            4.253, 12.702, 2.228,
                            2.015, 6.094, 6.966,
                            0.153, 0.772, 4.025,
                            2.406, 6.749, 7.507,
                            1.929, 0.095, 5.987,
                            6.327, 9.056, 2.758,
                            0.978, 2.360, 0.150,
                            1.974, 0.074 ]

    score = 0

    for index in range(0, 26):
        shiftIndex = (index + shift) % 26
        score += abs(frequencyAnalysis[index] - englishFrequencies[shiftIndex])

    return score / 26

def shiftCalculator(frequencyAnalysis): # Calculates the most likely shift value for a substring by comparing weighted scores of different shift values
    bestGuess = ''
    bestGuessVal = float('inf')

    for shift in range(1, 27):
        score = shiftScoreCalculator(frequencyAnalysis, shift)

        if score < bestGuessVal:
            bestGuessVal = score
            bestGuess = 26 - shift

    return bestGuess

def main():

    string = "krclxrwrbxwnxocqnlxxunbcrwencrxwbrwanlnwccrvnb"
    shift = shiftCalculator(frequencyAnalysis(string))
    print("Best shift value guess: %d (%c)\nAttempting decryption...\n%s" % (shift, chr(shift + ord('a') - 1), caesar(string, -shift)))

if __name__ == "__main__":
    main()