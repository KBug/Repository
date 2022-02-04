# Copyright © 2022 Parrot Developers.
# Coded by Parrot Developers alias HereIronman7746.
# Do not share this addon.
import base64, codecs
magic = 'aW1wb3J0IHN5cwpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdXJsZW5jb2RlLCBwYXJzZV9xc2wKaW1wb3J0IHhibWNndWkKaW1wb3J0IHhibWMKaW1wb3J0IHhibWNwbHVnaW4KZnJvbSByZXNvdXJjZXMubGliLmdyYWIgaW1wb3J0IGdyYWIKZnJvbSByZXNvdXJjZXMubGliLk1vdmllcy5Nb3ZpZXMgaW1wb3J0IHNlYXJjaE1vdmllcywgY2luZW1hX21vdmllcywgbW92aWVzCmZyb20gcmVzb3VyY2VzLmxpYi5UVlNob3dzLlRWU2hvd3MgaW1wb3J0IHNlYXJjaFRWU2hvd3MsIGxpc3RFcGlzb2RlcywgdHZzaG93c3RhYiwgZmVhdHVyZWR0dnNob3dzdGFiCgoKX1VSTCA9IHN5cy5hcmd2WzBdCl9IQU5ETEUgPSBpbnQoc3lzLmFyZ3ZbMV0pCgoKCmRlZiBnZXRfdXJsKCoqa3dhcmdzKToKICAgIHJldHVybiAne30/e30nLmZvcm1hdChfVVJMLCB1cmxlbmNvZGUoa3dhcmdzKSkKCmRlZiBpbnB0KCk6CiAgICB4Ym1jcGx1Z2luLnNldENvbnRlbnQoX0hBTkRMRSwgJ3ZpZGVvcycpCiAgICBrYiA9IHhibWMuS2V5Ym9hcmQoJycsICJFbnRlciBrZXl3b3JkcyB0byBzZWFyY2ggZm9yIikKICAgIGtiLmRvTW9kYWwoKQogICAgcXVlcnkgPSAiIgogICAgaWYga2IuaXNDb25maXJtZWQoKToKICAgICAgICBxdWVyeSA9IGtiLmdldFRleHQoKQogICAgcmV0dXJuIHF1ZXJ5CgpkZWYgYWRkX2l0ZW1fdG9fc2NyZWVuKG5hbWUsIGdlbnJlLCBpY29uLCB1cmwsIGlzRm9sZGVyKToKICAgIGxpc3RfaXRlbSA9IHhibWNndWkuTGlzdEl0ZW0obGFiZWw9bmFtZSkKICAgIGxpc3RfaXRlbS5zZXRJbmZvKCd2aWRlbycsIHsndGl0bGUnOiBuYW1lLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdnZW5yZSc6IGdlbnJlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdwbG90JzogbmFtZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnbWVkaWF0eXBlJzogJ3ZpZGVvJ30pCiAgICBsaXN0X2l0ZW0uc2V0QXJ0KHsndGh1bWInOiBpY29uLCAnaWNvbic6IGljb24sICdmYW5hcnQnOiBpY29ufSkKICAgIGxpc3RfaXRlbS5zZXRQcm9wZXJ0eSgnSXNQbGF5YWJsZScsICd0cnVlJykKICAgIHhibWNwbHVnaW4uYWRkRGlyZWN0b3J5SXRlbShfSEFORExFLCB1cmwsIGxpc3RfaXRlbSwgaXNGb2xkZXIpCgpkZWYgaG9tZV9zY3JlZW4oKToKICAgIHhibWNwbHVnaW4uc2V0Q29udGVudChfSEFORExFLCAnSG9tZScpCiAgICB4Ym1jcGx1Z2luLnNldFBsdWdpbkNhdGVnb3J5KF9IQU5ETEUsICJIb21lIikKICAgIGFkZF9pdGVtX3RvX3NjcmVlbigiTW92aWVzIiwgIiIsICJodHRwczovL2kuaWJiLmNvL1BHQ2ZTOVMvTW92aWVzLnBuZyIsIGdldF91cmwoYWN0aW9uPSdNaG9tZScpLCBUcnVlKQogICAgYWRkX2l0ZW1fdG9fc2NyZWVuKCJTZXJpZXMiLCAiIiwgImh0dHBzOi8vaS5pYmIuY28vTlpIbTlHci9UVi1TaG93cy5wbmciLCBnZXRfdXJsKGFjdGlvbj0nVGhvbWUnKSwgVHJ1ZSkKICAgIHhibWNwbHVnaW4uZW5kT2ZEaXJlY3RvcnkoX0hBTkRMRSkKCgoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBNb3ZpZXMgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgpkZWYgTW92aWVzX2hvbWUoKToKICAgIHhibWNwbHVnaW4uc2V0Q29udGVudChfSEFORExFLCAnTW92aWVzIEhvbWUnKQogICAgeGJtY3BsdWdpbi5zZXRQbHVnaW5DYXRlZ29yeShfSEFORExFLCAiTW92aWVzIEhvbWUiKQogICAgYWRkX2l0ZW1fdG9fc2NyZWVuKCJTZWFyY2giLCAiIiwgImh0dHBzOi8vaS5pYmIuY28vTVBoUjByNy9TZWFyY2gucG5nIiwgZ2V0X3VybChhY3Rpb249J3NlYXJjaEVuZ2luZU0nKSwgVHJ1ZSkKICAgIGFkZF9pdGVtX3RvX3NjcmVlbigiQ2luZW1hIE1vdmllcyIsICIiLCAiaHR0cHM6Ly9pLmliYi5jby9tOEs1OWI0L0NpbmVtYS1Nb3ZpZXMucG5nIiwgZ2V0X3VybChhY3Rpb249J2NpbmVtYU1vdmllcycpLCBUcnVlKQogICAgYWRkX2l0ZW1fdG9fc2NyZWVuKCJNb3ZpZXMiLCAiIiwgImh0dHBzOi8vaS5pYmIuY2'
love = '8iBGyFJx1EGv9Ao3McMKZhpT5aVvjtM2I0K3IloPuuL3Eco249W21iqzyyplpcYPOHpaIyXDbtVPNtrTWgL3OfqJqcov5yozECMxEcpzIwqT9lrFusFRSBERkSXDbXPzEyMvOGMJSlL2uAo3McMKZbXGbXVPNtVUS1MKW5VQ0tnJ5jqPtcPvNtVPOcMvOkqJIlrFN9CFNvVvOipvOkqJIlrFN9CFOBo25yBtbtVPNtVPNtVR1iqzyyp19bo21yXPxXVPNtVPNtVPOlMKE1pz4XVPNtVUuvoJAjoUIanJ4hp2I0D29hqTIhqPusFRSBERkSYPNaGJ92nJImWlxXVPNtVUuvoJAjoUIanJ4hp2I0HTk1M2yhD2S0MJqipaxbK0uOGxEZEFjtVyWyp3IfqPOiMwbtVvNeVUS1MKW5XDbtVPNtpzImqJk0VQ0tp2IupzAbGJ92nJImXUS1MKW5XDbtVPNtMz9lVTxtnJ4tpzShM2HboTIhXUWyp3IfqPxcBtbtVPNtVPNtVT5uoJHtCFOlMKA1oUEonI0hp3OfnKDbWl0gYFpcJmOqPvNtVPNtVPNtqKWfVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIfkKDbtVPNtVPNtVTywo24tCFOlMKA1oUEonI0hp3OfnKDbWl0gYFpcJmWqPvNtVPNtVPNtLJExK2y0MJ1sqT9sp2AlMJIhXT5uoJHfVPVvYPOcL29hYPOaMKEsqKWfXTSwqTyiow0apTkurFpfVUMcMTIiCKIloPxfVRMuoUAyXDbtVPNtrTWgL3OfqJqcov5yozECMxEcpzIwqT9lrFusFRSBERkSXDbXPzEyMvOQnJ5yoJSsGJ92nJImXUOuM2H9ZFx6PvNtVPO4Lz1wpTk1M2yhYaAyqRAioaEyoaDbK0uOGxEZEFjtW01iqzyyplpcPvNtVPO4Lz1wpTk1M2yhYaAyqSOfqJqcoxAuqTIao3W5XS9VDH5RGRHfVPWQnJ5yoJRtGJ92nJImVvxXVPNtVUWyp3IfqPN9VTAcozIgLI9go3McMKZbpTSaMFxXVPNtVTMipvOcVTyhVUWuozqyXTkyovulMKA1oUDcXGbXVPNtVPNtVPOhLJ1yVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIfjKDbtVPNtVPNtVUIloPN9VUWyp3IfqSgcKF5mpTkcqPtaYF0gWlyoZI0XVPNtVPNtVPOcL29hVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIflKDbtVPNtVPNtVTSxMS9cqTIgK3EiK3AwpzIyovuhLJ1yYPNvVvjtnJAiovjtM2I0K3IloPuuL3Eco249W3OfLKxaYPO2nJEyom11pzjcYPOTLJkmMFxXVPNtVTSxMS9cqTIgK3EiK3AwpzIyovtvGzI4qPODLJqyVvjtVx5yrUDtHTSaMFVfVPWbqUEjpmbiY2xhnJWvYzAiYmIMM1uhFT0iGzI4qP5jozpvYPOaMKEsqKWfXTSwqTyiow0aL2yhMJ1uGJ92nJImHTSaMFpfVUOuM2H9pTSaMFNeVQRcYPOHpaIyXDbtVPNtrTWgL3OfqJqcov5yozECMxEcpzIwqT9lrFusFRSBERkSXDbXMTIzVR1iqzyyplujLJqyCGRcBtbtVPNtrTWgL3OfqJqcov5mMKEQo250MJ50XS9VDH5RGRHfVPqAo3McMKZaXDbtVPNtrTWgL3OfqJqcov5mMKEDoUIanJ5QLKEyM29lrFusFRSBERkSYPNvGJ92nJImVvxXVPNtVUWyp3IfqPN9VT1iqzyyplujLJqyXDbtVPNtMz9lVTxtnJ4tpzShM2HboTIhXUWyp3IfqPxcBtbtVPNtVPNtVT5uoJHtCFOlMKA1oUEonI0hp3OfnKDbWl0gYFpcJmOqPvNtVPNtVPNtqKWfVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIfkKDbtVPNtVPNtVTywo24tCFOlMKA1oUEonI0hp3OfnKDbWl0gYFpcJmWqPvNtVPNtVPNtLJExK2y0MJ1sqT9sp2AlMJIhXT5uoJHfVPVvYPOcL29hYPOaMKEsqKWfXTSwqTyiow0apTkurFpfVUMcMTIiCKIloPxfVRMuoUAyXDbtVPNtLJExK2y0MJ1sqT9sp2AlMJIhXPWBMKu0VSOuM2HvYPNvGzI4qPODLJqyVvjtVzu0qUOmBv8inF5cLzVhL28iAIyaJT5VoF9BMKu0YaOhMlVfVTqyqS91pzjbLJA0nJ9hCFqgo3McMKADLJqyWljtpTSaMG1jLJqyVPftZFxfVSElqJHcPvNtVPO4Lz1wpTk1M2yhYzIhMR9zETylMJA0o3W5XS9VDH5RGRHcPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZtISLtH2uiq3ZtVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwPtcxMJLtISMmnT93p19bo21yXPx6PvNtVPO4Lz1wpTk1M2yhYaAyqRAioaEyoaDbK0uOGxEZEFjtW1AypzyyplOVo21yWlxXVPNtVUuvoJAjoUIanJ4hp2I0HTk1M2yhD2S0MJqipaxbK0uOGxEZEFjtVyAypzyyplOVo21yVvxXVPNtVTSxMS9cqTIgK3EiK3AwpzIyovtvH2IupzAb'
god = 'IiwgIiIsICJodHRwczovL2kuaWJiLmNvL01QaFIwcjcvU2VhcmNoLnBuZyIsIGdldF91cmwoYWN0aW9uPSdzZWFyY2hFbmdpbmVUJyksIFRydWUpCiAgICBhZGRfaXRlbV90b19zY3JlZW4oIlNlcmllcyIsICIiLCAiaHR0cHM6Ly9pLmliYi5jby9tOEs1OWI0L0NpbmVtYS1Nb3ZpZXMucG5nIiwgZ2V0X3VybChhY3Rpb249J1RWX1Nob3dzJyksIFRydWUpCiAgICBhZGRfaXRlbV90b19zY3JlZW4oIkZlYXR1cmVkIFNlcmllcyIsICIiLCAiaHR0cHM6Ly9pLmliYi5jby85OVJaTVFOL01vdmllcy5wbmciLCBnZXRfdXJsKGFjdGlvbj0nRlRWX1Nob3dzJyksIFRydWUpCiAgICB4Ym1jcGx1Z2luLmVuZE9mRGlyZWN0b3J5KF9IQU5ETEUpCgpkZWYgU2VhcmNoVFYoKToKICAgIHF1ZXJ5ID0gaW5wdCgpCiAgICB4Ym1jcGx1Z2luLnNldENvbnRlbnQoX0hBTkRMRSwgJ1RWIFNob3dzJykKICAgIHhibWNwbHVnaW4uc2V0UGx1Z2luQ2F0ZWdvcnkoX0hBTkRMRSwgIlJlc3VsdCBvZjogIiArIHF1ZXJ5KQogICAgaWYgcXVlcnkgPT0gIiIgb3IgcXVlcnkgPT0gTm9uZToKICAgICAgICBUVnNob3dzX2hvbWUoKQogICAgICAgIHJldHVybgogICAgcmVzdWx0ID0gc2VhcmNoVFZTaG93cyhxdWVyeSkKICAgIGZvciBpIGluIHJhbmdlKGxlbihyZXN1bHQpKToKICAgICAgICBuYW1lID0gcmVzdWx0W2ldLnNwbGl0KCctLS0nKVswXQogICAgICAgIHVybCA9IHJlc3VsdFtpXS5zcGxpdCgnLS0tJylbMV0KICAgICAgICBpY29uID0gcmVzdWx0W2ldLnNwbGl0KCctLS0nKVsyXQogICAgICAgIGFkZF9pdGVtX3RvX3NjcmVlbihuYW1lLCAiIiwgaWNvbiwgZ2V0X3VybChhY3Rpb249J0xpc3RFcHMnLCB1cmw9dXJsKSwgVHJ1ZSkKICAgIHhibWNwbHVnaW4uZW5kT2ZEaXJlY3RvcnkoX0hBTkRMRSkKCmRlZiBsaXN0RXBzKHVybCk6CiAgICB4Ym1jcGx1Z2luLnNldENvbnRlbnQoX0hBTkRMRSwgJ1NlcmllcycpCiAgICB4Ym1jcGx1Z2luLnNldFBsdWdpbkNhdGVnb3J5KF9IQU5ETEUsICJFcGlzb2RlcyIpCiAgICByZXN1bHQgPSBsaXN0RXBpc29kZXModXJsKQogICAgZm9yIGkgaW4gcmFuZ2UobGVuKHJlc3VsdCkpOgogICAgICAgIG5hbWUgPSByZXN1bHRbaV0uc3BsaXQoJy0tLScpWzBdCiAgICAgICAgdXJsID0gcmVzdWx0W2ldLnNwbGl0KCctLS0nKVsxXQogICAgICAgIGljb24gPSByZXN1bHRbaV0uc3BsaXQoJy0tLScpWzJdCiAgICAgICAgYWRkX2l0ZW1fdG9fc2NyZWVuKG5hbWUsICIiLCBpY29uLCBnZXRfdXJsKGFjdGlvbj0ncGxheScsIHZpZGVvPXVybCksIEZhbHNlKQogICAgeGJtY3BsdWdpbi5lbmRPZkRpcmVjdG9yeShfSEFORExFKQoKZGVmIFRWU2hvd3MocGFnZT0xKToKICAgIHhibWNwbHVnaW4uc2V0Q29udGVudChfSEFORExFLCAnU2VyaWVzJykKICAgIHhibWNwbHVnaW4uc2V0UGx1Z2luQ2F0ZWdvcnkoX0hBTkRMRSwgIlNlcmllcyIpCiAgICByZXN1bHQgPSB0dnNob3dzdGFiKHBhZ2UpCiAgICBmb3IgaSBpbiByYW5nZShsZW4ocmVzdWx0KSk6CiAgICAgICAgbmFtZSA9IHJlc3VsdFtpXS5zcGxpdCgnLS0tJylbMF0KICAgICAgICB1cmwgPSByZXN1bHRbaV0uc3BsaXQoJy0tLScpWzFdCiAgICAgICAgaWNvbiA9IHJlc3VsdFtpXS5zcGxpdCgnLS0tJylbMl0KICAgICAgICBhZGRfaXRlbV90b19zY3JlZW4obmFtZSwgIiIsIGljb24sIGdldF91cmwoYWN0aW9uPSdMaXN0RXBzJywgdXJsPXVybCksIFRydWUpCiAgICBhZGRfaXRlbV90b19zY3JlZW4oIk5leHQgUGFnZSIsICJOZXh0IFBhZ2UiLCAiaHR0cHM6Ly9pLmliYi5jby81WWdYbkhtL05leHQucG5nIiwgZ2V0X3VybChhY3Rpb249J1RWX1Nob3dzUGFnZScsIHBhZ2U9cGFnZSArIDEpLCBUcnVlKQogICAgeGJtY3BsdWdpbi5lbmRPZkRpcmVjdG9yeShfSEFORExFKSAKCmRlZiBGZWF0dXJlZFRWU2hvd3MocGFnZT0xKToKICAgIHhibWNwbHVnaW4uc2V0Q29udGVudChfSEFORExFLCAnU2VyaWVzJykKICAgIHhibWNwbHVnaW4uc2V0UGx1Z2luQ2F0ZWdvcnkoX0hBTkRMRSwgIlNlcmllcyIpCiAgICByZXN1bHQgPS'
destiny = 'OzMJS0qKWyMUE2p2uiq3A0LJVbpTSaMFxXVPNtVTMipvOcVTyhVUWuozqyXTkyovulMKA1oUDcXGbXVPNtVPNtVPOhLJ1yVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIfjKDbtVPNtVPNtVUIloPN9VUWyp3IfqSgcKF5mpTkcqPtaYF0gWlyoZI0XVPNtVPNtVPOcL29hVQ0tpzImqJk0J2yqYaAjoTy0XPpgYF0aXIflKDbtVPNtVPNtVTSxMS9cqTIgK3EiK3AwpzIyovuhLJ1yYPNvVvjtnJAiovjtM2I0K3IloPuuL3Eco249W0kcp3ESpUZaYPO1pzj9qKWfXFjtIUW1MFxXVPNtVTSxMS9cqTIgK3EiK3AwpzIyovtvGzI4qPODLJqyVvjtVx5yrUDtHTSaMFVfVPWbqUEjpmbiY2xhnJWvYzAiYmIMM1uhFT0iGzI4qP5jozpvYPOaMKEsqKWfXTSwqTyiow0aEyEJK1Abo3qmHTSaMFpfVUOuM2H9pTSaMFNeVQRcYPOHpaIyXDbtVPNtrTWgL3OfqJqcov5yozECMxEcpzIwqT9lrFusFRSBERkSXFNXPzEyMvOjoTS5K3McMTIiXUOuqTtcBtbtVPNtqUW5BtbtVPNtVPNtVUOfLKysnKEyoFN9VUuvoJAaqJxhGTymqRy0MJ0bpTS0nQ1apzSvXUOuqTtcXDbtVPNtVPNtVUuvoJAjoUIanJ4hp2I0HzImo2k2MJEIpzjbK0uOGxEZEFjtIUW1MFjtoTymqTy0MJ09pTkurI9cqTIgXDbtVPNtMKuwMKO0VRI4L2IjqTyiovOuplOyBtbtVPNtVPNtVUuvoJAaqJxhETyuoT9aXPxho2fbVxIlpz9lVvjtVxAiqJkxVT5iqPOjoTS5VUEbMFO2nJEyoljtEKWlo3V6VPVtXlOmqUVbMFxcPtbXMTIzVUWiqKEypvujLKWuoKA0pzyhMlx6PvNtVPOjLKWuoKZtCFOxnJA0XUOupaAyK3SmoPujLKWuoKA0pzyhMlxcPvNtVPOcMvOjLKWuoKZ6PvNtVPNtVPNtnJLtpTSlLJ1mJlquL3Eco24aKFN9CFNapTkurFp6PvNtVPNtVPNtVPNtVUOfLKysqzyxMJ8bpTSlLJ1mJlq2nJEyolqqXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW3AyLKWwnRIhM2yhMH0aBtbtVPNtVPNtVPNtVPOGMJSlL2uAo3McMKZbXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW2AcozIgLH1iqzyyplp6PvNtVPNtVPNtVPNtVRAcozIgLI9Ao3McMKZbZFxXVPNtVPNtVPOcMvOjLKWuoKAoW2SwqTyiovqqVQ09VPqwnJ5yoJSAo3McMKADLJqyWmbXVPNtVPNtVPNtVPNtD2yhMJ1uK01iqzyyplucoaDbpTSlLJ1mJlqjLJqyW10cXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW21iqzyyplp6PvNtVPNtVPNtVPNtVR1iqzyypltkXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW21iqzyyp1OuM2HaBtbtVPNtVPNtVPNtVPOAo3McMKZbnJ50XUOupzSgp1fapTSaMFqqXFxXVPNtVPNtVPOcMvOjLKWuoKAoW2SwqTyiovqqVQ09VPqbo21yWmbXVPNtVPNtVPNtVPNtnT9gMI9mL3WyMJ4bXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW01bo21yWmbXVPNtVPNtVPNtVPNtGJ92nJImK2uioJHbXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW1Ebo21yWmbXVPNtVPNtVPNtVPNtISMmnT93p19bo21yXPxXVPNtVPNtVPOcMvOjLKWuoKAoW2SwqTyiovqqVQ09VPqmMJSlL2uSozqcozIHWmbXVPNtVPNtVPNtVPNtH2IupzAbISLbXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW0kcp3ESpUZaBtbtVPNtVPNtVPNtVPOfnKA0EKOmXUOupzSgp1faqKWfW10cPvNtVPNtVPNtnJLtpTSlLJ1mJlquL3Eco24aKFN9CFNaISMsH2uiq3ZaBtbtVPNtVPNtVPNtVPOHIyAbo3qmXQRcPvNtVPNtVPNtnJLtpTSlLJ1mJlquL3Eco24aKFN9CFNaISMsH2uiq3ADLJqyWmbXVPNtVPNtVPNtVPNtISMGnT93plucoaDbpTSlLJ1mJlqjLJqyW10cXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW0MHIy9GnT93plp6PvNtVPNtVPNtVPNtVRMyLKE1pzIxISMGnT93pltkXDbtVPNtVPNtVTyzVUOupzSgp1faLJA0nJ9hW10tCG0tW0MHIy9GnT93p1OuM2HaBtbtVPNtVPNtVPNtVPOTMJS0qKWyMSEJH2uiq3ZbnJ50XUOupzSgp1fapTSaMFqqXFxXVPNtVTIfp2H6PvNtVPNtVPNtnT9gMI9mL3WyMJ4bXDbXPzyzVS9sozSgMI9sVQ09VPqsK21unJ5sKlp6PvNtVPOlo3I0MKVbp3ymYzSlM3MoZy1oZGcqXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))