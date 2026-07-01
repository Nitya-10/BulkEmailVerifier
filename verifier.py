import re
import dns.resolver

EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'


def verify_email(email):

    email = str(email).strip()

    if not re.match(EMAIL_REGEX,email):
        return "Bounce"

    domain=email.split("@")[1]

    try:

        dns.resolver.resolve(domain,"MX")

    except dns.resolver.NXDOMAIN:

        return "Bounce"

    except dns.resolver.NoAnswer:

        return "Bounce"

    except dns.resolver.Timeout:

        return "Unknown/Error"

    except:

        return "Unknown/Error"

    return "Valid"