from pomobot.timer import Timer
def test_start_initializes_vars_properly():
    #setup
    timer = Timer()
    #execute
    timer.start()
    #verify
    assert timer.is_running()
    assert timer.get_ticks() == 0

def test_init_initializes_vars_properly():
    timer = Timer()
    assert timer.is_running()
    assert timer.get_ticks() == 0   
    
def test_tick_increases_ticks():
    timer = Timer()
    timer.start()
    timer.tick()
    assert timer.is_running()
    assert timer.get_ticks() == 1
