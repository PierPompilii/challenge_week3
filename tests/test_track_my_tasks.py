from lib.track_my_tasks import *

def test_track_my_tasks_not_done():
    notdone = track_my_tasks("take the trash out: #TODO")
    assert notdone == "A task is pending"

def test_track_my_tasks_done():
    done = track_my_tasks("shopping grocerys")
    assert done == "Task Done"


def test_track_my_tasks_one_done_other_not():
    only_one = track_my_tasks("take the trash out: #TODO, shopping grocerys: #Done")
    assert only_one == "A task is pending"

# I belive I want to code function beyond my posibilitys
#with the knowladge I know and thats why i feel this is why i failed this exercies?
# thank you 