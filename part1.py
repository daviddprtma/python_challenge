import re

def is_palindrome(date_str):
    digits = ''.join(filter(str.isdigit, date_str))
    no_zero = digits.replace('0', '')
    if no_zero != no_zero[::-1]:
        return False
    
    parts = [part for part in re.split(r'\D', date_str) if part]
    if len(parts) != 3:
        return False
        
    max_days_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if len(parts[0]) == 4:
        try:
            y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        except:
            return False
        if m < 1 or m > 12:
            return False
        if m == 2:
            leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            days_in_month = 29 if leap else 28
        else:
            days_in_month = max_days_list[m]
        if 1 <= d <= days_in_month:
            return True
        else:
            return False
    else:
        if len(parts[2]) == 0 or len(parts[2]) > 2:
            return False
        try:
            yy = int(parts[2])
        except:
            return False
        y = 1900 + yy if yy >= 70 else 2000 + yy
        
        try:
            d0 = int(parts[0])
            m0 = int(parts[1])
            if 1 <= m0 <= 12:
                if m0 == 2:
                    leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
                    days_in_month0 = 29 if leap else 28
                else:
                    days_in_month0 = max_days_list[m0]
                if 1 <= d0 <= days_in_month0:
                    return True
        except:
            pass
            
        try:
            m1 = int(parts[0])
            d1 = int(parts[1])
            if 1 <= m1 <= 12:
                if m1 == 2:
                    leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
                    days_in_month1 = 29 if leap else 28
                else:
                    days_in_month1 = max_days_list[m1]
                if 1 <= d1 <= days_in_month1:
                    return True
        except:
            pass
            
    return False

print(is_palindrome("25/5/25"))  
print(is_palindrome("5-25-25"))  
print(is_palindrome("3333|03|03")) 
print(is_palindrome("29-9-92"))