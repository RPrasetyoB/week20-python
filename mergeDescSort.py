def Mergesortdesc(arr):

  if len(arr) > 1:
      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]

      Mergesortdesc(left_half)
      Mergesortdesc(right_half)

      merge_desc(arr, left_half, right_half)

  return arr

def merge_desc(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# keep this function call here 
print(Mergesortdesc(input()))