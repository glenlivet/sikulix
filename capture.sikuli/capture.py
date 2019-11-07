Settings.SlowMotionDelay = 0.5
Settings.DelayBeforeMouseDown = 0.3
Settings.DelayBeforeDrop = 0.3
Settings.MoveMouseDelay = 2
Settings.ClickDelay = 0.5


reg = Region(0,48,1024,763)

base = "1566103379648.png"
ms1 = "1566095757337.png"


def moveMouse(region, xOffset, yOffset):
    region.mouseMove(xOffset,yOffset)
    wait(1.5)

def adjustMouse(origin_ms_loc):
    adjusted_loc = origin_ms_loc.offset(18,17)  # coused by pointer image.
    xx = 5
    yy = 5
    ind = 0

    reg.hover(adjusted_loc)
    wait(1.5)
    while (xx > 1 or yy > 1) and ind < 10:
        ind += 1
        temp_mats = reg.findAllList(ms1)
        if len(temp_mats):
            temp_ms_loc = temp_mats[0].getTarget()
            xx = adjusted_loc.getX() - temp_ms_loc.getX()
            yy = adjusted_loc.getY() - temp_ms_loc.getY()
            print "found. xx: " + str(xx) + ", yy: " + str(yy)
            moveMouse(reg, xx, yy)
        else:
            print "mouse not found."
            return

def clickCurrentPoint(region):
    region.mouseDown(Button.LEFT);
    region.mouseUp(Button.LEFT);


def hoverObj(region, obj):
    tar_mats = region.findAllList(obj)
    if len(tar_mats):
        tar_loc = tar_mats[0].getTarget()
        adjustMouse(tar_loc)

def clickObj(region, obj):
    hoverObj(region, obj)
    clickCurrentPoint(region)


shanzi = "shanzi.png"
zhuazi = "zhuazi.png"
qiang = "1566110605246.png"

wq_dlg = Region(366,216,284,420)

click("1566101126223.png")

clickObj(reg, shanzi)
wait(1)
hover(base)
wait(1)
capture(wq_dlg, "wqd_1")
clickObj(reg, zhuazi)
wait(1)
hover(base)
wait(1)
capture(wq_dlg, "wqd_2")
clickObj(reg, qiang)
wait(1)
hover(base)
wait(1)
capture(wq_dlg, "wqd_3")



          
        
        




