from timer import Timer
def test_start():
    #setup
    timer = Timer()
    #execute
    timer.start()
    #verify
    assert timer.is_running()
    assert timer.get_ticks() == 0
    