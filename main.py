# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from action import action
from baseUse import baseUse
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HOSTNAME = 'testapi.huxin315.com'
    Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2OTEzNzQ4NzIsInVzZXJJZCI6ImVERmxiZnRXV2dGb3RXUjYweEFjaGs3Zk1xTW1MNFhxS2xhQ3ZwQzlnUEdEV2N5TU9vcXBmVDlaSnAvamhua3dZRis4cnIrYXl3UE1iRHJFSVJVNTRQdXFqSnd0T055ZjFLRWM0YjlnQWNDSFRoL2taUURhQ2lLbFJqYUYvVHVGWXRvKzd6YTJRM3FGcjVxakhieEZ4Zk1SbHZkeWhZcWgvRmdtRFYwMUhtWT0iLCJpYXQiOjE2MDUwNjEyNzJ9.uG75en-_gnw2f53wsLMdV1ENozf_KGjUogv0mkUMXGGp8JoPv2ciUG2hPCiY2wuBzeVVMjDoXGO7X3jLvOplEN743b30KJ70hoY1IHmnZUhTmjf50lL81z9VAwEI7Y57HN_wL5C1RAy_fOOkcbbhQoH1vQyyxTt2hGeuszmn119skiKGWtlanqD4uLrITa96Zb0Nekp6x4aDgoPQAocDBgQewoGJb2SUY-2oOMCKIAxO7JTLbWnTv86W4_uSW3UBwt2Xw3vTcABzcrf9bLesAEaLslununszfZ5XwO_9XyFga49wigKjUfj2ZuprKtfxSfI9Udp7yVlAOJttXhu50g'
    #baseUse=baseUse(HOSTNAME, Authorization)
    action=action(HOSTNAME, Authorization)
    action.login()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
