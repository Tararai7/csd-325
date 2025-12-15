# ==============================================================
# Student Name: Tara Rai
# Assignment: M2 — Documented Debugging + Flowchart
# Course: CSD-325
# Date: December 14, 2025
# Description: Password strength checker with intentional bug
#              for debugging practice (NameError: 'length' undefined).
# ==============================================================

def check_password_strength(password):
    # Check minimum length first
    if len(password) < 8:
        return "Weak: Too short"
    
    # Check for uppercase letter and digit
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    # Initialize strength score
    score = 0
    
    # ❌ INTENTIONAL BUG: 'length' is not defined!
    #    Should be: if len(password) >= 8:
    if length >= 8:   # <-- NameError will occur here during debugging
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1

    # Determine final strength level
    if score == 3:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"


def main():
    # Test with empty string to trigger the bug
    user_input = ""
    result = check_password_strength(user_input)
    print("Password strength:", result)


if __name__ == "__main__":
    main()