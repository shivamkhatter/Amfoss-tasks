#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
float change;
int count = 0;
do
{
change = get_float("Change owed: ");
}
while (change < 0);
int cent = round(change * 100);
while (cent >= 25)
{
cent = cent - 25;
count++;
}
while (cent >= 10)
{
cent = cent - 10;
count++;
}
while (cent >= 5)
{
cent = cent - 5;
count++;
}
while (cent >= 1)
{
cent = cent - 1;
count++;
}
printf("%i\n", count);
}