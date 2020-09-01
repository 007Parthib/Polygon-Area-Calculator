class Rectangle:
  
  def __init__(self, width, height):
    self.width=width
    self.height=height
  
  def __str__(self):
    string='Rectangle'+'('+'width='+str(self.width)+', '+'height='+str(self.height)+')'
    return string

  def set_width(self, width):
    self.width=width
  
  def set_height(self, height):
    self.height=height

  def get_area(self):
    area=self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter
  
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  
  def get_picture(self):
    i=0
    string = ''
    if self.width<30: 
      while i<self.height:
        string+= ('*'*self.width)+'\n'  
        i+=1
    else:
      string+="Too big for picture."
    
    return string
  
  def get_amount_inside(self,different):
    x=self.get_area()
    y=different.get_area()
    return x//y
  
class Square(Rectangle):
  
  def __init__(self, side):
    self.width=side
    self.height=side

  def __str__(self):
    string='Square'+'('+'side='+str(self.width)+')'
    return string
  
  def set_side(self, side):
    self.width=side
    self.height=side
