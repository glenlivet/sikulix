Settings.SlowMotionDelay = 0.5
Settings.DelayBeforeMouseDown = 0.3
Settings.DelayBeforeDrop = 0.3
Settings.MoveMouseDelay = 2
Settings.ClickDelay = 0.5

defaultSimi = Settings.MinSimilarity

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

# 6
shop_6 = "shop_6.png"
# 8
shop_8 = "shop_8.png"

Settings.MinSimilarity = 0.8

# 6 -> 8 offset 
six_to_eight_offset = getOffset(reg, shop_6, shop_8)
print "x: " + str(six_to_eight_offset[0]) + "; y: " + str(six_to_eight_offset[1])
# hover 8
hoverObj(reg, shop_8)
# move to shop 10
# moveMouse(reg, six_to_eight_offset[0], 
   #     six_to_eight_offset[1])

# move to shop 9
moveMouse(reg, six_to_eight_offset[0]/2, 
        six_to_eight_offset[1]/2)
# click
clickCurrentPoint(reg)

# niutou
niutou_sku = "niutou_sku.png"
clickObj(reg, niutou_sku)
buy_btn = "buy_btn.png"
clickObj(reg, buy_btn)

        



          
        
        




