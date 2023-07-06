import os
import resend

resend.api_key = os.environ.get("re_fzjDNHxM_KB6PXpmZXwD1i3jN1NFqg8gB")

params = {
    "from": "Acme <log@resend.dev>",
    "to": ["tboymaroga7@gmail.com"],
    "subject": "Hello world",
    "html": "<strong>It works!</strong>"
}

email = resend.Emails.send(params)
print(email)