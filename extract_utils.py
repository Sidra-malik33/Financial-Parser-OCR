import re

def extract_fields(text):
    text = text.replace('\n', ' ')  # flatten the text to avoid newlines breaking patterns

    date_pattern = r"(?:Invoice\s*date[:\s]*|Date[:\s]*)?((?:\d{1,2}[\/\-])?\d{1,2}[\/\-]\d{2,4}|[A-Za-z]{3,9}\s\d{1,2},?\s\d{4})"

    fields = {
        "invoice_number": re.findall(r"Invoice number[:\s]*([\d\-]+)", text, re.IGNORECASE),
        "invoice_date": re.findall(date_pattern, text, re.IGNORECASE),
        "total_amount": re.findall(r"Total.*?[€$]?\s?([0-9,]+\.\d{2})", text, re.IGNORECASE),
        "vendor": re.findall(r"(Google|Microsoft|Freelancer|Amazon|Zoho)", text, re.IGNORECASE),
    }

    return {k: v[0] if v else "Not Found" for k, v in fields.items()}
