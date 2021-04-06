#include<bits/stdc++.h>
using namespace std;

//function to decrypt the cipher text using brute force attack
void decrypt(string cipher)
{
    string text;
    for(int key=0; key<26; key++)
    {
        text = "";
        for(int i=0; i<cipher.length(); i++)
        {
            cipher[i] = tolower(cipher[i]);
            if((cipher[i] - key - 97) < 0)
                text += 123 + (cipher[i] - key - 97);
            else
                text += (cipher[i] - key - 97) + 97;
        }

        cout << "plain text for key " << key << " :- " << text << endl;
        cout<<endl;
    }
}

int main()
{
    string cipher="krclxrwrbxwnxocqnlxxunbcrwencrxwbrwanlnwccrvnb";
    decrypt(cipher);
}
