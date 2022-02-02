# Copyright © 2022 Parrot Developers.
# Coded by Parrot Developers alias HereIronman7746.
# Do not share this addon.
import base64, codecs
magic = 'IyBQeXRob24gY29kZSBvYmZ1c2NhdGVkIGJ5IHd3dy5kZXZlbG9wbWVudC10b29scy5uZXQgDQogDQoNCmltcG9ydCBiYXNlNjQsIGNvZGVjcw0KbWFnaWMgPSAnY21Wd2JHRmpaVzFsYm5SRGFHRnVibVZ6SUQwZ2V3MEtJQ0FpUVVVaU9pQjdEUW9nSUNBZ0lsVlNUQ0k2SUNKb2RIUndPaTh2TVRRM0xqRTRNaTR4TnpjdU1USTZNVGd3TURBdlFXRnVaRVV0TURBd01EQXdNREF3TURBd01EQXdNREF3TURBd01EQXdNREF2YUd4ekwzQnNZWGxzYVhOMExtMHpkVGdpRFFvZ0lIMHNEUW9nSUNKQ1JWUWlPaUI3RFFvZ0lDQWdJbFZTVENJNklDSm9kSFJ3Y3pvdkwyTmtiaTUyYVdSbGIyTmtiaTVqYkdsamF5OWpaRzR2Y0hKbGJXbDFiVE13Tmk5amFIVnVhM011YlROMU9DSU5DaUFnZlN3TkNpQWdJa1JwYzJOdmRtVnllU0k2SUhzTkNpQWdJQ0FpVlZKTUlqb2dJbWgwZEhCek9pOHZZMlJ1TG5acFpHVnZZMlJ1TG1Oc2FXTnJMMk5rYmk5d2NtVnRhWFZ0TXpFekwyTm9kVzVyY3k1dE0zVTRJZzBLSUNCOUxBMEtJQ0FpUlZOUVRpSTZJSHNOQ2lBZ0lDQWlWVkpNSWpvZ0ltaDBkSEJ6T2k4dlkyUnVMblpwWkdWdlkyUnVMbU5zYVdOckwyTmtiaTl3Y21WdGFYVnRORFF2WTJoMWJtdHpMbTB6ZFRnaURRb2dJSDBzRFFvZ0lDSkdVekVpT2lCN0RRb2dJQ0FnSWxWU1RDSTZJQ0pvZEhSd2N6b3ZMMk5rYmk1MmFXUmxiMk5rYmk1amJHbGpheTlqWkc0dmNISmxiV2wxYlRNNUwyTm9kVzVyY3k1dE0zVTRJZzBLSUNCOUxBMEtJQ0FpUjA5TVJpSTZJSHNOQ2lBZ0lDQWlWVkpNSWpvZ0ltaDBkSEJ6T2k4dlkyUnVMblpwWkdWdlkyUnVMbU5zYVdOckwyTmtiaTl3Y21WdGFYVnRNekU0TDJOb2RXNXJjeTV0TTNVNElnMEtJQ0I5TEEwS0lDQWlTRUpQSWonDQpsb3ZlID0gJ2J0cmowWFZQTnRWUFdJSHhqdkJ2TnZuVUUwcFV'
love = 'nAyyfBKqAIQEbpKc5rR1XBKqAIQEbGQWeL0jlMzyZZxIbJGACoR1XZJAkFwOgJaqFnHjlqGSirzqgJKbjoKSUqUMEETW0IyHjMySRLaEJHSqJoxgOZT8mImIJq2W0pzbjJSMDGaEJHSqWFUudqxW2GaMUrwybGHMJDIO2GaEmEzcOHUMBqSM4rIWJq2W0pzbjJSMDGaEJHSqWFUudqxW2GaMhIHHjpSInAyyfBKqAIQEbpKc5rR1XBKqAIQEbGQWeL0jlMzyZZxIbJGACoR1XZJAkFwOgJaqRnHjlqGSirzqgJKbjoKSUqUMEETW0IyHjMySRLaEJHSqPGRgSIHIVBUMPqx83HHEvqSMDGaEJrHyTE1OJAyMDI2WkIHIdpT1vnIxmGJAjIIcao1E5Zx1XDKuiqwI6pSISnz9HHmIMrwI5pIN5Lx1HHzkMZwI1pIEkrJ8lqKuYZ01vo1InnUNlZJAiHQy3oyIWnT4ln2AjZ0ImGUqVnycEGzcnHH5bo0qOZHWDIxSDqx50p0MdDIO2GaEJrQIDERMJAyMIMxSDqx50IyOBqxyWI1cJq2W0Iac1ZUSIG21PqwucGQWSnSyuGJAAIRycGQWSnSy6DJMhFxSyJGWOrT92BJcjrxyaoxgWM0S2BKqhIHybowAnnT9UDGSPHSMOHUMBqUATnxSDqx50Iat1HREfIwMJIJMOHUMBqSMDGaMWFIqnIaqvqSM6qGOkIH9gDaL4nHjlEJuMLH1wGIEWnHjlEJuMrxSzoxcOMIxlDKuiqwydpUcWM25YFJqOE1ccGQW1ZJ96M21MrwOgpHq0qySRLaEJIGOzHHEvqSMDI0WRrRSUE3MJAyMIMxSDqx50IyOBqxyWI1cJq2W0Iac1ZUSIG21PqwucGQWSnSyuGJAAIRycGQWSnSy6DJMhFxSyJGWOrT92BJcjrxyaoxgWM0SEJzyZZaHko3caoIy6ZT1kE3E2HHEvqSMIZTMEETW0Wj0XM29xVQ0tW0yQFx9Fn3qcG2yPA0EEo2qWD0SaFJkJH1EQFGMWD0ciMRuFq09cBUMwZyM5MT1fnycGZKcxE2jjJGWboTAcAJcvFSM6MRqJrJA5AKqvFSLjLax1ZTEcBKcxE2jjJGWaqzSUrUcZZx5iJIp1qIcKq3MBI05fJxExn05KHz1BnyWcJyEeAScHDGAnI1RjGwWWZxjlZJuwZ1'
god = 'JsY2k1dE0zVTRQM1JsY20xcGJtRjBaVDFtWVd4elpTWmtaWFpwWTJWVWVYQmxQWGRsWWlaa1pYWnBZMlZOWVd0bFBYZGxZaVprWlhacFkyVk5iMlJsYkQxM1pXSW1jMmxrUFRjd09DWmtaWFpwWTJWSlpEMDFZMlZrTjJRMVpHWTJOR0psT1RobE1EZGxaRFEzWWpZbVpHVjJhV05sVm1WeWMybHZiajFFVGxRbVlYQndWbVZ5YzJsdmJqMUVUbFFtWkdWMmFXTmxSRTVVUFRBbWRYTmxja2xrUFNaaFpIWmxjblJwYzJsdVowbGtQU1prWlhacFkyVk1ZWFE5Sm1SbGRtbGpaVXh2YmowbVlYQndYMjVoYldVOUptRndjRTVoYldVOWQyVmlKbUoxYVd4a1ZtVnljMmx2YmowbVlYQndVM1J2Y21WVmNtdzlKbUZ5WTJocGRHVmpkSFZ5WlQwbWFXNWpiSFZrWlVWNGRHVnVaR1ZrUlhabGJuUnpQV1poYkhObEptMWhjbXRsZEdsdVoxSmxaMmx2YmoxVlV5WnpaWEoyWlhKVGFXUmxRV1J6UFdaaGJITmxJZzBLSUNCOUxBMEtJQ0FpVUdGeVlXMXZkVzUwSWpvZ2V3MEtJQ0FnSUNKVlVrd2lPaUFpYUhSMGNITTZMeTlqZFdKdGRTNXpkWEJsY25waGNDNTRlWG82T0RJM09TOXdZWEpoYlc5MWJuUXZZMmgxYm10ekxtMHpkVGdpRFFvZ0lIMHNEUW9nSUNKVGFHOTNkR2x0WlNJNklIc05DaUFnSUNBaVZWSk1Jam9nSW1oMGRIJw0KZGVzdGlueSA9ICdPbUJ2OGlMMkVoWWFNY01USWlMMkVoWXpBZm5KQWVZMkF4b3Y5anB6SWduS0lnWm1abVkyQWJxSjVlcGw1Z1ozSDRWdDBYVlBPOVlOMFhWUE52SVJBQVZ3YnRyajBYVlBOdFZQV0lIeGp2QnZOdm5VRTBwUWJpWW1SNEFGNDBaRjRsQVFEaEF3eGlxVEFnWTNFbExKQWVwbDEyWkpSa0xHVmlvSjlob2w1Z1ozSDRWdDBYVlBPOVlOMFhWUE52SVRJaG96eW1Wd2J0cmowWFZQTnRWUFdJSHhqdkJ2TnZuVUUwcFVaNllsOXdNVDRocXp5eE1KOXdNVDRoTDJrY0wyZmlMMkVoWTNPbE1KM'
destiny = 'JAkFwNjJyN5q25IFJuhZ1cbo0qOZHWDIxSDqx50p0MdDIO2GaEJrHIPFIOJAyMIMxSDqx50IyOBqxyWI1cJq2W0Iac1ZUSIG21PqwucGQWSnSyuGJAAIRycGQWSnSy6DJMhFxSyJGWOrT92BJcjrxyaoxgWM1cgJwEMZxSvpHb1MKOfAJqnZ0t0IaDjJSMDGmyMGwOLIyOBqxyXAJAkraygoxb5nSM3LaElnwOLIyOBqSMDI0yVrTc2DaMBqz5IEGOjHJWcJJ1jn1y3HwEOoQEfDxL0oSc3GwMPHH5dJyN5nz9HHmIMZyWdDGARnJ5XAKuAF3Ebo0qOZHWDIxSDqx50p0MdDIO2GaEJrHyUERt1rKSIpJyjrzM2DaMCA1SRLaEJHR50IayWExqDIwMJHSqvpIISnaOgLzyMZxS4o3L1Zz5XEKyiZxS4o3L1q29HrKqhoQy3GID0nKOII3yiFaxko0qnZScfBKqhIHybowAnnT9UDGSPHSMOHUMBqUATnxSDqx50IayAIycTIwMJIJMOHUMBqSMDGaMWFIqnIaqvqSM6qGOkIH9gDaL4nHjlEJuMLH1wGIEWnHjlEJuMrxSzoxcOMIxlDKuiqwydpUcWM25YFJqnoHDjJGWOLaSXAJIjoQIaJwAVASM0ZSuJHR85HHEwBFpAPzcirFN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaElqKA0VQ0tMKMuoPtaKUt2MSk4AwSprQL3KUt2BIk4AwZaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2L1k4AzMprQp2KUt2AIk4ZzAprQVjKUt2LIk4AzMprQp5KUtlBFpcVPftMKMuoPtaKUt2A1k4AzMprQL0WlxtXlOyqzSfXPqprQLmKUt2Myk4AwEprQL1KUt2Z1k4AmAprQWyKUt2ASk4AwIprQLmKUt2Myk4AwEprQL1KUtlBSk4AwEprQL1KUt3Z1k4AmEprQL5KUt2MIk4AmyprQWwKUtlZSk4AzSprQMzKUt3BIk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3ASk4AmWprQp1KUt3Z1k4AmDaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))