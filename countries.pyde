add_library('controlP5')

countries = []
feature_0 = ""
feature_1 = ""
countryName = ""
w = 2048
h = 1024
cp5 = None
feature_list = []
current_feature_1 = 3
current_feature_2 = 4
map_image = 1
button_x = 10
button_y = 700

droplist = None 
droplist2 = None


centerX = 0
centerY = 0
offsetX = 0
offsetY = 0
zoom = 1

def setup():
    global cp5
    size(w,h)
    readData(current_feature_1,current_feature_2)
    labelFont = loadFont("ACaslonPro-Bold-48.vlw")
    textFont(labelFont, 32)
    cp5 = ControlP5(this)
    add_droplist()
    switch_map = cp5.addButton("switch map")
    switch_map.setPosition(button_x,button_y)
    switch_map.setSize(280,20)     
    switch_map.addListener(switch_mapListener)
    
    switch_features = cp5.addButton("<->")
    switch_features.setPosition(button_x+280,button_y+30)
    switch_features.setSize(20,20)
    switch_features.addListener(switch_featuresListener)
    
    xyplot = cp5.addButton("scatter chart")
    xyplot.setPosition(button_x+300,button_y)
    xyplot.setSize(280,20)  
    xyplot.addListener(showXY)

def draw():
    global centerX,centerY,offsetX,offsetY,zoom
    colorMode(RGB, 255, 255, 255,255);
    background(0,0,0)
    if(mousePressed==True):
        centerX=mouseX-offsetX
        centerY=mouseY-offsetY
    translate(centerX,centerY)
    scale(zoom)
    
    img = loadImage("earth"+str(map_image)+".png")
    image(img,0,0)

    
    stroke(0, 255, 0)
    for country in countries:
        country.draw()
        
    scale(1/zoom)
    translate(-centerX,-centerY)
    
    colorMode(RGB, 255, 255, 255,255);
    noStroke()
    fill(200,200,200)
    if(not countryName==''):
        rect(0,0,600,120)
    rect(00,690,600,450)
    countries[0].drawBar()
    colorMode(RGB, 255, 255, 255,255);
    fill(0,0,0,255)
    text(countryName, 10, 35)
    text(feature_0, 10, 70)
    text(feature_1, 10, 105)
    
def readData(r,c):
    global feature_list, countries
    countries=[]
    lines = loadStrings("factbook.csv")
    feature_list = lines[0].split(",")[3:]
    print feature_list
    print "Loaded", len(lines), "lines"
    for line in lines[2:]:
        columns = line.split(",")
        for i in range(len(columns)):
            if columns[i] == "":
                columns[i] = "NaN"
        country = Country()
        country.name = columns[0]
        country.latitude = float(columns[1])
        country.longitude = float(columns[2])
        country.radius = float(columns[r])
        country.color_ = float(columns[c])
        
        countries.append(country)
            
    #Country.minRadius = min(countries, key=lambda country: country.radius).radius
    #Country.maxRadius = max(countries, key=lambda country: country.radius).radius
    #Country.minColor = min(countries, key=lambda country: country.color_).color_
    #Country.maxColor = max(countries, key=lambda country: country.color_).color_
    radiuslist = []
    colorlist = []
    for country in countries:
        if country.radius == country.radius:
            radiuslist.append(country.radius)
        if country.color_ == country.color_:
            colorlist.append(country.color_)
    Country.minRadius = min(radiuslist)
    Country.maxRadius = max(radiuslist)
    Country.minColor = min(colorlist)
    Country.maxColor = max(colorlist)
    if (Country.maxRadius+1)/(Country.minRadius+1) > 100 and Country.minRadius+1 >0 :
        Country.log_mode_1 = 1
    else:
        Country.log_mode_1 = 0
    if (Country.maxColor+1)/(Country.minColor+1) > 100 and Country.minColor+1 >0 :
        Country.log_mode_2 = 1
    else:
        Country.log_mode_2 = 0
    Country.feature_0 = lines[0].split(",")[r]
    Country.feature_1 = lines[0].split(",")[c]
    
    
class Country(object):
    minRadius, maxRadius = (0,0)
    minColor, maxColor = (0,0)
    feature_0 = ""
    feature_1 = ""
    log_mode_1 = 0
    log_mode_2 = 0
    
    
    def __init__(self):
        self.name = ""
        self.latitude = 0
        self.longitude = 0
        self.radius = 0
        self.color_ = 0

    @property
    def x(self):
        return map(self.longitude, -180, 180, 0, w)
    
    @property
    def y(self):
        return map(self.latitude, 90, -90, 0, h)
    
    @property
    def drawRadius(self):
        return map(self.radius, Country.minRadius, Country.maxRadius, 10, 100)
    
    @property
    def drawColor(self):
        return map(self.color_, Country.minColor, Country.maxColor, 100, 0)
    
    def draw(self):
        try:
            if( self.drawRadius == self.drawRadius and self.drawColor==self.drawColor):
                colorMode(HSB, 360, 100, 100, 255);
                fill(self.drawColor,100,100,150)
                ellipse(self.x, self.y, self.drawRadius, self.drawRadius)

 
        except Exception, e:
            print "Error drawing place at ({}, {}):{}".format(self.x, self.y, e)
    
    def drawBar(self):
        x_ = 10
        y_ = 930
        noStroke()
        colorMode(HSB, 360, 100, 100,255)
        for i in range(100):
            fill(100-i,100,100,255)
            rect(x_+150+2*i, y_+50, 2, 30)
        colorMode(RGB, 255, 255, 255, 255)
        fill(0,0,0,150)
        text(Country.minColor,x_,y_+75)
        text(Country.maxColor,x_+380,y_+75)
        text(Country.feature_1,x_,y_+30)
        
        colorMode(HSB, 360, 100, 100,255)
        fill(50,100,100,255)
        ellipse(x_+130,y_-70,10,10)
        ellipse(x_+165,y_-70,40,40)
        ellipse(x_+230,y_-70,70,70)
        ellipse(x_+325,y_-70,100,100)
        fill(0,0,0,150)
        text(Country.minRadius,x_,y_-60)
        text(Country.maxRadius,x_+380,y_-60)
        text(Country.feature_0,x_,y_-130)
    
    def distTo(self):
        return abs((self.x*zoom+centerX) - mouseX) ** 2 + abs((self.y*zoom+centerY) - mouseY) ** 2
            
def keyPressed():
    global zoom;
    if (keyCode == UP and zoom <= 2):
       zoom += 0.05;
    if (keyCode == DOWN and zoom >=0.5):
       zoom -= 0.05;
       


def mousePressed():
    global feature_0, feature_1, countryName,offsetX,offsetY
    offsetX = mouseX-centerX
    offsetY = mouseY-centerY
    minDist = 1.7976931348623157e+300
    rightCountry = countries[0]
    for country in countries:
        distance = country.distTo()
        if distance < minDist:
            minDist = distance
            rightCountry = country

    if minDist < 300:
        feature_0 = rightCountry.feature_0 + ":  " + str(rightCountry.radius)
        feature_1 = rightCountry.feature_1 + ":  " + str(rightCountry.color_)
        countryName = rightCountry.name

    print str(mouseX)+"  -   "+str(mouseY)
    print "   "+str(centerX)+ " -- "+str(centerY)
    
def add_droplist():
    global cp5, droplist, droplist2
    droplist = cp5.addDropdownList("feature1")
    droplist2 = cp5.addDropdownList("feature2")
    
    feature_cnt = 1
    for feature_name in feature_list:
        droplist.addItem(feature_name, feature_cnt)
        feature_cnt += 1
    droplist.setPosition(button_x,button_y+30)
    droplist.setSize(270,250)
    droplist.setOpen(False)
    droplist.setBackgroundColor(color(255, 0, 0))
    droplist.setBarHeight(20)
    droplist.setItemHeight(20)
    droplist.setScrollSensitivity(0.5) 
    droplist.addListener(droplistListener1)
    
    feature_cnt = 1
    for feature_name in feature_list:
        droplist2.addItem(feature_name, feature_cnt)
        feature_cnt += 1
    droplist2.setPosition(button_x+310,button_y+30)
    droplist2.setSize(270,250)
    droplist2.setOpen(False)
    droplist2.setBackgroundColor(color(255, 0, 0))
    droplist2.setBarHeight(20)
    droplist2.setItemHeight(20)
    droplist2.setScrollSensitivity(0.5) 
    droplist2.addListener(droplistListener2) 


def droplistListener1(event):
    global current_feature_1
    if event.isController():
        current_feature_1 = int(event.getValue()) + 3
        readData( current_feature_1,  current_feature_2)

def droplistListener2(event):
    global current_feature_2
    if event.isController():
        current_feature_2 = int(event.getValue()) + 3
        readData( current_feature_1,  current_feature_2)


def switch_mapListener(event):
    global map_image
    if map_image == 5:
        map_image = 1
    else:
        map_image += 1
        
def switch_featuresListener(event):
    global current_feature_1, current_feature_2
    tem = current_feature_1
    current_feature_1 = current_feature_2
    current_feature_2 = tem
    readData( current_feature_1,  current_feature_2)

    

    
    
def showXY(e):
    sk=XYSketch(countries)
    sw='--sketch-path=' + sketchPath(), ''
    PApplet.runSketch(sw,sk)

class XYSketch(PApplet):

    pw=1200
    ph=900
    
    def __init__(self, c):
        self.countries = c
        self.cx = []
        self.cy = []
        self.cxl = []
        self.cyl = []
        self.feature_0 = ''
        self.feature_1 =''
        self.countryName = ''

    
    def settings(p):
        p.size(XYSketch.pw, XYSketch.ph), p.smooth(3)
        print sketchPath()
        print(len(countries))
        
    def setup(p):
        p.frame.setTitle("scatters")
        labelF = p.loadFont("ACaslonPro-Bold-48.vlw")
        p.textFont(labelF, 32)
        print('log1'+str(Country.log_mode_1))
        print('log2'+str(Country.log_mode_2))
        for country in p.countries:

            p.cx.append( p.map(country.radius, Country.minRadius, Country.maxRadius,110,XYSketch.pw-100))
            p.cxl.append( p.map(p.log(country.radius+1), p.log(Country.minRadius+1), p.log(Country.maxRadius+1),110,XYSketch.pw-100))

            p.cy.append( p.map(country.color_, Country.minColor, Country.maxColor,XYSketch.ph-210,100))
            p.cyl.append( p.map(p.log(country.color_+1), p.log(Country.minColor+1), p.log(Country.maxColor+1),XYSketch.ph-210,100))
            
        
    def draw(p):
        p.background(160), 
        p.colorMode(RGB, 255, 255, 255,255)
        
        p.fill(0,0,0)
        p.text("Use button 1 and 2 to toggle log scale mode", XYSketch.pw/2, 30)
        
        p.fill(255,0,0)
        
        if(Country.log_mode_1==0):
            p.text(Country.feature_0, XYSketch.pw/2 -200, XYSketch.ph-150)
        else:
            p.text(Country.feature_0+" (in log scale)", XYSketch.pw/2 -300, XYSketch.ph-150)
        p.fill(0,0,255)
        if(Country.log_mode_2==0):
            p.text(Country.feature_1, 10, 70)
        else:
            p.text(Country.feature_1+" (in log scale)", 10, 70)
        p.stroke(0,0,0)
        p.strokeWeight(3)
        p.line(100,100,100,XYSketch.ph-200)
        p.line(100,XYSketch.ph-200,XYSketch.pw-100,XYSketch.ph-200)
        p.strokeWeight(1)
        p.ellipseMode(CENTER)
        p.stroke(255,255,255)
        p.fill(255,255,255)
        if (Country.log_mode_1==0 and Country.log_mode_2==0):
            for ii in range(len(countries)):
                p.ellipse(p.cx[ii],p.cy[ii],8,8)
        if (Country.log_mode_1==1 and Country.log_mode_2==0):
            for ii in range(len(countries)):
                p.ellipse(p.cxl[ii],p.cy[ii],8,8)
        if (Country.log_mode_1==0 and Country.log_mode_2==1):
            for ii in range(len(countries)):
                p.ellipse(p.cx[ii],p.cyl[ii],8,8)
        if (Country.log_mode_1==1 and Country.log_mode_2==1):
            for ii in range(len(countries)):
                p.ellipse(p.cxl[ii],p.cyl[ii],8,8)
                    
        if (not p.countryName==''):

            p.fill(0,0,0)
            p.text(p.countryName,100, XYSketch.ph-110)
            p.text(p.feature_0,100, XYSketch.ph-70)
            p.text(p.feature_1,100, XYSketch.ph-30)
        
    def keyPressed(p,e):

        if (p.key == '1'):
            Country.log_mode_1 = 1-Country.log_mode_1
        if (p.key == '2'):
            Country.log_mode_2 = 1-Country.log_mode_2
    
    def mouseMoved(p,e):
        minDist = 1.7976931348623157e+300
        rightCountry = countries[0]
        for ii in range(len(countries)):
            if (Country.log_mode_1==0 and Country.log_mode_2==0):
                pdistance = (p.cx[ii]-p.mouseX)**2+(p.cy[ii]-p.mouseY)**2
            if (Country.log_mode_1==1 and Country.log_mode_2==0):
                pdistance = (p.cxl[ii]-p.mouseX)**2+(p.cy[ii]-p.mouseY)**2
            if (Country.log_mode_1==0 and Country.log_mode_2==1):
                pdistance = (p.cx[ii]-p.mouseX)**2+(p.cyl[ii]-p.mouseY)**2
            if (Country.log_mode_1==1 and Country.log_mode_2==1):
                pdistance = (p.cxl[ii]-p.mouseX)**2+(p.cyl[ii]-p.mouseY)**2
                
            if pdistance < minDist:
                minDist = pdistance
                rightCountry = countries[ii]

        if minDist < 200:
            p.feature_0 = rightCountry.feature_0 + ":  " + str(rightCountry.radius)
            p.feature_1 = rightCountry.feature_1 + ":  " + str(rightCountry.color_)
            p.countryName = rightCountry.name
        else:
            p.feature_0=''
            p.feature_1=''
            p.countryName=''
        
    def exit(p):
        return
