#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize){
    

    int *res = (int *)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] < 0)
            nums[i] = nums[i] * -1;
    }
    qsort(nums, numsSize, sizeof(int), compare);
        
    
    for (int i = 0; i < numsSize; i++)
        res[i] = nums[i] * nums[i];

    return res;
}

// int* sortedSquares(int* A, int ASize, int* returnSize) {
//     int* ans = calloc(ASize, sizeof(int));
//     *returnSize = ASize;
//     int i = 0, j = ASize - 1, index = ASize - 1;
//     while(i <= j)
//     {
//         if(-A[i] > A[j])
//         {
//             ans[index--] = A[i] * A[i];
//             i++;
//         }
//         else
//         {
//             ans[index--] = A[j] * A[j];
//             j--;
//         }
//     }
//     return ans;
// }