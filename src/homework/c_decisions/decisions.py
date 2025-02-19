#
def get_options_ratio(option, total):
 """returns the ratio of option divided by total"""
 ratio = option/total
 return ratio 

def get_faculty_rating(ratio):
 """returns faculty rating based on ratio"""
 if ratio <= 1 and ratio > 0.9 :
  return ("Excellent")
 elif ratio > 0.8 :
  return ("Very Good")
 elif ratio > 0.7 :
  return ("Good")
 elif ratio > 0.6:
  return ("Needs Improvement")
 elif ratio <= 0.59:
  return ("Unacceptable")
 
  
   
 
 


    
     