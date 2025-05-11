from pomobot.timer import Timer, TimerStatus


def test_init_initializes_vars_properly():
    timer = Timer()
    assert timer.get_status() == TimerStatus.INITIALIZED
    # assert not timer.is_running()
    assert timer.get_ticks() == 0


def test_start_initializes_vars_properly():
    # setup
    timer = Timer()
    # execute
    timer.start(max_ticks=0)
    # verify
    assert timer.get_status() == TimerStatus.RUNNING
    assert timer.get_ticks() == 0


def test_tick_increases_ticks():
    timer = Timer()
    timer.start(max_ticks=2)
    timer.tick()
    assert timer.get_status() == TimerStatus.RUNNING
    assert timer.get_ticks() == 1


def test_tick_will_expire_when_it_reaches_max_ticks():
    timer = Timer()
    timer.start(max_ticks=2)
    timer.tick()
    assert timer.get_status() == TimerStatus.RUNNING
    assert timer.get_ticks() == 1
    timer.tick()
    assert timer.get_status() == TimerStatus.EXPIRED
    assert timer.get_ticks() == 2
