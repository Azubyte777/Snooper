from email_validator import validate_email, EmailNotValidError
 
def check(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        email = v["email"] 
        return True
    except EmailNotValidError as e:
        # Email is invalid
        print(str(e))
        return False