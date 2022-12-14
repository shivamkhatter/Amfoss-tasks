#include <cs50.h>
#include <stdio.h>
int main(void)
{
int h;
do
{
h = get_int(" Height: ");
}
while (h < 1 || h > 8);
for (int row = 0; row < h; row++)
{
for (int s = h - row - 1; s > 0; s--)
{
printf(" ");
}
for (int c = 0; c< row + 1; c++)
{
printf("#");
}
printf("\n");
}
}