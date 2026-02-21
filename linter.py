import json
import re

with open("token.json") as f:
    tokens = json.load(f)


def check_tokens(code):
    errors = []

    if tokens["primaryColor"] not in code:
        errors.append("Primary color not used")

    if tokens["borderRadius"] not in code:
        errors.append("Border radius missing")

    if tokens["fontFamily"] not in code:
        errors.append("Font family missing")

    return errors


def check_brackets(code):
    if code.count("{") != code.count("}"):
        return ["Unbalanced curly brackets"]
    return []


def check_html_structure(code):
    open_div = len(re.findall(r"<div", code))
    close_div = len(re.findall(r"</div>", code))

    if open_div != close_div:
        return ["Unclosed <div> tag"]
    return []


def validate(code):

    errors = []
    errors.extend(check_tokens(code))
    errors.extend(check_brackets(code))
    errors.extend(check_html_structure(code))

    return errors

