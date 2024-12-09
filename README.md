# path_planning_salwa
# מטלה להגשת מועמדות לצןןת האוטונומיה לbgu_racing
# Path Planning Assignment 2

# המטלה הזאת היא להגשת מועמדות לצוות הפורמולה באוניברסיטת בן גוריון והמטרה שלה היא לתכנן נתיב עבור רכב בין קונוסים כלומר עיבוד נתונים ויצירת הנתיב עם חישובים מתמטיים

# השלבים עד שעשיתי את המטלה
# הקוד כתוב בפייתון עם השתמשות בnumpy, sciPy, Matplotlib, Pandas
# בהתחלה עשיתי קריאה וניקוי של נתוני הקונוסים כי בקובץ CSV כל שורה מייצגת קונוס עם המיקום X ו Y שלו שמאל או ימין
#import pandas as pd לטיפול בנתונים כלומר קריאה וניקוי של הCSV (לקרוא קובץ הread_CSV)
#import numpy as np לחישובים מתמטיים
#import matplotlib.pyplot as plt ליצירת גרפים דו-ממדיים
#from scipy.interpolate import CubicSpline לעשות נתיב חלק בין הנקודות
# וקראתי את קובץ הCSV שיש בו המידע על הקונוסים והמיקום של כל קונוס בציר הX ובציר הY 
#data = pd.read_csv('BrandsHatchLayout.csv')
#data_cleaned = data.dropna() מנקה נתינים חסרים/שורות חסרות/שגויות 
# אחר כך חילקתי את הקונוסים לצד שמאל וימין
# left_cones = data_cleaned[data_cleaned['side'] == 'left']
#right_cones = data_cleaned[data_cleaned['side'] == 'right'] מסנן את הנתונים לפי עמודת side
#x_left = left_cones['x'].values
#y_left = left_cones['y'].values מקומי הקונוסים בצד שמאל
#x_right = right_cones['x'].values
#y_right = right_cones['y'].values מקומי הקונוסים בצד ימין
# אחר כך חישבתי את הנתיב האמצעעי כלומר עשיתי ממוצע לצד השמאלי והימני
# x_center = (x_left + x_right) / 2
#y_center = (y_left + y_right) / 2
#centerline_data = pd.DataFrame({'x': x_center, 'y': y_center}).sort_values(by='x') וסידרתי נתיב האמצע בסדר עולה
#x_center_sorted = centerline_data['x'].values
#y_center_sorted = centerline_data['y'].values
#לאחר מכך עשיתי נתיב חלק כלומר חיברתי את כל נקודות נתיב האמצע בצורה חלקה
# אחר כך חישבתי הפונקציה של שינוי השיפוע לאורך הנתיב כלומר עשיתי נגזרות ראשונות ונגזרות שניות ל X ו Y 
#ויצרתי גרף בסיסי כך שהכחול הוא צד שמאל והימין הוא האדום ונתיב האמצע החלק בירוק
# ו עשיתי גרף לשינוי העקמומיות לאורך נתיב האמצע שהעקמומיות היא השיפוע לאורך הנתיב של X ו Y
# ויצרתי המחשה ריאליסטית עם רקע שמדמה כביש ומשולשים בצבע כחול ואדום שמדמים קונוסים ונתיב ירוק עם נקודות התחלה וסיום
# בכך סיימתי את העבודה 
# תוצרים:
# centerline_plot.png למחשה ריאליסטית של מסלול הנהיגה עם קונוסים ונתיב
#curvature_plot.png curvature_plot.png
# realistic_centerline_plot.png המחשה ריאליסטית של מסלול הנהיגה עם קונוסים ונתיב

#איך להתקין את המטלה
# ספריות בשימוש: matplotlib, numpy, scipy, pandas
# שיבצו את הפרויקט בתיקייה מקומית במחשב שלכם
# התקינו את הספריות הנדרשות באמצעות הפקודה הבאה pip install -r requirements.txt
# ודאו שקובץ הCSVעם מיקומי הקונוסים נמצא בתיקיית הפרויקט אחר כך הריצו את הסקריפט לתכנון המסלול python path_planner.py
 ויפיק את התוצרים הבאים centerline_plot.png שהוא המחשה בסיסית לנתיב ו curvature_plot.png שהוא גרף העקמומיות לאורך הנתיב וגם realistic_centerline_plot.png  
# ודאו שקובץ BrandsHatchLayout.csv נמצא באותה תיקייה עם הקובץ path_planner.py
#בדקו את התמונות שהופקו 

#הקבצים הכלולים בתיקייה:
#path_planner.py הקוד הראשי לתכנון המסלול
# BrandsHatchLayout.csv קובץ מיקום הקונוסים
# README.md הקובץ הזה שהוא הסבר על המטלה 
# והקבצים הגרפיים centerline_plot.png, curvature_plot.png, realistic_centerline_plot.png

#סלא גיריס ת.ז. 214741761 salwaje@post.bgu.ac.il
