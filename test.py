from company_name_matching import DefaultMatching
matching_object = DefaultMatching()
print("Unither Pharmaceuticals SAS", "Unither Pharmaceuticals Inc", matching_object.match("Unither Pharmaceuticals SAS", "Unither Pharmaceuticals Inc").score)

print("Groupe BPCE + ", "BPCE, score: ", matching_object.match("Groupe BPCE", "BPCE").score)

print("Groupe crédit agricole + ", "crédit agricole, score:", matching_object.match("Groupe crédit agricole", "crédit agricole").score)

print("Groupe caisse d'épargne + ", "caisse d'épargne, score:", matching_object.match("Groupe caisse d'épargne", "caisse d'épargne").score)

print("Groupe banque populaire + ", "banque populaire, score:", matching_object.match("Groupe banque populaire", "banque populaire").score)

print("Groupe efdscfed rfdcfd + ", "efdscfed rfdcfd, score:", matching_object.match("Groupe efdscfed rfdcfd", "efdscfed rfdcfd").score)

print("accenture limitee ltd + ", "accenture, score:", matching_object.match("accenture limitee ltd", "accenture").score)

print("accenture limitee ltd + ", "accenture ltd, score:", matching_object.match("accenture limitee ltd", "accenture ltd").score)

print("accenture limitee caisse + ", "accenture ltd, score:", matching_object.match("accenture limitee caisse", "accenture ltd").score)

print("accenture incorporated caisse + ", "accenture ltd, score:", matching_object.match("accenture incorporated caisse", "accenture ltd").score)

print("accenture incorporated caisse ltd + ", "accenture, score:", matching_object.match("accenture incorporated caisse ltd", "accenture").score)

print("accenture incorporated ltd + ", "accenture, score:", matching_object.match("accenture incorporated ltd", "accenture").score)

print("accenture utility ltd general + ", "accenture, score:", matching_object.match("accenture utility ltd general", "accenture").score)