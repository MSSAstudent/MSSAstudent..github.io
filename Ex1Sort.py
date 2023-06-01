#!/user/bin/env python3

# Matthew Hays
# Cuyamaca College CS-119
# Lab12, exercise1, Ex1Sort

import Methods as m

def main():
    nums1 = [12, 67, 7, 5, 45, 19, 13, 15, 23, 3]
    #nums1 = [77, 102, 55, 48, 2, 19, 79, 81, 60, 57, 113]

    # high to low
    nums2 = m.de_sort_integers(nums1)

    # low to high
    #nums2 = m.as_sort_integers(nums1)

        
    print(nums2)

if __name__ == "__main__":
    main()

    
