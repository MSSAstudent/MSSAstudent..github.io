#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab12, exercise2, Ex2Median

import Methods as m

def main():
    nums1 = [12, 67, 13, 5, 45, 19, 7, 15, 23, 3]
    nums2 = [12, 67, 13, 5, 45, 19, 7, 15, 23, 3, 32]

    # test numbers
    #nums1 = [4, 3, 1, 2, 4, 3, 2, 1, 1, 5]
    #nums2 = [1567, 4267, 67, 7, 2053, 89, 3600, 2600, 1600, 2020, 2022]

    nums_1 = m.as_sort_integers(nums1)
    mean1 = m.calc_mean(nums1)
    median1 = m.calc_median(nums_1)
    nums_2 = m.as_sort_integers(nums2)
    mean2 = m.calc_mean(nums2)
    median2 = m.calc_median(nums_2)



    print(nums_1)
    print("Mean = " + str(mean1))
    print("Median = " + str(median1))

    print(nums_2)
    print("Mean = " + str(mean2))
    print("Median = " + str(median2))

if __name__ == "__main__":
    main()
