import random


Settings.SlowMotionDelay = 0.5
Settings.DelayBeforeMouseDown = 0.3
Settings.DelayBeforeDrop = 0.3
Settings.MoveMouseDelay = 2
Settings.ClickDelay = 0.5

reg = Region(0,24,1029,788)

base = "1566103379648.png"
ms1 = "1570978733528.png"
trainer = "trainer.png"
trainer_dlg = "trainer_dlg.png"
open_train_btn = "open_train_btn.png"
training_win = "training_win.png"
physical_attack_item = "physical_attack_item.png"
magic_item = "magic_item.png"
magic_protect_item = "1571132720304.png"
physical_protect_item = "physical_protect_item.png"
train_btn = "train_btn.png"
congrat_win = "congrat_win.png"

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
    while (xx > 0.5 or yy > 0.5) and ind < 10:
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
    region.mouseDown(Button.LEFT)
    wait(random.uniform(0.15,0.25))
    region.mouseUp(Button.LEFT)


def hoverObj(region, obj):
    tar_mats = region.findAllList(obj)
    if len(tar_mats):
        tar_loc = tar_mats[0].getTarget()
        adjustMouse(tar_loc)

def isDisplayed(region,obj):
    tar_mats = region.findAllList(obj)
    return len(tar_mats)

    
def clickObjIfDisplayed(region, obj):
    tar_mats = region.findAllList(obj)
    if len(tar_mats):
        tar_loc = tar_mats[0].getTarget()
        adjustMouse(tar_loc)
        clickCurrentPoint(region)

def clickObj(region, obj):
    hoverObj(region, obj)
    clickCurrentPoint(region)

def getCentre(region, point):
    base_reg = region.findAllList(point)[0]
    return Location(base_reg.x + base_reg.w/2, 
        base_reg.y + base_reg.h/2)

def getOffset(region, start_point, end_point):
    start_centre = getCentre(region, start_point)
    end_centre = getCentre(region, end_point)
    return (end_centre.x - start_centre.x, 
            end_centre.y - start_centre.y)


click("1566101126223.png")

# clickObj(reg, trainer)
# reg.wait(trainer_dlg,3)
# clickObj(reg, open_train_btn)
# reg.wait(training_win,3)
clickObj(reg, magic_item)
for i in range(9000):
    
    reg.wait(train_btn, 4)
    reg.wait(random.uniform(0.1,1.0))
    if i == 0:
        clickObj(reg, train_btn)
    else:
        clickCurrentPoint(reg)
    wait(random.uniform(1.1,1.5))
    if (isDisplayed(reg, congrat_win)):
        clickObj(reg, congrat_win)
        reg.wait(train_btn, 5)
        reg.wait(random.uniform(0.1,1.0))
        clickObj(reg, train_btn)

          
        
        




