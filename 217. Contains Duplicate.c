#include <stdbool.h>

void	quicksort(int arr[], int L, int R)
{
	int	left;
	int	right;
	int	pivot;

	left = L;
	right = R;
	pivot = arr[(L + R) / 2];
	while (left <= right)
	{
		while (arr[left] < pivot)
			left++;
		while (arr[right] > pivot)
			right--;
		if (left <= right)
		{
			swap(&arr[left], &arr[right]);
			left++;
			right--;
		}
	}
	if (L < right)
		quicksort(arr, L, right);
	if (left < R)
		quicksort(arr, left, R);
}

void	swap(int *a, int *b)
{
	int	t;

	t = *a;
	*a = *b;
	*b = t;
}


bool containsDuplicate(int* nums, int numsSize){
    
    quicksort(nums, 0, numsSize - 1);
    for (int i = 0; i < numsSize - 1; i++)
    {
        if (nums[i] == nums[i + 1])
            return true;
    }
    return false;
}