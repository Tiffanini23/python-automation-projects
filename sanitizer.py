"""
Email Sanitizer Pro
A professional utility to clean, validate, and de-duplicate email lists.
"""

def is_valid_email(email):
    """
    Validates format and filters common domain typos.
    """
    if '@' not in email or '.' not in email:
        return False
    
    # Domain typo blacklist (Add more as needed)
    banned_typos = ["gmial.com", "yaho.com", "gnail.com", "hotmial.com", "outlok.com"]
    for typo in banned_typos:
        if email.endswith(typo):
            return False
            
    return True

def clean_email_list(raw_data):
    """
    Standardizes casing, removes whitespace, and filters duplicates.
    """
    cleaned_emails = []
    for entry in raw_data:
        # Data Cleaning: remove spaces and lowercase everything
        clean_entry = entry.strip().lower()
        
        # Validation and De-duplication
        if is_valid_email(clean_entry) and clean_entry not in cleaned_emails:
            cleaned_emails.append(clean_entry)
            
    return sorted(cleaned_emails) # Returns an organized A-Z list

def save_to_disk(results, filename="cleaned_emails.txt"):
    """
    Writes the final list to a permanent text file.
    """
    with open(filename, "w") as f:
        for email in results:
            f.write(email + "\n")

if __name__ == "__main__":
    # Sample data for testing purposes
    test_emails = [
        "  Alice@gmail.com ", 
        "bob@gmial.com",      # Typo: Should be filtered
        "ALICE@gmail.com",    # Duplicate: Should be filtered
        "info@business.co.uk", 
        "user@yaho.com"       # Typo: Should be filtered
    ]

    print("--- Initializing Email Sanitizer ---")
    processed_list = clean_email_list(test_emails)
    
    # Save the professional output
    save_to_disk(processed_list)
    
    print(f"Success! {len(processed_list)} clean emails exported to file.")
