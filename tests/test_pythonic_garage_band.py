import pytest

from pythonic_garage_band.garage_band import (
    Band,
    Musician,
    Guitarist,
    Bassist,
    Drummer,
)


# @pytest.mark.skip("todo")
def test_guitarist_str():
    joan = Guitarist("Joan Jett", "guitar")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected


# @pytest.mark.skip("todo")
def test_guitarist_repr():
    joan = Guitarist("Joan Jett" , "guitar")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected


# @pytest.mark.skip("todo")
def test_drummer_str():
    sheila = Drummer("Sheila E.", "drums")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected


# @pytest.mark.skip("todo")
def test_drummer_repr():
    sheila = Drummer("Sheila E.", "drums")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
    assert actual == expected


# @pytest.mark.skip("todo")
def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello", "bass")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected

# @pytest.mark.skip("todo")
def test_bassist_repr():
    meshell = Bassist("Meshell Ndegeocello", "bass")
    actual = repr(meshell)
    expected = "Bassist instance. Name = Meshell Ndegeocello"
    assert actual == expected


# @pytest.mark.skip("todo")
def test_band_name():
    nirvana = Band("Nirvana", [])

    assert nirvana.name == "Nirvana"


# @pytest.mark.skip("todo")
def test_guitarist():
    jimi = Guitarist("Jimi Hendrix", "guitar")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"


# @pytest.mark.skip("todo")
def test_bassist():
    flea = Bassist("Flea" , "bass")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "Bass"


# @pytest.mark.skip("todo")
def test_drummer():
    ginger = Drummer("Ginger Baker", "drums")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "Drums"


# @pytest.mark.skip("todo")
def test_instruments(jimmy):
    assert jimmy.instrument == 'guitar'


# @pytest.mark.skip("todo")
def test_individual_solos(jimmy):
        if jimmy.get_instrument() == "guitar":
            assert jimmy.play_solo() == "face melting guitar solo"
        elif jimmy.get_instrument() == "bass":
            assert jimmy.play_solo() == "bom bom buh bom"
        elif jimmy.get_instrument() == "drums":
            assert jimmy.play_solo() == "rattle boom crash"


# @pytest.mark.skip("todo")
def test_band_members_jimmy(jimmy):
    assert len(jimmy.members) == 4
    assert isinstance(jimmy, Guitarist)
    assert isinstance(jimmy, Musician)
    assert jimmy.name == 'Jimmy'
    assert jimmy.instrument == 'guitar'


# @pytest.mark.skip("todo")
def test_play_solos_for_jimmy(jimmy):
    assert jimmy.play_solo() == "face melting guitar solo"
 
    
# @pytest.mark.skip("todo")
def test_class_tracks_instances():
    assert Band.to_list() == []
    the_nobodies = Band("The Nobodies", [])
    assert len(Band.instances) == 1
    assert Band.instances[0] == the_nobodies


# @pytest.mark.skip("todo")
def test_to_list():
    assert Band.to_list() == []
    the_nobodies = Band("The Nobodies", [])
    all_bands = Band.to_list()
    assert len(all_bands) == 1
    assert all_bands[0] == the_nobodies


#######################
# Fixtures
#######################

@pytest.fixture
def one_band(jimmy):
    data = [
    {'name': 'Jimmy',
     'instrument': 'Guitar'
     },

    {'name': 'Michael',
        'instrument': 'Bass'
     },
    {'name': 'Lisa',
        'instrument': 'Drums'
     }
]

    Band.create_from_data(data)

    assert Band.members[0].name == "Jimmy"

 

@pytest.fixture()
def jimmy():
    return Guitarist('Jimmy', 'guitar')


@pytest.fixture()
def test_data():
  return [
    {'name': 'Jimmy',
     'instrument': 'Guitar'
     },

    {'name': 'Michael',
        'instrument': 'Bass'
     },
    {'name': 'Lisa',
        'instrument': 'Drums'
     }
]
@pytest.fixture(autouse=True)
def clean():
    Band.instances = []
