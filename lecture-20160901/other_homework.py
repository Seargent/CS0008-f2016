#the wrong code
def min(davyd, was, here):
    if davyd>was and was>here and davyd>here:
        return here
    elif davyd<was and was<here and davyd<here:
        return davyd
    else:
        return was
n = int(input())
for i in range(0,n):
    a = input().split (" ")
    print(min(int(a[0]), int(a[1]), int(a[2])), " ")
#
#
#the right code
def min(davyd, was, here):
    if davyd< was and davyd< here:
        return davyd
    elif here <was and here<davyd:
        return here
    else:
        return was
n = int(input())
for i in range(0,n):
    a = input().split (" ")
    print(min(int(a[0]), int(a[1]), int(a[2])), " ")
#
#
#also the URL of the task for which the code was written: http://www.codeabbey.com/index/task_view/min-of-three