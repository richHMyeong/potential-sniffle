num_dict={
    'zero':0, 'one':1, 'two':2, 
    'three':3, 'four':4, 'five':5, 
    'six':6, 'seven':7,'eight':8, 
    'nine':9
}

def solution(s):
    answer = 0

    for num in num_dict:
        if num in s:
            s = s.replace(num, str(num_dict[num]))
    answer = int(s)
    return answer
