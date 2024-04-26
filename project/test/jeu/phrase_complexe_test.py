import pytest
from project.src.jeu.PhraseComplexe import PhraseComplexe

class TestQuestion: 
    def test_instanciation_classe_abstraite(self):
        with pytest.raises(NotImplementedError):
            PhraseComplexe()
            