import json
import ast

def get_average(arr):
    # Returns the sum of an array.
    sum = 0
    avg = 0
    if len(arr) == 0:
        print("Length its zero")
        return
    if len(arr) == 1:
        return arr[0]
    else:
        for i in range(0, len(arr)):
            sum += arr[i]
            avg = sum / len(arr)
        return avg




def test_oneway():
    f = open("oneway_trials_table_sha1.txt", "r")
    arr_length_str = f.read()
    arr_obj = ast.literal_eval(arr_length_str)
    f.close()
    return get_average(arr_obj)


def test_collision():
    f = open("table_trials_collision_sha1.txt")
    arr_len_str = f.read()
    arr_obj = ast.literal_eval(arr_len_str)
    f.close()
    return get_average(arr_obj)
def main():
    print("Test Collision average:", test_collision())
    print("Test oneway average:", test_oneway())
    if test_collision() > test_oneway():
        print("Test collision average is bigger.")
    elif test_collision() < test_oneway():
        print("Test oneway average is bigger.")



if __name__ == '__main__':
    main()