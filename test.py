from company_name_matching import DefaultMatching

entity_matching = DefaultMatching()
print(entity_matching.match("accenture ltd", "accenture France").score)