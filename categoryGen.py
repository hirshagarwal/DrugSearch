mappingStr = ""
items = ['PRODUCTID', 'PRODUCTNDC', 'PRODUCTTYPENAME', 'PROPRIETARYNAME', 'PROPRIETARYNAMESUFFIX', 'NONPROPRIETARYNAME', 'DOSAGEFORMNAME', 'ROUTENAME', 'STARTMARKETINGDATE', 'ENDMARKETINGDATE', 'MARKETINGCATEGORYNAME', 'APPLICATIONNUMBER', 'LABELERNAME', 'SUBSTANCENAME', 'ACTIVE_NUMERATOR_STRENGTH', 'ACTIVE_INGRED_UNIT', 'PHARM_CLASSES', 'DEASCHEDULE', 'NDC_EXCLUDE_FLAG', 'LISTING_RECORD_CERTIFIED_THROUGH']

for item in items:
    mappingStr = mappingStr + ('"' + item + '"' + ':{"type":"string"},\n')
print(mappingStr)