#ifdef A
    x=100/0;
#ifdef B
        y=100/0;
#endif #else
    z=100/0;
#endif
#ifndef C
#error C must be defined
#endif

void f() {
    char arr[5];
    arr[10] = arr[10] / 0;
}

void f(int *p)
{
    *p = 3;
}
int main() {
int*p=0;
}