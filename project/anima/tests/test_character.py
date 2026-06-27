from anima.core.characters import Character


def test_character_name() -> None :
    character = Character("Aria")
    assert character.name