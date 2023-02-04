from stix2.v21 import (Bundle)

for obj in bundle.objects:
    if obj == malware:
        print("------------------")
        print("== MALWARE ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Malware Types: " + str(obj.malware_types))
        print("Is Family:" + str(obj.is_family))
        print("Kill Chain: " + str(obj.kill_chain_phases))

    elif obj == indicator:
        print("------------------")
        print("== INDICATOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Indicator Types: " + str(obj.indicator_types))
        print("Pattern: " + obj.pattern)
        print("Pattern Type: " + obj.pattern_type)
        print("Valid From: " + str(obj.valid_from))

    elif obj == relationship:
        print("------------------")
        print("== RELATIONSHIP ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Type: " + obj.type)
        print("Relationship Type: " + obj.relationship_type)
        print("Source Ref: " + obj.source_ref)
        print("Target Ref: " + obj.target_ref)