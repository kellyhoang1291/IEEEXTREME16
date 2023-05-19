#include <iostream>

using namespace std;

char Rotate13(char _letter)
{
    int pos = (_letter >= 'A' && _letter <= 'Z') ? _letter - 'A' : _letter - 'a';
    int rotation = (pos + 14) % 26;
    int ret = (_letter >= 'A' && _letter <= 'Z') ? 'A' + rotation : 'a' + rotation;

    return ret;
}

bool IsLetter(char _letter)
{
    return (_letter >= 'A' && _letter <= 'Z') || (_letter >= 'a' && _letter <= 'z');
}

int main() {
    string phrase;
    getline(cin, phrase);

    for (size_t k = 0; k < phrase.length(); k++)
    {
        char current = phrase.at(k);
        if (IsLetter(current))
        {
            phrase.replace(k, 1, string(1, Rotate13(current)));
        }
    }

    cout << phrase << endl;

    return 0;
}