#include <stdio.h>
#include <string>

using namespace std;

unsigned int hash_function(char *);

unsigned int hash_function(char* str) {
    const unsigned int FNV_prime = 0x100193;
    const unsigned int FNV_offset_basic = 0x811C9DC5;

    unsigned int hash = FNV_offset_basic;

    for (auto &&item : str)
    {
        char byte_of_data = item;

        hash ^= byte_of_data;
        hash *= FNV_prime; 
    }
    
    return hash;
    
}
