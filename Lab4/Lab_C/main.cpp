#include <string>
#include <iostream>

using namespace std;

unsigned int murmur(string key);

int main()
{
    unsigned int hash = murmur("BSUIR");
    cout << hex <<hash<<endl;

    return 0;
}

unsigned int murmur(string key){
    const unsigned int m = 0x5bd1e995;
    const unsigned int seed = 21;
    const int r = 24;
    unsigned int len = (unsigned int)key.length();

    unsigned int h = seed ^ len;
    string data = key;
    unsigned int k;
    int currentIndex = 0;

    while (len >=4)
    {
        
        k  = data[currentIndex];
        k |= data[currentIndex +1] << 8;
        k |= data[currentIndex+2] << 16;
        k |= data[currentIndex + 3] << 24;

        k *= m;
        k ^= k >> r;
        k *= m;

        h *= m;
        h ^= k;

        currentIndex += 4;
        len -= 4;
    }

    switch (len)
    {
    case 3:
        h^= data[currentIndex + 2] << 16;
    case 2:
        h^= data[currentIndex + 1] << 8;
    case 1:
        h^= data[currentIndex];
        h*=m;
        break;
    }

    h ^= h >> 13;
    h *= m;
    h ^= h >> 15;

    return h;
}

