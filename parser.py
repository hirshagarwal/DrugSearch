from elasticsearch import Elasticsearch

f = open('product.txt', 'r')

# Get the first line (category names)
text = f.readline()
text = text.strip("\n")

categoryList = ['PRODUCTID', 'PRODUCTNDC', 'PRODUCTTYPENAME', 'PROPRIETARYNAME', 'PROPRIETARYNAMESUFFIX', 'NONPROPRIETARYNAME', 'DOSAGEFORMNAME', 'ROUTENAME', 'STARTMARKETINGDATE', 'ENDMARKETINGDATE', 'MARKETINGCATEGORYNAME', 'APPLICATIONNUMBER', 'LABELERNAME', 'SUBSTANCENAME', 'ACTIVE_NUMERATOR_STRENGTH', 'ACTIVE_INGRED_UNIT', 'PHARM_CLASSES', 'DEASCHEDULE', 'NDC_EXCLUDE_FLAG', 'LISTING_RECORD_CERTIFIED_THROUGH']


mapping = {
    "drug":{
        "PRODUCTID":{"type":"string"},
        "PRODUCTNDC":{"type":"string"},
        "PRODUCTTYPENAME":{"type":"string"},
        "PROPRIETARYNAME":{"type":"string"},
        "PROPRIETARYNAMESUFFIX":{"type":"string"},
        "NONPROPRIETARYNAME":{"type":"string"},
        "DOSAGEFORMNAME":{"type":"string"},
        "ROUTENAME":{"type":"string"},
        "STARTMARKETINGDATE":{"type":"string"},
        "ENDMARKETINGDATE":{"type":"string"},
        "MARKETINGCATEGORYNAME":{"type":"string"},
        "APPLICATIONNUMBER":{"type":"string"},
        "LABELERNAME":{"type":"string"},
        "SUBSTANCENAME":{"type":"string"},
        "ACTIVE_NUMERATOR_STRENGTH":{"type":"string"},
        "ACTIVE_INGRED_UNIT":{"type":"string"},
        "PHARM_CLASSES":{"type":"string"},
        "DEASCHEDULE":{"type":"string"},
        "NDC_EXCLUDE_FLAG":{"type":"string"},
        "LISTING_RECORD_CERTIFIED_THROUGH":{"type":"string"},
    }
}

es = Elasticsearch()
# es.indices.create("drugs")
# es.indices.put_mapping(index="drugs", doc_type="drug", body=mapping)

while True:
    text = f.readline()
    text = text.strip("\n")
    splitText = text.split("\t")
    # print(splitText)
    content = {}
    for i in range(len(categoryList)):
        content[categoryList[i]] = splitText[i]
    print("Writing: " + splitText[5] + " to database")
    es.index(index="drugs", doc_type="drug", id=splitText[0], body=content)

