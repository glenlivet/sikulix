Settings.SlowMotionDelay = 0.5
Settings.DelayBeforeMouseDown = 0.3
Settings.DelayBeforeDrop = 0.3
Settings.MoveMouseDelay = 2
Settings.ClickDelay = 0.5

click("1566088969022.png")
reg = Region(0,48,1024,763)
xl_btn = "1566057576783.png"
ms1 = "1566094758052.png"
xl_mat = reg.findBest(xl_btn)
xl_loc = xl_mat.getTarget()

hover(xl_btn)
wait(1)

ms_mat = reg.findBest(ms)
ms_loc = ms_mat.getTarget()

x_offset = xl_loc.getX() - ms_loc.getX()
y_offset = xl_loc.getY() - ms_loc.getY()
print (x_offset,y_offset)

mouseMove(x_offset, y_offset)
mouseDown(Button.LEFT)
mouseUp(Button.LEFT)



