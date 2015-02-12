New Account
------

For new account must be created a mail verification template, for this you should follow this steps:

1.- Go to admin panel (url:port/admin)
2.- Find Email_templates 
3.- add new email
4.- Add something like this (you can modify it):

- (Codice) Code: verify-account 
- (Oggetto) Subject : Verify Account 
- (Testo) Text: 
Hi {{ user.first_name }} {{ user.last_name }},
click on the link below in order to verify your email address

{{ token.get_url }}

sincerly
Ep2015 Team


With this you should be able to create new accounts.
