from Units.ConcreateCreators import CreatorPersonality


Character_client = CreatorPersonality('Hulk').create_character()
print(Character_client.health)
print(Character_client)
