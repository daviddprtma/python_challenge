import re

def is_palindrome(date_str):
    parts = re.split(r'\D+', date_str)
    parts = [p for p in parts if p]

    if not is_valid_date(parts):
        return False

    processed_parts = []
    for p in parts:
        stripped = p.lstrip('0')
        if not stripped:
            stripped = '0'
        processed_parts.append(stripped)
    concatenated = ''.join(processed_parts)
    return concatenated == concatenated[::-1]

def is_valid_date(parts):
    if len(parts) != 3:
        return False

    # Check YYYY-MM-DD format
    if len(parts[0]) == 4 and parts[0].isdigit():
        year_str, month_str, day_str = parts
        try:
            year = int(year_str)
            month = int(month_str)
            day = int(day_str)
        except ValueError:
            pass
        else:
            if year < 1 or month < 1 or month > 12 or day < 1:
                return False

            if month in (4, 6, 9, 11):
                max_day = 30
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_day = 29
                else:
                    max_day = 28
            else:
                max_day = 31

            if day > max_day:
                return False
            return True

    valid = False
    # Try DD-MM-YY format
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        pass
    else:
        if 1 <= month <= 12:
            if month in (4, 6, 9, 11):
                max_day = 30
            elif month == 2:
                max_day = 28  # Assume non-leap year for two-digit year
            else:
                max_day = 31
            if 1 <= day <= max_day:
                valid = True

    if not valid:
        # Try MM-DD-YY format
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        except ValueError:
            pass
        else:
            if 1 <= month <= 12:
                if month in (4, 6, 9, 11):
                    max_day = 30
                elif month == 2:
                    max_day = 28
                else:
                    max_day = 31
                if 1 <= day <= max_day:
                    valid = True

    return valid

# test case
print (is_palindrome('25/5/25'))
print (is_palindrome('5-25-25'))
print (is_palindrome('3333|03|03'))
print (is_palindrome('31-11-13'))