def hourglass_sum(arr):
    max_sum = float('-inf')
    
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            current_sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                           arr[i + 1][j + 1] +
                           arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
            max_sum = max(max_sum, current_sum)
    
    return max_sum


def lambda_handler(event, context):
    # Example: return the sum of two numbers from the event
    arr = event.get('arr', [])
    if not arr or len(arr) < 3 or len(arr[0]) < 3:
        return "Invalid input: Array must be at least 3x3 in size."
    return hourglass_sum(arr)
    

